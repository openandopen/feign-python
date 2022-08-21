#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-19 14:54
from typing import Union

# 服务信息
from ldj.common import Cache
from ldj.feign.model.ServiceInfo import ServiceInfo


class ServiceContext:



    @staticmethod
    def get_service_server(key: str) -> Union[ServiceInfo, None]:
        """
        :param key class.__module__+"."+class.__name__
        """
        if key in Cache.SERVICE_INFOS:
            return Cache.SERVICE_INFOS[key]
        return None

    @staticmethod
    def put_service_server(key: str, serviceInfo: ServiceInfo) -> bool:
        Cache.SERVICE_INFOS[key] = serviceInfo
        return True

    @staticmethod
    def del_service_server(key: str) -> bool:
        del Cache.SERVICE_INFOS[key]
        return True

    @staticmethod
    def clear_service_server() -> bool:
        Cache.SERVICE_INFOS.clear()
        return True
