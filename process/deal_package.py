import math
import sys
import numpy as np

import struct
import time
from config import system_memory as SystemMemory
from config.system_constant import SystemConstants

from sklearn.cluster import DBSCAN


# 处理数据类
class DealPackage:

    def __init__(self, myWin, mySocket):
        self.myWin = myWin
        self.mySocket = mySocket
        self.count = 0
        self.start = 0
        self.FrameNum = 16
        self.TargetNum = 512
        self.data1 = [0 for index in range(1024)]
        self.data2 = [0 for index in range(4096)]
        self.data = [self.data1 for index in range(self.FrameNum)]
        self.data = np.array(self.data)
        self.nFrame = 0
        self.data_counts = 0
        self.breathe_data_list = []
        self.heart_data_list = []
        self.person_staus = []
        self.MODE = 0

    def wired_packet_callback(self, win_pcap, param, header, pkt_data):
        packet = list(pkt_data)
        if packet[0] == 0xFF and packet[1] == 0xFF and packet[2] == 0xFF \
                and packet[3] == 0xFF and packet[4] == 0xFF and packet[5] == 0xFF \
                and packet[6] == 0x48 and packet[7] == 0x5B and packet[8] == 0x39 \
                and packet[9] == 0xC2 and packet[10] == 0x7D and packet[11] == 0xF8 \
                and header.contents.caplen == 1040:
            self.count = self.count + 1
            self.deal_parameter_package(packet, SystemConstants.WIRED_NETWORK_TYPE)

    def deal_location_wifi_package(self):
        while True:
            packet_in, addr = self.mySocket.recvfrom(1040)
            result_recv_data = packet_in.hex()
            # print(result_recv_data)
            ls = []
            a = len(result_recv_data) // 2

            for i in range(len(result_recv_data) // 2):
                tmp = result_recv_data[i * 2] + result_recv_data[i * 2 + 1]
                tmp_int = int(tmp, 16)
                ls.append(tmp_int)

            packet = ls
            self.FrameNum = 16
            self.TargetNum = 512
            self.deal_location_package(packet, SystemConstants.WIFI_NETWORK_TYPE)

    def deal_parameter_wifi_package(self):
        while True:
            packet_in, addr = self.mySocket.recvfrom(1040)
            if len(packet_in) == 1040:
                result_recv_data = packet_in.hex()
                # print(result_recv_data)
                ls = []
                a = len(result_recv_data) // 2

                for i in range(len(result_recv_data) // 2):
                    tmp = result_recv_data[i * 2] + result_recv_data[i * 2 + 1]
                    tmp_int = int(tmp, 16)
                    ls.append(tmp_int)

                packet = ls

                self.FrameNum = 16
                self.TargetNum = 512
                self.count = self.count + 1
                self.deal_parameter_package(packet, SystemConstants.WIFI_NETWORK_TYPE)

    def deal_parameter_package(self, packet, network_type):
        if packet[14] == 0:
            self.start = 1
            self.count = 0
            self.MODE = packet[12]
        if self.start == 1:
            tmp = packet[16:1040]
            self.data[self.count, 0:1024] = tmp
            if self.count == (self.FrameNum - 1):
                self.start = 0
                rxFramedata = np.squeeze(self.data.reshape(-1, 16 * 1024))

                Framedata1 = rxFramedata[0:self.FrameNum * 1024:4]
                Framedata2 = rxFramedata[1:self.FrameNum * 1024:4]
                Framedata3 = rxFramedata[2:self.FrameNum * 1024:4]
                Framedata4 = rxFramedata[3:self.FrameNum * 1024:4]

                for i in range(4096):
                    if network_type == SystemConstants.WIRED_NETWORK_TYPE:
                        self.data2[i] = bytesToFloat(Framedata4[i], Framedata3[i], Framedata2[i],
                                                     Framedata1[i])
                    elif network_type == SystemConstants.WIFI_NETWORK_TYPE:
                        self.data2[i] = bytesToFloat(Framedata3[i], Framedata4[i], Framedata1[i],
                                                     Framedata2[i])
                # 0 时，处理呼吸数据
                if self.MODE == 0:
                    self.myWin.T1_phaseBreath = self.data2[1600:1600 + 256]
                    self.myWin.T1_phaseHeart = self.data2[1900:1900 + 256]
                    self.myWin.T1_amp = self.data2[2700:2700 + 32]
                    self.myWin.T1_wave = self.data2[2250:2250 + 256]

                    T1_Breath_val = self.data2[531 * 5]
                    T1_Heart_val = self.data2[531 * 5 + 1]
                    T1_RNG_val = self.data2[531 * 5 + 2]
                    T1_REAL_val = self.data2[531 * 5 + 3]

                    # 10个点为一组，去掉最大，去掉最小
                    self.data_counts = self.data_counts + 1
                    self.breathe_data_list.append(T1_Breath_val)
                    self.heart_data_list.append(T1_Heart_val)
                    if self.data_counts >= 10:
                        self.breathe_data_list.remove(max(self.breathe_data_list))
                        self.breathe_data_list.remove(min(self.breathe_data_list))
                        breath_average = sum(self.breathe_data_list) / len(self.breathe_data_list)
                        self.heart_data_list.remove(max(self.heart_data_list))
                        self.heart_data_list.remove(min(self.heart_data_list))
                        heart_average = sum(self.heart_data_list) / len(self.heart_data_list)
                        breath_str = str(int(breath_average))
                        heart_str = str(int(heart_average))
                        SystemMemory.set_value(SystemConstants.BREATHE_DATA_VALUE, breath_str)
                        SystemMemory.set_value(SystemConstants.HEART_DATA_VALUE, heart_str)
                        self.myWin.label_T1_2.setText("呼吸：" + breath_str + " 次/分钟")
                        self.myWin.label_T2_2.setText("心率：" + heart_str + " 次/分钟")
                        self.data_counts = 0
                        self.breathe_data_list = []
                        self.heart_data_list = []

    def deal_location_package(self, packet, package_type):
        self.count = self.count + 1
        if packet[14] == 0:
            self.start = 1
            self.count = 0
        if self.start == 1:
            tmp = packet[16:1040]
            self.data[self.count, 0:1024] = tmp
            if self.count == (self.FrameNum - 1):
                self.start = 0
                rxFrameData = np.squeeze(self.data.reshape(-1, 16 * 1024))

                FrameData1 = rxFrameData[0:self.FrameNum * 1024:4]
                FrameData2 = rxFrameData[1:self.FrameNum * 1024:4]
                FrameData3 = rxFrameData[2:self.FrameNum * 1024:4]
                FrameData4 = rxFrameData[3:self.FrameNum * 1024:4]

                for i in range(4096):
                    if package_type == SystemConstants.WIRED_NETWORK_TYPE:
                        self.data2[i] = bytesToFloat(FrameData4[i], FrameData3[i], FrameData2[i], FrameData1[i])
                    elif package_type == SystemConstants.WIFI_NETWORK_TYPE:
                        self.data2[i] = bytesToFloat(FrameData3[i], FrameData4[i], FrameData1[i], FrameData2[i])

                self.myWin.ACTION_TYPE_DISPLAY = int(self.data2[3001])
                tnum = int(self.data2[3002] / 1)

                self.myWin.TNUM = tnum

                R = np.array(self.data2[0:self.TargetNum * 5:5])
                V = np.array(self.data2[1:self.TargetNum * 5:5])
                P = np.array(self.data2[2:self.TargetNum * 5:5])
                A = np.array(self.data2[3:self.TargetNum * 5:5])
                E = np.array(self.data2[4:self.TargetNum * 5:5])
                P_cal = np.pi * P / 180.0
                E_cal = np.pi * E / 180.0
                R_cal = R * np.cos(E_cal)
                H_cal = R * np.sin(E_cal)
                R_dis = R_cal * np.cos(P_cal)
                L_dis = R_cal * np.sin(P_cal)
                H_dis = H_cal

                self.myWin.pos = np.zeros((self.TargetNum, 3))
                cnt = 0
                for i in range(self.TargetNum):
                    if A[i] < 0.05:
                        continue
                    self.myWin.pos[cnt, 0] = R_dis[i]
                    self.myWin.pos[cnt, 1] = L_dis[i]
                    self.myWin.pos[cnt, 2] = H_dis[i]
                    cnt = cnt + 1
                # 半秒处理一次
                self.data_counts = self.data_counts + 1
                if self.data_counts >= 10:
                    R_real = np.zeros(self.TargetNum)
                    L_real = np.zeros(self.TargetNum)
                    H_real = np.zeros(self.TargetNum)
                    for i in range(self.TargetNum):
                        if A[i] < 0.05:
                            continue
                        R_real[i] = R_dis[i]
                        L_real[i] = L_dis[i]
                        H_real[i] = H_dis[i]

                    # 根据 R_dis 和 L_dis 创建一个新的二维数组
                    points = np.column_stack((R_real, L_real))
                    # print(points)
                    self.deal_cluster_person_point(points)
                    self.data_counts = 0

    def deal_cluster_person_point(self, points):
        # 使用 DBSCAN 算法进行聚类
        dbscan = DBSCAN(eps=1, min_samples=1)  # eps 半径、min_samples 最小样本数
        clusters = dbscan.fit_predict(points)

        # 获取群体数量（忽略噪声点，即 cluster == -1 的点）
        num_clusters = len(set(clusters)) - (1 if -1 in clusters else 0)

        # 将相近的点分组到各自的数组中
        clustered_points = {}
        for i, cluster in enumerate(clusters):
            if cluster == -1:
                continue
            if cluster not in clustered_points:
                clustered_points[cluster] = []
            clustered_points[cluster].append(points[i])

        """
          # 打印分组后的点
          for cluster, points in clustered_points.items():
              print(f"群体 {cluster}: {points}")
          """
        for cluster, points in clustered_points.items():
            points_array = np.array(points)
            avg_R_dis = np.mean(points_array[:, 0])
            avg_L_dis = np.mean(points_array[:, 1])
            # 存储在 myWin.pos 中
            cur_person_pos_tuple = (round(avg_R_dis, 6), round(avg_L_dis, 6))
            if abs(cur_person_pos_tuple[0]) < 0.5 and abs(cur_person_pos_tuple[1]) < 0.5:
                return
            self.modify_person_pos_dict(cur_person_pos_tuple)

    # 比较在缓存中是否存在该位置的人
    def modify_person_pos_dict(self, new_cluster_person_point):
        person_pos_dict = SystemMemory.get_value("person_pos_dict")
        if new_cluster_person_point[0] > 7.4 or new_cluster_person_point[0] < 1:
            return
        if new_cluster_person_point[1] > 3.0 or new_cluster_person_point[1] < -4:
            return
        if person_pos_dict:
            if self.update_person_location(new_cluster_person_point, person_pos_dict):
                # 没有人，人从其他地方出现，添加人
                print("没有人，人从其他地方出现，添加人")
                person_pos_dict[len(person_pos_dict)] = new_cluster_person_point
            # 门附近 出现人，进入，添加人
            if self.person_in_door(new_cluster_person_point) == 1:
                print("门附近 出现人，进入，添加人")
                person_pos_dict[len(person_pos_dict)] = new_cluster_person_point
            elif self.person_in_door(new_cluster_person_point) == 2:
                print("门附近 出现人，出门 ，减少人")
                # person_pos_dict.pop(person_num)
        else:
            # 添加一个人
            print("没有记录，添加人")
            person_pos_dict = {0: new_cluster_person_point}
        SystemMemory.set_value("person_pos_dict", person_pos_dict)
        self.myWin.modify_person_location_list(person_pos_dict)

    def update_person_location(self, new_cluster_person_point, person_pos_dict):
        sqrt_diff_list_x = []
        sqrt_diff_list_y = []
        sqrt_diff_list_all = []
        for person_num, person_pos in person_pos_dict.items():
            sqrt_diff_list_x.append(abs(new_cluster_person_point[0] - person_pos[0]))
            sqrt_diff_list_y.append(abs(new_cluster_person_point[1] - person_pos[1]))
            sqrt_diff_list_all.append(self.calculate_sqrt_diff(new_cluster_person_point[0], person_pos[0],
                                                               new_cluster_person_point[1],
                                                               person_pos[1]))
        min_index = sqrt_diff_list_all.index(min(sqrt_diff_list_all))
        if sqrt_diff_list_all[min_index] < 4:
            if sqrt_diff_list_x[min_index] < 1 and sqrt_diff_list_y[min_index] < 1:
                print("更新人的位置" + str(new_cluster_person_point))
                person_pos_dict[min_index] = new_cluster_person_point
                return False
            else:
                return False
        else:
            return True

    #  判断人是否进入
    @staticmethod
    def person_in_door(new_cluster_person_point):
        old_door_cluseter_person_point = SystemMemory.get_value("old_door_cluseter_person_point")
        # 到门附近，开始判断是进入还是出去
        if abs(new_cluster_person_point[0] - SystemConstants.DOOR_LOCATION_X) < 1 and abs(
                new_cluster_person_point[1] - SystemConstants.DOOR_LOCATION_Y) < 1:
            print("处理门附近的聚点信息 " + str(new_cluster_person_point))
            # 设置旧的坐标
            SystemMemory.set_value("old_door_cluseter_person_point", new_cluster_person_point)
            if old_door_cluseter_person_point:
                # 如果坐标减小，是进入
                if abs(old_door_cluseter_person_point[0] - new_cluster_person_point[0]) < 0.2:
                    return 0
                elif old_door_cluseter_person_point[0] - new_cluster_person_point[0] > 0.2:
                    print("----------进入进入进入---------------进入----进入------------------------")
                    # time.sleep(0.05)
                    return 1
                # 如果坐标增大，是出去
                elif old_door_cluseter_person_point[0] - new_cluster_person_point[0] < -0.2:
                    print("-------------------出去-出去-出去-------出去--------------出去-出去-出去----------")
                    # time.sleep(0.05)
                    return 2
            else:
                # 没有前一个坐标，判断也是进入
                return 0
        else:
            # 不在门附近
            return 0

    @staticmethod
    def calculate_sqrt_diff(a, b, c, d):
        diff1 = (a - b) ** 2
        diff2 = (c - d) ** 2
        sqrt_sum = math.sqrt(diff1 + diff2)
        return sqrt_sum


def bytesToFloat(h1, h2, h3, h4):
    ba = bytearray()
    ba.append(h1)
    ba.append(h2)
    ba.append(h3)
    ba.append(h4)
    return struct.unpack("!f", ba)[0]
