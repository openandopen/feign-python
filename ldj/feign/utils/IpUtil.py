#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-19 15:54
import socket


class IpUtil:

    @staticmethod
    def get_ip_v4() -> str:
        return socket.gethostbyname(socket.gethostname())

    @staticmethod
    def ip_to_long(ip: str) -> int:
        ip_list = ip.split('.')
        result = 0
        for i in range(4):
            result = result + int(ip_list[i]) * 256 ** (3 - i)
        return result

    @staticmethod
    def long_to_ip(num: int) -> str:
        floor_list = []
        for i in reversed(range(4)):
            res = divmod(num, 256 ** i)
            floor_list.append(str(res[0]))
            num = res[1]
        return '.'.join(floor_list)

    @staticmethod
    def get_ip_v4s() -> list[str]:
        ips = list[str]()
        ip_list = socket.getaddrinfo(socket.gethostname(), None)
        for item in ip_list:
            if ':' not in item[4][0]:
                ips.append(item[4][0])
        return ips


