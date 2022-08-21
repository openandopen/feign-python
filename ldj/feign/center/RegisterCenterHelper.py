#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author: dejian.liu
# @date:  2022-08-19 22:26
from ldj.center.nacos.NacosIns import NacosIns
from ldj.common import Cache
from ldj.config import settings
from ldj.feign.center.RegisterCenter import RegisterCenter
from ldj.feign.enums.RegisterCenterType import RegisterCenterType
from ldj.feign.exception.BusinessException import BusinessException
from ldj.feign.model.ServiceInfo import ServiceInfo


# 获取服务对应的服务器地址
def get_service_server(serviceId: str, groupName: str) -> ServiceInfo:
    """
    :param serviceId: 服务ID
    :param groupName: 分组名称
    :return:
    """
    key = "{0}@@{1}".format(groupName, serviceId)
    serviceInfo = Cache.CACHE_SERVICE_INFOS.get(key)
    if serviceInfo is None:
        cls = RegisterCenterType.parse(settings.REGISTER_CENTER)
        if len(cls.__bases__) > 0 and cls.__bases__[0].__name__ == RegisterCenter.__name__:
            serviceInfo = cls._obtain_service(serviceId, groupName)
            Cache.CACHE_SERVICE_INFOS[key] = serviceInfo
        else:
            raise BusinessException("not support {}".format(cls))
    return serviceInfo;


# 初始化注册中心
def init_register_center():
    cls = RegisterCenterType.parse(settings.REGISTER_CENTER)
    if len(cls.__bases__) > 0 and cls.__bases__[0].__name__ == RegisterCenter.__name__:
        if cls.__name__ == "NacosCenter":
            NacosIns.init_nacos()
    else:
        raise BusinessException("not support {}".format(cls))
