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
SystemConstants.LOCATION_DATA_VALUE = "location_data_value"
SystemConstants.RADAR_BREATH_DATA_TYPE = "radar_breath_data"
SystemConstants.RADAR_HEART_DATA_TYPE = "radar_heart_data"
SystemConstants.RADAR_LOCATION_DATA_TYPE = "radar_location_type_data"
SystemConstants.IP_NAME = "ip"
SystemConstants.PORT_NAME = "port"
SystemConstants.SPAN_NAME = "span"
SystemConstants.ENCODE_TYPE = "'utf-8'"

# udp 发送触发信息
SystemConstants.WIFI_START_SEND_CONTENT = "hello"
# udp 发送结束信息
SystemConstants.WIFI_END_SEND_CONTENT = "exit"

# 有线网络类型
SystemConstants.WIRED_NETWORK_TYPE = 1
# 无线网络类型
SystemConstants.WIFI_NETWORK_TYPE = 2
# 综合探头类型
SystemConstants.CIRCLE_NETWORK_TYPE = 3
