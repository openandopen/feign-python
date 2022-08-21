#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述: 随机
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-19 16:17
from ldj.feign.model.HostInfo import HostInfo
from ldj.feign.model.ServiceInfo import ServiceInfo
from ldj.feign.router.Router import Router
import random


# 轮询
class RandomRouter(Router):

    @staticmethod
    def _select_host(serviceInfo: ServiceInfo) -> HostInfo:
        hosts = serviceInfo.hosts
        count = len(hosts)
        if count > 0:
            return hosts[random.randint(1, 100) % count]
        return None
        pass
