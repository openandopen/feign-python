#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-19 14:38
from toolbox import ObjectDict

from ldj.center.nacos.NacosClient import NacosClient
from ldj.feign.center.RegisterCenter import RegisterCenter
from ldj.feign.model.HostInfo import HostInfo
from ldj.feign.model.ServiceInfo import ServiceInfo


# nacos注册中心-实现
class NacosCenter(RegisterCenter):

    # 后期远程服务
    @staticmethod
    def _obtain_service(serviceId: str, groupName: str) -> ServiceInfo:
        service_info = ServiceInfo()
        service_data = NacosClient.get_client().list_naming_instance(serviceId, group_name=groupName)
        result = ObjectDict(service_data)
        service_info.name = result.name
        service_info.groupName = result.groupName
        service_info.lastRefTime = result.lastRefTime
        host_list = list[HostInfo]()
        for res in result.hosts:
            host = HostInfo()
            host.ip = res["ip"]
            host.port = int(res["port"])
            host.weight = int(res["weight"])
            host.healthy = res["healthy"]
            host.enabled = bool(res["enabled"])
            host.meta = res["metadata"]
            host_list.append(host)
        service_info.hosts = host_list
        return service_info;