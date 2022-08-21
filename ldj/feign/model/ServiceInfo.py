#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-19 9:51
# 服务信息
from pydantic import BaseModel

from ldj.feign.exception.handler.ExceptionHandler import ExceptionHandler
from ldj.feign.interceptor.Interceptor import Interceptor
from ldj.feign.model.HostInfo import HostInfo


class ServiceInfo(BaseModel):
    name: str = None
    groupName: str = None
    prefix: str = ""
    serverUrl: str = None
    interceptor: Interceptor = None
    exceptionHandler: ExceptionHandler = None
    lastRefTime: int = None
    hosts: list[HostInfo] = None
