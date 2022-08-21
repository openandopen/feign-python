#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-19 14:58
from ldj.feign.model.HostInfo import HostInfo
from ldj.feign.model.ServiceInfo import ServiceInfo


class Router:

    # 选择远程主机
    @staticmethod
    def _select_host(serviceInfo: ServiceInfo) -> HostInfo:
        ...


