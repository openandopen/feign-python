#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-19 14:59
# 默认实现
from ldj.feign.model.HostInfo import HostInfo
from ldj.feign.model.ServiceInfo import ServiceInfo
from ldj.feign.router.Router import Router
from ldj.feign.utils.IpUtil import IpUtil

CURRENT_IP_LONG = IpUtil.ip_to_long(IpUtil.get_ip_v4())


# 本地IP Hash
class HashRouter(Router):

    #  默认选中第一条记录
    @staticmethod
    def _select_host(serviceInfo: ServiceInfo) -> HostInfo:
        if serviceInfo is None:
            return None
        hosts = serviceInfo.hosts
        count = len(hosts)
        if count > 0:
            return hosts[CURRENT_IP_LONG % count]
        return None
