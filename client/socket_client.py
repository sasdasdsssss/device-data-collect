import socket
import time
from datetime import datetime

from config import system_memory as SystemMemory
from config.system_constant import SystemConstants

from config.location_convert import LocationConvert

from loguru import logger


class SocketClient:
    def __int__(self):
        pass

    @staticmethod
    def send_breathe_heart_content():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip = SystemMemory.get_value(SystemConstants.IP_NAME)
        port = SystemMemory.get_value(SystemConstants.PORT_NAME)
        while True:
            breath_data = SystemMemory.get_value(SystemConstants.BREATHE_DATA_VALUE)
            heart_rate_data = SystemMemory.get_value(SystemConstants.HEART_DATA_VALUE)
            logging_str = ""
            # 发送呼吸数据
            if breath_data:
                send_breath_data = {"type": SystemConstants.RADAR_BREATH_DATA_TYPE,
                                    "data": breath_data}
                send_breath_msg = str(send_breath_data).encode(SystemConstants.ENCODE_TYPE)
                sock.sendto(send_breath_msg, (ip, port))
                logging_str = "发送呼吸数据成功：" + str(send_breath_data)
            # 发送心率数据
            if heart_rate_data:
                send_heart_data = {"type": SystemConstants.RADAR_HEART_DATA_TYPE,
                                   "data": heart_rate_data}
                send_heart_msg = str(send_heart_data).encode(SystemConstants.ENCODE_TYPE)
                sock.sendto(send_heart_msg, (ip, port))
                logging_str = " 发送心率数据成功：" + str(send_heart_data)
            SystemMemory.set_value("logging", logging_str)

            person_pos_dict = SystemMemory.get_value("person_pos_dict")
            if person_pos_dict:
                petient_posture = [0, 0]
                patient_posture_1 = SystemMemory.get_value("petient_posture192.168.101.42")
                patient_posture_2 = SystemMemory.get_value("petient_posture192.168.101.43")
                if patient_posture_1:
                    petient_posture[0] = patient_posture_1
                if patient_posture_2:
                    petient_posture[1] = patient_posture_2
                personLocation = []
                for person_index, person_location in person_pos_dict.items():
                    single_person_location = [person_location[0], person_location[1]]
                    personLocation.append(LocationConvert.convert_location_list(single_person_location))
                send_location_data = {"type": SystemConstants.RADAR_LOCATION_DATA_TYPE,
                                      "patientPosture": petient_posture,
                                      "roomPersonNumber": len(person_pos_dict),
                                      "personLocation": personLocation
                                      }
                send_location_msg = str(send_location_data).encode(SystemConstants.ENCODE_TYPE)
                sock.sendto(send_location_msg, (ip, port))
                logging_str = " 发送位置数据成功：" + str(send_location_data)
                SystemMemory.set_value("logging", logging_str)
            time.sleep(SystemMemory.get_value(SystemConstants.SPAN_NAME) / 1000)

    # def send_location_content(self):
    #     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #     ip = SystemMemory.get_value(SystemConstants.IP_NAME)
    #     port = SystemMemory.get_value(SystemConstants.PORT_NAME)
    #     while True:
    #         person_pos_dict = SystemMemory.get_value("person_pos_dict")
    #         if person_pos_dict:
    #             petient_posture = [0, 0]
    #             patient_posture_1 = SystemMemory.get_value("petient_posture192.168.101.42")
    #             patient_posture_2 = SystemMemory.get_value("petient_posture192.168.101.43")
    #             if patient_posture_1 and patient_posture_2:
    #                 petient_posture = [patient_posture_1, patient_posture_2]
    #             personLocation = []
    #             for person_index, person_location in person_pos_dict.items():
    #                 single_person_location = [person_location[0], person_location[1]]
    #                 personLocation.append(LocationConvert.convert_location_list(single_person_location))
    #             send_location_data = {"type": SystemConstants.RADAR_LOCATION_DATA_TYPE,
    #                                   "patientPosture": petient_posture,
    #                                   "roomPersonNumber": len(person_pos_dict),
    #                                   "personLocation": personLocation
    #                                   }
    #             send_location_msg = str(send_location_data).encode(SystemConstants.ENCODE_TYPE)
    #             sock.sendto(send_location_msg, (ip, port))
    #             logging_str = " 发送位置数据成功：" + str(send_location_data)
    #             SystemMemory.set_value("logging", logging_str)
    #             time.sleep(10)
