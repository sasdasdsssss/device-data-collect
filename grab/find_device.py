import os
import re
import socket
import time
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

import pandas as pd

from loguru import logger

from config import system_memory as SystemMemory

from config.global_config import global_config


class FindDevice:
    def __init__(self, myWin):
        self.myWin = myWin

    @staticmethod
    def get_net_segment():
        with os.popen("arp -a") as res:
            for line in res:
                line = line.strip()
                if line.startswith("接口"):
                    net_segment = re.findall(
                        "(\d+\.\d+\.\d+)\.\d+", line)[0]
                    break
        return net_segment

    @staticmethod
    def ping_net_segment_all(net_segment):
        with ThreadPoolExecutor(max_workers=4) as executor:
            for i in range(1, 255):
                executor.submit(os.popen, f"ping -w 1 -n 1 {net_segment}.{i}")

    @staticmethod
    def get_local_ip():
        # 获取主机名
        hostname = socket.gethostname()

        # 获取IP地址列表
        ip_list = socket.getaddrinfo(hostname, None, socket.AF_INET, socket.SOCK_STREAM)

        # 遍历IP地址列表，找到IPv4地址
        for item in ip_list:
            if item[0] == socket.AF_INET:
                if item[4][0].startswith(global_config.addressPrex):
                    ip_address = item[4][0]
                    break
        return ip_address

    @staticmethod
    def get_arp_ip_mac():
        header = None
        with os.popen("arp -a") as res:
            for line in res:
                line = line.strip()
                if not line or line.startswith("接口"):
                    continue
                if header is None:
                    header = re.split(" {2,}", line.strip())
                    break
            df = pd.read_csv(res, sep=" {2,}",
                             names=header, header=0, engine='python')
        return df

    @staticmethod
    def ping_ip_list(ips, max_workers=4):
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_tasks = []
            for ip in ips:
                future_tasks.append(executor.submit(os.popen, f"ping -w 1 -n 1 {ip}"))
            wait(future_tasks, return_when=ALL_COMPLETED)

    def run_find_device(self):
        # 是否进行初始扫描
        init_search = False
        if init_search:
            logger.info("正在扫描当前网段所有ip....")
            self.ping_net_segment_all(self.get_net_segment())

        device_list = []

        last = None
        df = self.get_arp_ip_mac()
        df = df.loc[df.类型 == "动态", ["Internet 地址", "物理地址"]]
        if last is None:
            for value in df.values:
                if value[0][-2:] != ".1" and value[0][0:9] == global_config.addressPrex:
                    device_list.append(value[1] + "," + value[0])
        SystemMemory.set_value("device_list", device_list)
        self.myWin.init_wifi_device_list(device_list)
        while True:
            df = self.get_arp_ip_mac()
            df = df.loc[df.类型 == "动态", ["Internet 地址", "物理地址"]]
            if last is None:
                pass
            else:
                online = df.loc[~df.物理地址.isin(last.物理地址)]
                offline = last[~last.物理地址.isin(df.物理地址)]
                if online.shape[0] > 0:
                    device_ip_list_old = SystemMemory.get_value("device_list")
                    for value in online.values:
                        if value[0][-2:] != ".1" and value[0][0:11] == global_config.addressPrex:
                            device_str = value[1] + "," + value[0]
                            device_ip_list_old.append(device_str)
                            logger.info("上线设备：{}", device_str)
                    SystemMemory.set_value("device_list", device_ip_list_old)
                    self.myWin.init_wifi_device_list(device_ip_list_old)
                if offline.shape[0] > 0:
                    device_ip_list_old = SystemMemory.get_value("device_list")
                    for value in offline.values:
                        device_str = value[1] + "," + value[0]
                        if device_str in device_ip_list_old:
                            device_ip_list_old.remove(device_str)
                            logger.info("下线设备：{}", device_str)
                    SystemMemory.set_value("device_list", device_ip_list_old)
                    self.myWin.init_wifi_device_list(device_ip_list_old)
            self.ping_ip_list(df["Internet 地址"].values)
            last = df
            time.sleep(15)
