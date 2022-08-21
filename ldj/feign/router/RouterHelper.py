#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author: dejian.liu
# @date:  2022-08-19 22:33
from ldj.config import settings
from ldj.feign.enums.RouterType import RouterType
from ldj.feign.exception.BusinessException import BusinessException
from ldj.feign.model.HostInfo import HostInfo
from ldj.feign.model.ServiceInfo import ServiceInfo
from ldj.feign.router.Router import Router


class RouterHelper:
    @staticmethod
    def get_host_url(protocol: str, serviceInfo: ServiceInfo) -> str:
        router = RouterType.parse(settings.ROUTER_TYPE)
        if len(router.__bases__) > 0 and router.__bases__[0].__name__ == Router.__name__:
            host = router._select_host(serviceInfo)
            if host is not None:
                if not host.enabled:
                    raise BusinessException("该服务{}:{}已被禁用".format(host.ip, host.port))
                if not host.healthy:
                    raise BusinessException("该服务{}:{}当时处于不可用户状态".format(host.ip, host.port))
                return RouterHelper.__get_host_url(host, protocol)

        return ""

    @staticmethod
    def __get_host_url(hostInfo: HostInfo, prefix: str):
        return "{prefix}://{ip}:{port}".format(prefix=prefix, ip=hostInfo.ip, port=hostInfo.port)
