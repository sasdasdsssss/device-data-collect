import sys
import threading
import time

from PySide6 import QtWidgets

from loguru import logger

from client.socket_client import SocketClient
from my_graph_window import MyGraphWindow
from PySide6 import QtCore
from config import system_memory as SystemMemory

if __name__ == '__main__':
    # 初始化缓存
    SystemMemory.initialize()

    app = QtWidgets.QApplication(sys.argv)
    myWin = MyGraphWindow()

    timer_draw_line = QtCore.QTimer()
    timer_draw_line.timeout.connect(myWin.picture_draw_timer)
    timer_draw_line.start(50)

    timer_set_logging = QtCore.QTimer()
    timer_set_logging.timeout.connect(myWin.set_socket_logger)
    timer_set_logging.start(1000)

    time.sleep(1)

    # 启动接收线程
    frame_receive_thread = threading.Thread(target=myWin.frame_receive_thread)
    frame_receive_thread.setDaemon(True)
    frame_receive_thread.start()
    logger.info("接收数据线程启动！")

    # 启动 发送到socket 线程
    socket_client_thread = threading.Thread(target=SocketClient.send_content)
    socket_client_thread.setDaemon(True)
    socket_client_thread.start()
    logger.info("发送数据线程启动！")

    # myWin.setStyleSheet("background-color: rgb(181, 181, 181)")
    myWin.show()
    sys.exit(app.exec())
