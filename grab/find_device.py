import os
import re
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

import pandas as pd

from loguru import logger


class FindDevice:
    def __int__(self):
        pass

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
        logger.info("正在扫描在线列表")
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
            logger.info("当前在线的设备：")
            logger.info(df)
            for value in df.values:
                device_list.append(value[1] + " , " + value[0])
        return device_list
