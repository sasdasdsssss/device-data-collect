import socket
import time
import random
from datetime import datetime

from config import system_memory as SystemMemory
from config.global_config import global_config
from config.system_constant import SystemConstants

from config.location_convert import LocationConvert

from loguru import logger


class SocketClient:
    def __init__(self, myWin):
        self.myWin = myWin

    def send_radar_content(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip = SystemMemory.get_value(SystemConstants.IP_NAME)
        port = SystemMemory.get_value(SystemConstants.PORT_NAME)
        while True:
            breath_data = SystemMemory.get_value(SystemConstants.BREATHE_DATA_VALUE)
            heart_rate_data = SystemMemory.get_value(SystemConstants.HEART_DATA_VALUE)
            # 发送呼吸数据
            if breath_data:
                if 10 <= int(breath_data) <= 30:
                    send_breath_data = {"type": SystemConstants.RADAR_BREATH_DATA_TYPE,
                                        "data": breath_data}
                    send_breath_msg = str(send_breath_data).encode(SystemConstants.ENCODE_TYPE)
                    sock.sendto(send_breath_msg, (ip, port))
                    logger.info("发送呼吸数据成功：{}", str(send_breath_data))
            # 发送心率数据
            if heart_rate_data:
                if 65 <= int(heart_rate_data) <= 85:
                    send_heart_data = {"type": SystemConstants.RADAR_HEART_DATA_TYPE,
                                       "data": heart_rate_data}
                    send_heart_msg = str(send_heart_data).encode(SystemConstants.ENCODE_TYPE)
                    sock.sendto(send_heart_msg, (ip, port))
                    logger.info("发送心率数据成功：{}", str(send_heart_data))

            person_pos_dict = SystemMemory.get_value("person_pos_dict")
            if person_pos_dict and len(person_pos_dict) > 0:
                petient_posture_list = []
                posture_device_ip_list = []
                for ip_value, wifi_device_type in global_config.wifiAddressType.items():
                    if wifi_device_type == global_config.postureRadarType:
                        posture_device_ip_list.append(ip_value)
                for ip_value in posture_device_ip_list:
                    petient_posture = SystemMemory.get_value("petient_posture" + ip_value)
                    if petient_posture:
                        petient_posture_list.append(petient_posture)
                    else:
                        petient_posture_list.append(0)
                personLocation = []
                for person_index, person_location in person_pos_dict.items():
                    single_person_location = [person_location[0], person_location[1]]
                    personLocation.append(LocationConvert.convert_location_list(single_person_location))
                send_location_data = {"type": SystemConstants.RADAR_LOCATION_DATA_TYPE,
                                      "patientPosture": petient_posture_list,
                                      "roomPersonNumber": len(person_pos_dict),
                                      "personLocation": personLocation
                                      }
                send_location_msg = str(send_location_data).encode(SystemConstants.ENCODE_TYPE)
                sock.sendto(send_location_msg, (ip, port))
                logger.info("发送位置数据成功：{}", str(send_location_data))
            time.sleep(SystemMemory.get_value(SystemConstants.SPAN_NAME) / 1000)
