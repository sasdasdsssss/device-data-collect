import socket
import time

from config import system_memory as SystemMemory
from config.system_constant import SystemConstants

from loguru import logger


class SocketClient:
    def __int__(self):
        pass

    @staticmethod
    def send_content():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            while True:
                send_breath_data = {"type": SystemConstants.RADAR_BREATH_DATA_TYPE,
                                    "data": SystemMemory.get_value(SystemConstants.BREATHE_DATA_VALUE)}
                send_heart_data = {"type": SystemConstants.RADAR_HEART_DATA_TYPE,
                                   "data": SystemMemory.get_value(SystemConstants.HEART_DATA_VALUE)}
                send_breath_msg = str(send_breath_data).encode(SystemConstants.ENCODE_TYPE)
                send_heart_msg = str(send_heart_data).encode(SystemConstants.ENCODE_TYPE)
                sock.sendto(send_breath_msg, (
                    SystemMemory.get_value(SystemConstants.IP_NAME), SystemMemory.get_value(SystemConstants.PORT_NAME)))
                sock.sendto(send_heart_msg, (
                    SystemMemory.get_value(SystemConstants.IP_NAME), SystemMemory.get_value(SystemConstants.PORT_NAME)))
                # logger.info("发送成功，间隔时间： {}", SystemMemory.get_value("span"))
                time.sleep(SystemMemory.get_value(SystemConstants.SPAN_NAME) / 1000)
        finally:
            sock.close()
