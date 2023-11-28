# -*- coding: utf-8 -*-
# python 3.x
# Filename:const.py
# 定义一个常量类实现常量的功能
#
# 该类定义了一个方法__setattr()__,和一个异常ConstError, ConstError类继承
# 自类TypeError. 通过调用类自带的字典__dict__, 判断定义的常量是否包含在字典
# 中。如果字典中包含此变量，将抛出异常，否则，给新创建的常量赋值。
# 最后两行代码的作用是把const类注册到sys.modules这个全局字典中。
class SystemConstants:
    def __init__(self):
        pass

    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const (%s)" % name)
        self.__dict__[name] = value


SystemConstants.PASS_RESULT = "Pass"
SystemConstants.FAIL_RESULT = "Fail"
SystemConstants.BREATHE_DATA_VALUE = "breath_value"
SystemConstants.HEART_DATA_VALUE = "heart_value"
SystemConstants.RADAR_BREATH_DATA_TYPE = "radar_breath_data"
SystemConstants.RADAR_HEART_DATA_TYPE = "radar_heart_data"
SystemConstants.RADAR_LOCATION_DATA_TYPE = "location_data"
SystemConstants.IP_NAME = "ip"
SystemConstants.PORT_NAME = "port"
SystemConstants.SPAN_NAME = "span"
SystemConstants.ENCODE_TYPE = "'utf-8'"
# 无人
SystemConstants.NO_PEOPLE = 0
# 行动
SystemConstants.WALKING = 1
# 站立
SystemConstants.STANDING = 2
# 坐下
SystemConstants.SIT_DOWN = 3
# 跌倒
SystemConstants.FALL_DOWN = 4
# 躺下
SystemConstants.LIE_DOWN = 5
# 配置wifi 对应ip地址类型
SystemConstants.WIFI_ADDRESS_TYPE = {"192.168.101.39": 2, "192.168.101.42": 2, "192.168.101.43": 2}
# udp 发送触发信息
SystemConstants.WIFI_START_SEND_CONTENT = "hello"
# udp 发送结束信息
SystemConstants.WIFI_END_SEND_CONTENT = "exit"
# 位置类型
SystemConstants.LOCATION_RADAR_TYPE = 2
# 心率呼吸类型
SystemConstants.PARAMETER_RADAR_TYPE = 1
# 配置本地udp端口地址
SystemConstants.SERVER_ADDRESS_LOCALHOST_PORT = 13010
# 有线网络类型
SystemConstants.WIRED_NETWORK_TYPE = 1
# 无线网络类型
SystemConstants.WIFI_NETWORK_TYPE = 2

# 门位置的坐标X
SystemConstants.DOOR_LOCATION_X = 7.2

# 门位置的坐标Y
SystemConstants.DOOR_LOCATION_Y = -1.5
