import socket
import time

from config import system_memory as SystemMemory
from config import system_constant as SystemConstants

from loguru import logger


class SocketClient:
    def __int__(self):
        pass

    @staticmethod
    def send_content():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            while True:
                send_breath_data = {"type": "radar_breath_data",
                                    "data": SystemMemory.get_value("breathe_value")}
                send_heart_data = {"type": "radar_heart_data",
                                   "data": SystemMemory.get_value("heart_value")}
                send_breath_msg = str(send_breath_data).encode('utf-8')
                send_heart_msg = str(send_heart_data).encode('utf-8')
                sock.sendto(send_breath_msg, (SystemMemory.get_value("ip"), SystemMemory.get_value("port")))
                sock.sendto(send_heart_msg, (SystemMemory.get_value("ip"), SystemMemory.get_value("port")))
                # logger.info("发送成功，间隔时间： {}", SystemMemory.get_value("span"))
                time.sleep(SystemMemory.get_value("span") / 1000)
        finally:
            sock.close()
