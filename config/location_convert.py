import math

from config.global_config import global_config

# 安装高度H、倾斜角a
H = 2.1
a = 37


class LocationConvert:
    @staticmethod
    def convert_location_list(location_list):
        new_location_list = []
        # 坐标变换
        seta_x = -0.05  # x误差
        seta_y = 0.05  # y误差
        x_dis = 4.2  # 两个坐标原点的距离
        y_dis = 3.3
        x_pre = round(location_list[0], 6)
        y_pre = round(location_list[1], 6)
        dis_e = math.radians(global_config.radarLAngle)  # 雷达安装的偏转角
        beta = math.atan2(x_pre, y_pre)  # 原坐标下的投影角
        alpha = beta - dis_e  # 转换后的投影角
        r = math.sqrt(math.pow(x_pre, 2) + math.pow(y_pre, 2))
        y_new = r * math.cos(alpha) - y_dis + seta_y  # 转换后坐标
        x_new = -r * math.sin(alpha) + x_dis + seta_x

        return_x = x_new * 4.6 / 4.2
        return_y = y_new * 4.6 / 3.3
        if return_x > 6:
            return_x = 5.7
        if return_x < -6:
            return_x = -5.7
        if return_y > 5:
            return_y = 4.7
        new_location_list.append(return_x)
        new_location_list.append(return_y)
        return new_location_list

    @staticmethod
    def convert_xyz_location_list(location_list, alpha_E, distance):
        new_location_list = []
        # 坐标变换
        seta_x = -0.05  # x误差
        seta_y = 0.05  # y误差
        x_dis = 6.6  # 两个坐标原点的距离
        y_dis = 3.5
        x_pre = round(location_list[0], 6)
        y_pre = round(location_list[1], 6)
        z_pre = round(location_list[2], 6)
        dis_e = math.radians(22)  # 雷达安装的偏转角
        beta = math.atan2(x_pre, y_pre)  # 原坐标下的投影角
        alpha = beta - dis_e  # 转换后的投影角
        r = math.sqrt(math.pow(x_pre, 2) + math.pow(y_pre, 2))
        # 转换后坐标
        y_new = r * math.cos(alpha) - y_dis + seta_y
        x_new = -r * math.sin(alpha) + x_dis + seta_x

        # # r
        # r_dis = math.sqrt(math.pow(x_new, 2) + math.pow(y_new, 2))
        #
        # if z_pre > 0:
        #     z_new = 2.5 - r_dis * math.tan(dis_e) + z_pre / math.cos(dis_e)
        # else:
        #     z_new = 2.5 - r_dis * math.tan(dis_e) - z_pre / math.cos(dis_e)

        beta1 = 90 - a - alpha_E
        # print("beat1 :", beta1)
        z_new = H - abs(distance * math.cos(math.radians(beta1)))

        new_location_list = [x_new, y_new, z_new, distance, alpha_E]
        return new_location_list
