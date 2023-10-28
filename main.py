import sys
import numpy as np
from PySide6 import QtWidgets
import pyqtgraph as pg

from my_graph_window import MyGraphWindow
from ui.ui_main_window import Ui_MainWindow
from winpcapy import WinPcapDevices
from winpcapy import WinPcapUtils
import struct
import time
import threading
import serial
import serial.tools.list_ports
from PySide6 import QtCore
import PySide6.QtGui as qg

from loguru import logger

from config import system_memory as SystemMemory

import os  # 用于处理文件

from PySide6.QtGui import QVector3D, QLinearGradient
from PySide6.QtDataVisualization import *  # QAbstract3DSeries,Q3DScatter, QScatter3DSeries, QScatterDataItem,
# Q3DCamera,QScatterDataProxy
from PySide6.QtWidgets import QWidget



if __name__ == '__main__':
    # if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    #     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    # if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    #     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    # 初始化缓存
    SystemMemory.initialize()

    app = QtWidgets.QApplication(sys.argv)
    myWin = MyGraphWindow()

    t3 = QtCore.QTimer()
    t3.timeout.connect(myWin.PictureDrawTimer)
    t3.start(50)

    # myWin.setStyleSheet("background-color: rgb(181, 181, 181)")
    myWin.show()
    sys.exit(app.exec())
