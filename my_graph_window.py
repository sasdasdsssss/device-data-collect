import sys
import numpy as np
from PySide6 import QtWidgets
import pyqtgraph as pg

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

import os  # 用于处理文件

from PySide6.QtGui import QVector3D, QLinearGradient
from PySide6.QtDataVisualization import QAbstract3DSeries, Q3DScatter, QScatter3DSeries, \
    QScatterDataItem, Q3DCamera, QScatterDataProxy, Q3DTheme
from PySide6.QtWidgets import QWidget

from process.deal_package import DealPackage

from config import system_memory as SystemMemory
from config import system_constant as SystemConstants


# 界面类
class MyGraphWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MyGraphWindow, self).__init__()
        self.setupUi(self)  # 初始化窗口
        self.p1, self.p11, self.p2, self.p22, self.curve1, self.curve11, \
            self.curve2, self.curve22, self.pos, self.series = self.set_graph_ui()  # 设置绘图窗口
        self.T1_phaseBreath, self.T1_phaseHeart, self.T1_amp, self.T1_wave, \
            self.ST_x, self.ST_y, self.TNUM, self.GES_x, self.GES_y, \
            self.ACTION_TYPE_DISPLAY = self.init_data()
        self.btn1.clicked.connect(self.data_open)  # 打开网卡
        self.btn2.clicked.connect(self.serial_open)  # 打开串口
        self.btn3.clicked.connect(self.serial_send)  # 打开串口
        self.btn4.clicked.connect(self.serial_read)  # 打开串口
        self.btn_save_server.clicked.connect(self.save_server_information)  # 打开串口

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
        return T1_phaseBreath, T1_phaseHeart, T1_amp, T1_wave, ST_x, ST_y, TNUM, GES_x, GES_y, ACTION_TYPE_DISPLAY

    def set_graph_ui(self):
        pg.setConfigOptions(antialias=True)  # pg全局变量设置函数，antialias=True开启曲线抗锯齿

        pos = np.zeros((1024, 3))

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
        SystemMemory.set_value("ip", self.lineEdit_IP.text())
        SystemMemory.set_value("port", int(self.lineEdit_port.text()))
        SystemMemory.set_value("span", int(self.lineEdit_span_millisecond.text()))

        ports_list = list(serial.tools.list_ports.comports())
        # ports_list_value = list()
        for comport in ports_list:
            self.comboBox_2.addItem(comport.name)
        self.comboBox_2.setCurrentIndex(0)

        self.label_T1_2.setText("呼吸频率：")
        self.label_T2_2.setText("心率：")

        Q3D = Q3DScatter()
        container = QWidget.createWindowContainer(Q3D)
        self.graph8.addWidget(container, True)

        series = QScatter3DSeries()
        series.setMeshSmooth(1)
        Q3D.addSeries(series)
        Q3D.axisX().setTitle("X")
        Q3D.axisX().setTitleVisible(True)
        Q3D.axisX().setRange(-5, 5)
        Q3D.axisY().setTitle("Y")
        Q3D.axisY().setTitleVisible(True)
        Q3D.axisY().setRange(-1.5, 1.5)
        Q3D.axisZ().setTitle("Z")
        Q3D.axisZ().setTitleVisible(True)
        Q3D.axisZ().setRange(0, 6)
        Q3D.activeTheme().setLabelBackgroundEnabled(False)
        Q3D.activeTheme().setBackgroundColor(qg.QColor(0, 0, 0))

        series.setMesh(QAbstract3DSeries.MeshPoint)
        series.setSingleHighlightColor(qg.QColor(0, 0, 90))
        series.setBaseColor(qg.QColor(0, 255, 255))
        series.setItemSize(0.4)

        Qline = QLinearGradient()
        Qline.setColorAt(0.0, qg.QColor(70, 70, 70))
        Qline.setColorAt(0.5, qg.QColor(255, 0, 0))
        Qline.setColorAt(1.0, qg.QColor(0, 255, 0))
        series.setBaseGradient(Qline)
        series.setColorStyle(Q3DTheme.ColorStyleRangeGradient)

        camera = Q3D.scene().activeCamera()
        camera.setCameraPreset(Q3DCamera.CameraPresetFront)

        return p1, p11, p2, p22, curve1, curve11, curve2, curve22, pos, series,

    def frame_receive_thread(self):
        net_card = self.comboBox.currentText()
        dealPackage = DealPackage(self)
        WinPcapUtils.capture_on(pattern=net_card, callback=dealPackage.packet_callback)

    def picture_draw_timer(self):
        self.curve1.setData(self.T1_phaseBreath)
        self.curve11.setData(self.T1_wave)
        self.curve2.setData(self.T1_amp)
        self.curve22.setData(self.T1_phaseHeart)

        data = []

        for i in range(512):
            if self.pos[i, 0] > 0:
                data.append(QScatterDataItem(QVector3D(self.pos[i, 1], self.pos[i, 2], self.pos[i, 0])))

        for i in range(512):
            if self.pos[i, 0] > 0:
                data.append(QScatterDataItem(QVector3D(self.pos[i, 1], -1.5, self.pos[i, 0])))

        # self.series.dataProxy().resetArray(data)

    def data_open(self):
        frame_receive_thread = threading.Thread(target=self.frame_receive_thread)
        frame_receive_thread.start()

    def serial_open(self):
        global ser
        btn_text = self.btn2.text()
        if btn_text == "打开串口":
            ser_choose = self.comboBox_2.currentText()
            ser = serial.Serial(ser_choose, 115200)  # 打开COM17，将波特率配置为115200，其余参数使用默认值
            if ser.isOpen():  # 判断串口是否成功打开
                self.btn2.setText("关闭串口")
                logger.info("打开串口成功。")
            else:
                logger.info("打开串口失败。")

        elif btn_text == "关闭串口":
            self.btn2.setText("打开串口")
            ser.close()
            logger.info("已关闭串口。")

    @staticmethod
    def serial_send():
        if ser.isOpen():  # 判断串口是否成功打开
            while True:
                com_input = ser.read(10)
                if com_input:  # 如果读取结果非空，则输出
                    print(com_input)
            write_len = ser.write("ABCDEFG".encode('utf-8'))
            logger.info("串口发出{}个字节。".format(write_len))
        else:
            logger.info("未打开串口。")

    def serial_read(self):
        x1 = float(self.lineEdit.text())
        y1 = float(self.lineEdit_2.text())
        x2 = float(self.lineEdit_3.text())
        y2 = float(self.lineEdit_4.text())
        doorX = float(self.lineEdit_5.text())
        doorY = float(self.lineEdit_6.text())
        height = float(self.lineEdit_7.text())
        ele = float(self.lineEdit_8.text())
        logger.info("已读取")

    # 保存发送服务信息
    def save_server_information(self):
        SystemMemory.set_value("ip", self.lineEdit_IP.text())
        SystemMemory.set_value("port", int(self.lineEdit_port.text()))
        SystemMemory.set_value("span", int(self.lineEdit_span_millisecond.text()))
        logger.info("保存服务端信息成功！")

    def closeEvent(self, event):
        logger.info("退出程序!")
        try:
            sys.exit(1)
        except:
            os._exit(1)
        finally:
            os._exit(1)
