import socket
import time
from datetime import datetime

from config import system_memory as SystemMemory
from config.system_constant import SystemConstants

from config.location_convert import LocationConvert

from loguru import logger


class ClearDataThread:
    def __int__(self):
        pass

    @staticmethod
    def clear_person_location_data():
        while True:
            SystemMemory.set_value("person_pos_dict", {})
            SystemMemory.set_value("logging", "")
            time.sleep(60)
