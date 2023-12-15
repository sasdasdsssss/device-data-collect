import sys
import threading
import time

from PySide6 import QtWidgets

from loguru import logger

from client.socket_client import SocketClient
from my_graph_window import MyGraphWindow
from PySide6 import QtCore
from config import system_memory as SystemMemory
from grab.find_device import FindDevice
from process.clear_data_thread import ClearDataThread

from config.global_config import global_config

if __name__ == '__main__':
    # 初始化缓存
    SystemMemory.initialize()
    logger.info("缓存初始化成功!")

    app = QtWidgets.QApplication(sys.argv)
    myWin = MyGraphWindow()

    logger.info("版本：" + str(global_config.version))
    logger.info("姿态：" + str(global_config.personPosture))

    # 启动设备发现线程
    find_device_thread = threading.Thread(target=FindDevice(myWin).run_find_device)
    find_device_thread.setDaemon(True)
    find_device_thread.start()
    logger.info("设备发现线程启动！")

    # 启动数据清除线程
    clear_person_location_thread = threading.Thread(target=ClearDataThread().clear_person_location_data)
    clear_person_location_thread.setDaemon(True)
    clear_person_location_thread.start()
    logger.info("位置数据清除线程线程启动！")

    timer_draw_line = QtCore.QTimer()
    timer_draw_line.timeout.connect(myWin.picture_draw_timer)
    timer_draw_line.start(1000)

    time.sleep(1)

    # myWin.setStyleSheet("background-color: rgb(231, 231, 231)")

    myWin.show()
    sys.exit(app.exec())
