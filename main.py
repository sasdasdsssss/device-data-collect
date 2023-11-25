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

if __name__ == '__main__':
    # 初始化缓存
    SystemMemory.initialize()

    app = QtWidgets.QApplication(sys.argv)
    myWin = MyGraphWindow()

    # 启动设备发现线程
    find_device_thread = threading.Thread(target=FindDevice(myWin).run_find_device)
    find_device_thread.setDaemon(True)
    find_device_thread.start()
    logger.info("设备发现线程启动！")

    timer_draw_line = QtCore.QTimer()
    timer_draw_line.timeout.connect(myWin.picture_draw_timer)
    timer_draw_line.start(50)

    time.sleep(1)

    timer_set_logging = QtCore.QTimer()
    timer_set_logging.timeout.connect(myWin.set_socket_logger)
    timer_set_logging.start(1000)

    # myWin.setStyleSheet("background-color: rgb(181, 181, 181)")

    myWin.show()
    sys.exit(app.exec())
