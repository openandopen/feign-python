#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述: 轮询
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-19 16:17
from ldj.feign.model.HostInfo import HostInfo
from ldj.feign.model.ServiceInfo import ServiceInfo
from ldj.feign.router.Router import Router


# 轮询
class RoundRobinRouter(Router):
    counter = 0

    @staticmethod
    def _select_host(serviceInfo: ServiceInfo) -> HostInfo:
        hosts = serviceInfo.hosts
        count = len(hosts)
        RoundRobinRouter.counter += 1
        if RoundRobinRouter.counter > 100000:
            RoundRobinRouter.counter = 0
        if count > 0:
            return hosts[RoundRobinRouter.counter % count]
        return None
        pass
