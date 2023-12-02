import math


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
        dis_e = math.radians(24)  # 雷达安装的偏转角
        beta = math.atan2(x_pre, y_pre)  # 原坐标下的投影角
        alpha = beta - dis_e  # 转换后的投影角
        r = math.sqrt(math.pow(x_pre, 2) + math.pow(y_pre, 2))
        y_new = r * math.cos(alpha) - y_dis + seta_y  # 转换后坐标
        x_new = -r * math.sin(alpha) + x_dis + seta_x

        return_x = x_new * 4.6 / 4.2
        return_y = y_new * 4.6 / 3.3
        if return_x > 5:
            return_x = 4.7
        if return_x < -5:
            return_x = -4.7
        if return_y > 5:
            return_y = 4.7
        new_location_list.append(return_x)
        new_location_list.append(return_y)
        return new_location_list
