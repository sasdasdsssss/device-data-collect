import sys
from datetime import datetime

import numpy as np
from PySide6 import QtWidgets, QtCore
import pyqtgraph as pg
from PySide6.QtCore import Qt

from client.socket_client import SocketClient
from ui.ui_main_window import Ui_MainWindow
from winpcapy import WinPcapDevices
from winpcapy import WinPcapUtils
import struct
import time
import threading
import serial
import serial.tools.list_ports
import PySide6.QtGui as qg
from loguru import logger

import socket

import os  # 用于处理文件

from PySide6.QtGui import QVector3D, QLinearGradient, QIcon
from PySide6.QtDataVisualization import QAbstract3DSeries, QScatter3DSeries, \
    QScatterDataItem, Q3DCamera, QScatterDataProxy, Q3DTheme, Q3DScatter, QAbstract3DGraph
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout

from process.deal_package import DealPackage

from config import system_memory as SystemMemory
from config.system_constant import SystemConstants

from grab.find_device import FindDevice


# 界面类
class MyGraphWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyGraphWindow, self).__init__()
        self.setupUi(self)  # 初始化窗口
        self.setWindowTitle('雷达数据发送')
        self.setWindowIcon(QIcon('ui/main.ico'))
        self.p1, self.p11, self.p2, self.p22, self.curve1, self.curve11, \
            self.curve2, self.curve22, self.pos, self.pos1, self.series, self.Q3D = self.set_graph_ui()  # 设置绘图窗口
        self.T1_phaseBreath, self.T1_phaseHeart, self.T1_amp, self.T1_wave, \
            self.ST_x, self.ST_y, self.TNUM, self.GES_x, self.GES_y, \
            self.ACTION_TYPE_DISPLAY, self.ACTION_TYPE_DISPLAY2 = self.init_data()
        self.btn1.clicked.connect(self.open_network_card)  # 打开网卡
        self.btn_open_wifi.clicked.connect(self.open_wifi_receive)  # 打开wifi接收
        self.btn_save_server.clicked.connect(self.save_server_information)  # 保存服务端数据
        self.btn_clear_log.clicked.connect(self.clear_log_text)  # 保存服务端数据
        self.btn_start_send.clicked.connect(self.start_send_thread)  # 发送数据

        self.btn_save_server.setEnabled(True)

    @staticmethod
    def init_data():
        T1_phaseBreath = np.zeros(300)
        T1_phaseHeart = np.zeros(300)
        T1_amp = np.zeros(300)
        T1_wave = np.zeros(300)
        ST_x = np.zeros(10)
        ST_y = np.zeros(10)
        TNUM = 0

        GES_x = np.zeros(1)
        GES_y = np.zeros(1)
        GES_x[0] = 0.5
        GES_y[0] = 0.5
        ACTION_TYPE_DISPLAY = 0
        ACTION_TYPE_DISPLAY2 = 0
        return T1_phaseBreath, T1_phaseHeart, T1_amp, T1_wave, ST_x, ST_y, TNUM, GES_x, GES_y, ACTION_TYPE_DISPLAY, ACTION_TYPE_DISPLAY2

    def set_graph_ui(self):
        pg.setConfigOptions(antialias=True)  # pg全局变量设置函数，antialias=True开启曲线抗锯齿

        pos = np.zeros((1024, 3))
        pos1 = np.zeros((1024, 3))

        win_1 = pg.GraphicsLayoutWidget()  # 创建pg layout，可实现数据界面布局自动管理
        # Enable antialiasing for prettier plots
        self.graph2.addWidget(win_1)

        win_2 = pg.GraphicsLayoutWidget()  # 创建pg layout，可实现数据界面布局自动管理
        # Enable antialiasing for prettier plots
        self.graph4.addWidget(win_2)

        win_3 = pg.GraphicsLayoutWidget()  # 创建pg layout，可实现数据界面布局自动管理
        # Enable antialiasing for prettier plots
        self.graph5.addWidget(win_3)

        win_4 = pg.GraphicsLayoutWidget()  # 创建pg layout，可实现数据界面布局自动管理
        # Enable antialiasing for prettier plots
        self.graph6.addWidget(win_4)

        p1 = win_1.addPlot(title="呼吸波形")
        # p1.setYRange(-15,15)
        curve1 = p1.plot(pen='y')
        p2 = win_2.addPlot(title="雷达频谱")
        # p2.setYRange(-15, 15)
        curve2 = p2.plot(pen='w')
        # win.nextRow()
        p11 = win_3.addPlot(title="原始波形")
        curve11 = p11.plot(pen='g')
        p22 = win_4.addPlot(title="心率波形")
        curve22 = p22.plot(pen='r')

        list_device = WinPcapDevices.list_devices()
        list_device_value = list(list_device.values())
        list_device_key = list(list_device.keys())

        # 初始化网卡信息
        device_index = 0
        count = 0
        for values in list_device_value:
            logger.info(values)
            if "Realtek USB" in values:
                device_index = count
            self.comboBox.addItem(values)
            count = count + 1
        self.comboBox.setCurrentIndex(device_index)

        # 初始化ip地址和端口信息
        SystemMemory.set_value(SystemConstants.IP_NAME, self.lineEdit_IP.text())
        SystemMemory.set_value(SystemConstants.PORT_NAME, int(self.lineEdit_port.text()))
        SystemMemory.set_value(SystemConstants.SPAN_NAME, int(self.lineEdit_span_millisecond.text()))

        self.label_T1_2.setText("呼吸：")
        self.label_T2_2.setText("心率：")

        Q3D = Q3DScatter()
        container = QWidget.createWindowContainer(Q3D)
        self.graph8.addWidget(container, True)

        series = QScatter3DSeries()
        series.setMeshSmooth(1)
        Q3D.addSeries(series)
        Q3D.axisX().setTitle("横向距离")
        Q3D.axisX().setTitleVisible(True)
        Q3D.axisX().setRange(-20, 20)
        Q3D.axisY().setTitle("高度")
        Q3D.axisY().setTitleVisible(True)
        Q3D.axisY().setRange(-5, 5)
        Q3D.axisZ().setTitle("纵向距离")
        Q3D.axisZ().setTitleVisible(True)
        Q3D.axisZ().setRange(0, 50)
        Q3D.activeTheme().setLabelBackgroundEnabled(False)
        Q3D.activeTheme().setBackgroundColor(qg.QColor(50, 50, 50))
        Q3D.activeTheme().setType(Q3DTheme.ThemeRetro)
        Q3D.setShadowQuality(QAbstract3DGraph.ShadowQualityNone)
        Q3D.activeTheme().setGridEnabled(True)

        series.setMesh(QAbstract3DSeries.MeshPoint)
        series.setSingleHighlightColor(qg.QColor(0, 0, 90))
        series.setBaseColor(qg.QColor(0, 255, 255))
        series.setItemSize(1)

        Qline = QLinearGradient()
        Qline.setColorAt(0.0, qg.QColor(0, 255, 0))
        Qline.setColorAt(1.0, qg.QColor(255, 0, 0))
        Qline.setColorAt(2.0, qg.QColor(0, 0, 255))
        series.setBaseGradient(Qline)
        series.setColorStyle(Q3DTheme.ColorStyleRangeGradient)

        camera = Q3D.scene().activeCamera()
        camera.setZoomLevel(120)
        camera.setCameraPreset(Q3DCamera.CameraPresetFront)

        return p1, p11, p2, p22, curve1, curve11, curve2, curve22, pos, pos1, series, Q3D

    def init_wifi_device_list(self, device_ip_list):
        self.listWidget_2.clear()
        self.listWidget_2.addItem("无线设备列表")
        for device in device_ip_list:
            self.listWidget_2.addItem(device)

    def modify_person_location_list(self, person_pos_dict):
        self.listWidgetPersonLocation.clear()
        self.listWidgetPersonLocation.addItem("坐标列表")
        for person_num, person_location in person_pos_dict.items():
            self.listWidgetPersonLocation.addItem(str(person_num) + " : " + str(person_location))

    def wired_receive_thread(self):
        # 有线设备线程
        net_card = self.comboBox.currentText()
        dealPackage = DealPackage(self, None, None)
        WinPcapUtils.capture_on(pattern=net_card, callback=dealPackage.wired_packet_callback)

    def picture_draw_timer(self):
        self.curve1.setData(self.T1_phaseBreath)
        self.curve11.setData(self.T1_wave)
        self.curve2.setData(self.T1_amp)
        self.curve22.setData(self.T1_phaseHeart)
        # print(self.ACTION_TYPE_DISPLAY)
        # if self.TNUM >= 1:
        #     pass

        if self.ACTION_TYPE_DISPLAY == SystemConstants.NO_PEOPLE:
            self.label_T2_4.setText("无人.")
        if self.ACTION_TYPE_DISPLAY == SystemConstants.WALKING:
            self.label_T2_4.setText("走动.")
        if self.ACTION_TYPE_DISPLAY == SystemConstants.STANDING:
            self.label_T2_4.setText("站立.")
        if self.ACTION_TYPE_DISPLAY == SystemConstants.SIT_DOWN:
            self.label_T2_4.setText("坐下.")
        if self.ACTION_TYPE_DISPLAY == SystemConstants.FALL_DOWN:
            self.label_T2_4.setText("跌倒！")
        if self.ACTION_TYPE_DISPLAY == SystemConstants.LIE_DOWN:
            self.label_T2_4.setText("躺下.")

        if self.ACTION_TYPE_DISPLAY2 == SystemConstants.NO_PEOPLE:
            self.label_T2_5.setText("无人.")
        if self.ACTION_TYPE_DISPLAY2 == SystemConstants.WALKING:
            self.label_T2_5.setText("走动.")
        if self.ACTION_TYPE_DISPLAY2 == SystemConstants.STANDING:
            self.label_T2_5.setText("站立.")
        if self.ACTION_TYPE_DISPLAY2 == SystemConstants.SIT_DOWN:
            self.label_T2_5.setText("坐下.")
        if self.ACTION_TYPE_DISPLAY2 == SystemConstants.FALL_DOWN:
            self.label_T2_5.setText("跌倒！")
        if self.ACTION_TYPE_DISPLAY2 == SystemConstants.LIE_DOWN:
            self.label_T2_5.setText("躺下.")

        data = []
        data_val = 0

        # self.ST_x = np.zeros(512)
        # self.ST_y = np.zeros(512)

        for i in range(512):
            if self.pos[i, 0] > 0:
                data.append(QScatterDataItem(QVector3D(self.pos[i, 1], self.pos[i, 2], self.pos[i, 0])))

        # for i in range(512):
        #     if self.pos[i, 0] > 0:
        #         data.append(QScatterDataItem(QVector3D(self.pos[i, 1], -1.5, self.pos[i, 0])))

        self.series.dataProxy().resetArray(data)

    def open_network_card(self):
        # 启动接收线程
        wired_receive_thread = threading.Thread(target=self.wired_receive_thread)
        wired_receive_thread.setDaemon(True)
        wired_receive_thread.start()
        logger.info("接收有线数据线程启动！")
        self.btn1.setEnabled(False)

    def open_wifi_receive(self):
        # 启动接收线程
        socket_dict = {}
        for device_value in SystemMemory.get_value("device_list"):
            mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            ip_value = device_value.split(",")[1]
            radar_device_udp_address = (ip_value, 80)
            # 绑定本地端口 避免重启问题
            local_ip = FindDevice(self).get_local_ip()
            client_udp_address = (local_ip, SystemConstants.SERVER_ADDRESS_LOCALHOST_PORT + int(ip_value.split(".")[3]))
            logger.info("绑定udp客户端 ： {}", client_udp_address)
            mySocket.bind(client_udp_address)
            # 需要发送出发数据
            mySocket.sendto(SystemConstants.WIFI_START_SEND_CONTENT.encode(), radar_device_udp_address)
            socket_dict[radar_device_udp_address] = mySocket
            logger.info("发送触发数据：{}", radar_device_udp_address)
            if SystemConstants.WIFI_ADDRESS_TYPE[ip_value] == SystemConstants.LOCATION_RADAR_TYPE:
                wifi_receive_thread = threading.Thread(
                    target=DealPackage(self, mySocket, ip_value).deal_location_wifi_package)
                wifi_receive_thread.setDaemon(True)
                wifi_receive_thread.start()
                logger.info("接收wifi位置数据线程启动！对应设备{}", ip_value)
            elif SystemConstants.WIFI_ADDRESS_TYPE[ip_value] == SystemConstants.PARAMETER_RADAR_TYPE:
                wifi_receive_thread = threading.Thread(
                    target=DealPackage(self, mySocket, ip_value).deal_parameter_wifi_package)
                wifi_receive_thread.setDaemon(True)
                wifi_receive_thread.start()
                logger.info("接收wifi心率呼吸数据线程启动！对应设备{}", ip_value)
            elif SystemConstants.WIFI_ADDRESS_TYPE[ip_value] == SystemConstants.POSTURE_RADAR_TYPE:
                wifi_receive_thread = threading.Thread(
                    target=DealPackage(self, mySocket, ip_value).deal_posture_wifi_package)
                wifi_receive_thread.setDaemon(True)
                wifi_receive_thread.start()
                logger.info("接收wifi姿态数据线程启动！对应设备{}", ip_value)
        SystemMemory.set_value("socket_dict", socket_dict)
        self.btn_open_wifi.setEnabled(False)

    # 保存发送服务信息
    def save_server_information(self):
        SystemMemory.set_value(SystemConstants.IP_NAME, self.lineEdit_IP.text())
        SystemMemory.set_value(SystemConstants.PORT_NAME, int(self.lineEdit_port.text()))
        SystemMemory.set_value(SystemConstants.SPAN_NAME, int(self.lineEdit_span_millisecond.text()))
        self.add_content_to_text_edit_logging("保存服务端信息成功！")
        logger.info("保存服务端信息成功！")

    def add_content_to_text_edit_logging(self, add_text):
        if len(self.plainTextEdit_send.toPlainText()) > 3000:
            self.plainTextEdit_send.setPlainText("")
        self.plainTextEdit_send.setPlainText(self.plainTextEdit_send.toPlainText() +
                                             datetime.now().strftime('%Y-%m-%d %H:%M:%S') + add_text + "\n")
        self.plainTextEdit_send.moveCursor(qg.QTextCursor.End)

    def set_socket_logger(self):
        if SystemMemory.get_value("logging"):
            self.add_content_to_text_edit_logging(SystemMemory.get_value("logging"))

    def clear_log_text(self):
        self.plainTextEdit_send.setPlainText("")

    def start_send_thread(self):
        # 启动 发送到socket 线程
        socket_client_thread = threading.Thread(target=SocketClient.send_breathe_heart_content)
        socket_client_thread.setDaemon(True)
        socket_client_thread.start()
        logger.info("发送心率呼吸数据线程启动！")

        # socket_client_thread = threading.Thread(target=SocketClient.send_location_content)
        # socket_client_thread.setDaemon(True)
        # socket_client_thread.start()
        # logger.info("发送位置数据线程启动！")
        # self.btn_start_send.setEnabled(False)

    def closeEvent(self, event):
        socket_dict = SystemMemory.get_value("socket_dict")
        if socket_dict:
            for cur_udp_address, mySocket in socket_dict.items():
                # 发送结束信号
                mySocket.sendto(SystemConstants.WIFI_END_SEND_CONTENT.encode(), cur_udp_address)
                mySocket.close()
                logger.info("关闭wifi socket 连接! {}", cur_udp_address)
        logger.info("退出程序!")
        try:
            sys.exit(1)
        except:
            os._exit(1)
        finally:
            os._exit(1)
