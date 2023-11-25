import sys
import numpy as np

import struct
import time
from config import system_memory as SystemMemory
from config.system_constant import SystemConstants

import socket


# 处理数据类
class DealPackage:

    def __init__(self, myWin):
        self.myWin = myWin
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

    def packet_callback(self, win_pcap, param, header, pkt_data):
        packet = list(pkt_data)
        global MODE
        if packet[0] == 0xFF and packet[1] == 0xFF and packet[2] == 0xFF \
                and packet[3] == 0xFF and packet[4] == 0xFF and packet[5] == 0xFF \
                and packet[6] == 0x48 and packet[7] == 0x5B and packet[8] == 0x39 \
                and packet[9] == 0xC2 and packet[10] == 0x7D and packet[11] == 0xF8 \
                and header.contents.caplen == 1040:
            self.count = self.count + 1
            if packet[14] == 0:
                self.start = 1
                self.count = 0
                MODE = packet[12]
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
                        self.data2[i] = bytesToFloat(Framedata4[i], Framedata3[i], Framedata2[i],
                                                     Framedata1[i])
                    # 0 时，处理呼吸数据
                    if MODE == 0:
                        self.myWin.T1_phaseBreath = self.data2[1600:1600 + 256]
                        self.myWin.T1_phaseHeart = self.data2[1900:1900 + 256]
                        self.myWin.T1_amp = self.data2[2700:2700 + 32]
                        self.myWin.T1_wave = self.data2[2250:2250 + 256]

                        T1_Breath_val = self.data2[531 * 5]
                        T1_Heart_val = self.data2[531 * 5 + 1]
                        T1_RNG_val = self.data2[531 * 5 + 2]
                        T1_REAL_val = self.data2[531 * 5 + 3]

                        # 增加多次平均值处理
                        self.data_counts = self.data_counts + 1
                        self.breathe_data_list.append(T1_Breath_val)
                        self.heart_data_list.append(T1_Heart_val)
                        if self.data_counts >= 20:
                            breath_average = sum(self.breathe_data_list) / len(self.breathe_data_list)
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
                    # 1 时，处理坐标数据
                    if MODE == 1:
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
                        print(f"坐标：{0},{1},{2}" % R_dis, L_dis, H_dis)
                        self.myWin.pos = np.zeros((self.TargetNum, 3))
                        cnt = 0
                        for i in range(self.TargetNum):
                            if A[i] < 0.05:
                                continue
                            self.myWin.pos[cnt, 0] = R_dis[i]
                            self.myWin.pos[cnt, 1] = L_dis[i]
                            self.myWin.pos[cnt, 2] = H_dis[i]
                            cnt = cnt + 1

    def deal_wifi_package(self):
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        global count, start, FrameNum, TargetNum
        global data, data2
        global t0HeartStore, t1HeartStore, t0BreathStore, t1BreathStore
        global MODE

        packet_in, addr = mySocket.recvfrom(1040)
        if len(packet_in) == 1040:
            result_recv_data = packet_in.hex()
            ls = []
            a = len(result_recv_data) // 2

            for i in range(len(result_recv_data) // 2):
                tmp = result_recv_data[i * 2] + result_recv_data[i * 2 + 1]
                tmp_int = int(tmp, 16)
                ls.append(tmp_int)

            packet = ls

            FrameNum = 16
            TargetNum = 512
            global nFrame
            count = count + 1

            if packet[14] == 0:
                start = 1
                count = 0
                MODE = packet[12]
            if start == 1:
                tmp = packet[16:1040]
                data[count, 0:1024] = tmp
                if count == (FrameNum - 1):
                    start = 0
                    rxFrameData = np.squeeze(data.reshape(-1, 16 * 1024))

                    FrameData1 = rxFrameData[0:FrameNum * 1024:4]
                    FrameData2 = rxFrameData[1:FrameNum * 1024:4]
                    FrameData3 = rxFrameData[2:FrameNum * 1024:4]
                    FrameData4 = rxFrameData[3:FrameNum * 1024:4]

                    for i in range(4096):
                        data2[i] = bytesToFloat(FrameData3[i], FrameData4[i], FrameData1[i], FrameData2[i])
                    if MODE == 0:
                        self.myWin.T1_phaseBreath = data2[1600:1600 + 256]
                        self.myWin.T1_phaseHeart = data2[1900:1900 + 256]
                        self.myWin.T1_amp = data2[2700:2700 + 32]
                        self.myWin.T1_wave = data2[2250:2250 + 256]

                        T1_Breath_val = data2[531 * 5]
                        T1_Heart_val = data2[531 * 5 + 1]
                        T1_RNG_val = data2[531 * 5 + 2]
                        T1_REAL_val = data2[531 * 5 + 3]

                        a = str(T1_Breath_val)
                        b = str(T1_Heart_val)

                        self.myWin.label_T1_2.setText("呼吸：" + a + " 次/分钟")
                        self.myWin.label_T2_2.setText("心率：" + b + " 次/分钟")

                        self.myWin.pos = np.zeros((TargetNum, 3))
                        cnt = 1
                        self.myWin.pos[0, 0] = data2[532 * 5]
                        self.myWin.pos[0, 1] = data2[532 * 5 + 1]

                    if MODE == 1:
                        R = np.array(data2[0:TargetNum * 5:5])
                        V = np.array(data2[1:TargetNum * 5:5])
                        P = np.array(data2[2:TargetNum * 5:5])
                        A = np.array(data2[3:TargetNum * 5:5])
                        E = np.array(data2[4:TargetNum * 5:5])
                        P_cal = np.pi * P / 180.0
                        E_cal = np.pi * E / 180.0
                        R_cal = R * np.cos(E_cal)
                        H_cal = R * np.sin(E_cal)
                        R_dis = R_cal * np.cos(P_cal)
                        L_dis = R_cal * np.sin(P_cal)
                        H_dis = H_cal

                        self.myWin.pos = np.zeros((TargetNum, 3))

                        cnt = 0
                        for i in range(TargetNum):
                            if A[i] < 0.05:
                                continue
                            self.myWin.pos[cnt, 0] = R_dis[i]
                            self.myWin.pos[cnt, 1] = L_dis[i]
                            self.myWin.pos[cnt, 2] = H_dis[i]
                            cnt = cnt + 1


def bytesToFloat(h1, h2, h3, h4):
    ba = bytearray()
    ba.append(h1)
    ba.append(h2)
    ba.append(h3)
    ba.append(h4)
    return struct.unpack("!f", ba)[0]
