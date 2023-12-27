# *coding:utf-8 *
import yaml


# 需要定义全局变量的放在这里，最好定义一个初始值
class GlobalConfig:
    def __init__(self):
        self.version = '1.0'
        # 读取配置文件
        with open("global_config.yml", 'r', encoding='utf-8') as ymlfile:
            config_data = yaml.load(ymlfile, Loader=yaml.FullLoader)
            # 获取版本号
            self.version = config_data["other"]["version"]
            # 本地绑定端口
            self.serverAddressLocalhostPort = config_data["other"]["serverAddressLocalhostPort"]
            # 门横坐标
            self.doorLocationX = config_data["other"]["doorLocationX"]
            # 门纵坐标
            self.doorLocationY = config_data["other"]["doorLocationY"]
            # wifi地址和设备类型
            self.wifiAddressType = config_data["other"]["wifiAddressType"]
            # 姿态类型
            self.postureRadarType = config_data["other"]["postureRadarType"]
            # 心率呼吸类型
            self.parameterRadarType = config_data["other"]["parameterRadarType"]
            # 位置类型
            self.locationRadarType = config_data["other"]["locationRadarType"]
            # 姿态类型字典
            self.personPosture = config_data["other"]["personPosture"]
            # 位置 范围
            self.personLocationScope = config_data["other"]["personLocationScope"]
            # 人远近 判断
            self.personDistance = config_data["other"]["personDistance"]
            # 门附近坐标判断
            self.doorLocationScope = config_data["other"]["doorLocationScope"]
            # 人进入出去判断
            self.doorInOutScope = config_data["other"]["doorInOutScope"]
            # 心率呼吸 处理数量
            self.parameterDealCount = config_data["other"]["parameterDealCount"]
            # 综合探头ip对应类型
            self.circleAddressType = config_data["other"]["circleAddressType"]
            # 本地ip地址，暂时固定
            self.localAddressIp = config_data["other"]["localAddressIp"]
            # 本地综合探头雷达发送数据端口
            self.localAddressUdpPort = config_data["other"]["localAddressUdpPort"]
            # 姿态处理数量
            self.postureDealCount = config_data["other"]["postureDealCount"]


global_config = GlobalConfig()
