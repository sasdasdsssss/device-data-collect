import sys
import numpy as np

import struct
import time
from config import system_memory as SystemMemory
from config import system_constant as SystemConstants


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
                    time_start = time.time()  # 记录开始时间
                    self.start = 0
                    rxFramedata = np.squeeze(self.data.reshape(-1, 16 * 1024))

                    Framedata1 = rxFramedata[0:self.FrameNum * 1024:4]
                    Framedata2 = rxFramedata[1:self.FrameNum * 1024:4]
                    Framedata3 = rxFramedata[2:self.FrameNum * 1024:4]
                    Framedata4 = rxFramedata[3:self.FrameNum * 1024:4]

                    for i in range(4096):
                        self.data2[i] = bytesToFloat(Framedata4[i], Framedata3[i], Framedata2[i],
                                                     Framedata1[i])
                    if (MODE == 0):
                        self.myWin.T1_phaseBreath = self.data2[1600:1600 + 256]
                        self.myWin.T1_phaseHeart = self.data2[1900:1900 + 256]
                        self.myWin.T1_amp = self.data2[2700:2700 + 32]
                        self.myWin.T1_wave = self.data2[2250:2250 + 256]

                        T1_Breath_val = self.data2[531 * 5]
                        T1_Heart_val = self.data2[531 * 5 + 1]
                        T1_RNG_val = self.data2[531 * 5 + 2]
                        T1_REAL_val = self.data2[531 * 5 + 3]

                        breath_str = str(T1_Breath_val)
                        heart_str = str(T1_Heart_val)

                        SystemMemory.set_value("breathe_value", breath_str)
                        SystemMemory.set_value("heart_value", heart_str)

                        self.myWin.label_T1_2.setText("呼吸频率：" + breath_str + " 次/分钟")
                        self.myWin.label_T2_2.setText("心率：" + heart_str + " 次/分钟")
                    if (MODE == 1):
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
                    # self.nFrame = self.nFrame+1
                    # if self.nFrame>50:
                    #     self.nFrame = 0
                    time_end = time.time()  # 记录结束时间
                    time_sum = time_end - time_start  # 计算的时间差为程序的执行时间，单位为秒/s
                    # print(time_sum)


def bytesToFloat(h1, h2, h3, h4):
    ba = bytearray()
    ba.append(h1)
    ba.append(h2)
    ba.append(h3)
    ba.append(h4)
    return struct.unpack("!f", ba)[0]
