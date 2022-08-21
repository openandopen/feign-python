#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-19 15:04
# 该注解作用在类上面,用于定义服务全局配置信息
from functools import wraps

from ldj.config import settings
from ldj.feign.center import RegisterCenterHelper
from ldj.feign.context.ServiceContext import ServiceContext
from ldj.feign.exception.handler.DefaultExceptionHandler import DefaultExceptionHandler
from ldj.feign.exception.handler.ExceptionHandler import ExceptionHandler
from ldj.feign.interceptor.DefaultInterceptor import DefaultInterceptor
from ldj.feign.interceptor.Interceptor import Interceptor
from ldj.feign.model.ServiceInfo import ServiceInfo


class Feign(object):
    def __init__(self, serviceId: str = None, prefix: str = None,
                 groupName: str = None, serviceUrl: str = None,
                 name: str = None, interceptor: Interceptor = None,
                 exceptionHandler: ExceptionHandler = None, timeout: int = None):
        """
        :param serverId 服务ID, 从注册中心获取服务
        :param method 请求方法（GET|POST|PUT|DELETE）
        :param prefix uri前缀
        :param serverUrl 服务地址 ,指定服务地址,如果不为空，则按此规则走
        :param groupName 分组名
        :param name 服务名
        :param interceptor 拦截器
        :param exceptionHandler 异常处理器
        """
        self.serviceId = serviceId
        self.prefix = prefix
        self.serviceUrl = serviceUrl
        self.name = name
        self.groupName = groupName
        self.timeout = timeout
        if self.timeout is None:
            self.timeout = settings.DEFAULT_TIMEOUT
        if groupName is None:
            self.groupName = "DEFAULT_GROUP"
        self.interceptor = interceptor
        if self.interceptor is None:
            self.interceptor = DefaultInterceptor()
        self.exceptionHandler = exceptionHandler
        if self.exceptionHandler is None:
            self.exceptionHandler = DefaultExceptionHandler()

    def __call__(self, cls):
        @wraps(cls)
        def wrapper(*args, **kwargs):
            if type(cls).__name__ != 'type':
                raise Exception("@Feign can only work on classes ")
            key = "{}.{}".format(cls.__module__, cls.__name__)

            serviceInfo = ServiceContext.get_service_server(key)
            if serviceInfo is None:
                if self.serviceId is not None and self.serviceUrl is None:
                    serviceInfo = RegisterCenterHelper.get_service_server(self.serviceId, self.groupName)
                    serviceInfo.prefix = self.prefix
                    serviceInfo.serverUrl = self.serviceUrl
                    serviceInfo.interceptor = self.interceptor
                    serviceInfo.exceptionHandler = self.exceptionHandler
                    ServiceContext.put_service_server(key, serviceInfo)
                else:
                    serviceInfo = ServiceInfo()
                    serviceInfo.prefix = self.prefix
                    serviceInfo.serverUrl = self.serviceUrl
                    serviceInfo.interceptor = self.interceptor
                    serviceInfo.exceptionHandler = self.exceptionHandler
                    ServiceContext.put_service_server(key, serviceInfo)
            return cls(*args, **kwargs)

        return wrapper
