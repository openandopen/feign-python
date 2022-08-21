#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-19 15:04
# 1=开启日志 0=关闭日志
from http.client import HTTPConnection
import types
from functools import wraps
from http.client import HTTPConnection

import requests

from ldj.config import settings
from ldj.feign.center import RegisterCenterHelper
from ldj.feign.enums.Method import Method
from ldj.feign.exception.BusinessException import BusinessException
from ldj.feign.exception.handler.DefaultExceptionHandler import DefaultExceptionHandler
from ldj.feign.exception.handler.ExceptionHandler import ExceptionHandler
from ldj.feign.interceptor.DefaultInterceptor import DefaultInterceptor

from ldj.feign.interceptor.Interceptor import ProcessRequest, Interceptor
from ldj.feign.router.RouterHelper import RouterHelper
from ldj.feign.utils.UrlUtil import UrlUtil

HTTPConnection.debuglevel = 1 if settings.HTTP_DEBUG else 0


# 可直接装饰在静态方法上面
class FeignApi(object):

    def __init__(self, method: Method, uri: str,
                 serviceId: str = None, groupName: str = None,
                 serviceUrl: str = None, name: str = None,
                 interceptor: Interceptor = None, exceptionHandler: ExceptionHandler = None,
                 timeout: int = None):
        """
        :param method 请求方法（GET|POST|PUT|DELETE）
        :uri uri
        :param serviceId 服务ID, 从注册中心获取服务
        :param groupName: str = None,
        :param serverUrl 服务地址 ,指定服务地址,如果不为空，则按此规则走
        :param name 服务名(描述)
        :param interceptor 请求与响应拦截器
        :param exceptionHandler 异常拦截器
        """
        self.serviceId = serviceId
        self.groupName = groupName
        if groupName is None:
            self.groupName = "DEFAULT_GROUP"
        self.method = method
        self.uri = uri
        self.serviceUrl = serviceUrl
        self.name = name
        self.timeout = timeout
        if self.timeout is None:
            self.timeout = settings.DEFAULT_TIMEOUT
        self.interceptor = interceptor
        if self.interceptor is None:
            self.interceptor = DefaultInterceptor()
        self.exceptionHandler = exceptionHandler
        if self.exceptionHandler is None:
            self.exceptionHandler = DefaultExceptionHandler()

    # 调用函数时触发
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_result = None
            service_url = self.serviceUrl
            method = self.method
            headers = {}
            params = {}
            body = {}
            data = None
            try:
                if method == Method.GET or method == Method.DELETE:
                    if len(args) > 0:
                        var_names = func.__code__.co_varnames
                        for index, pname in enumerate(var_names):
                            params[pname] = args[index]
                elif method == Method.POST or method == Method.PUT:
                    if len(args) > 0:
                        body = args[0].__dict__
                else:
                    raise BusinessException("not support ".format(method))

                # 从注册中心获取
                if service_url is None or len(service_url) == 0:
                    serverInfo = RegisterCenterHelper.get_service_server(self.serviceId, self.groupName)
                    service_url = RouterHelper.get_host_url(settings.HTTP_PROTOCOL, serverInfo)
                finalUrl = UrlUtil.wrap_url(self.uri, prefix=service_url)
                # 请求前拦截器
                pr: ProcessRequest = self.interceptor.encode(method=method,
                                                                      headers=headers,
                                                                      params=params,
                                                                      body=body,
                                                                      data=data)
                # 执行请求
                resp = requests.request(method.name, finalUrl,
                                        params=pr.params, json=pr.body,
                                        headers=pr.headers,
                                        data=pr.data, timeout=self.timeout)
                # 响应处理
                func_result = self.interceptor.decode(resp)

                # func(*args, **kwargs)
            except Exception as e:
                if self.exceptionHandler is not None:
                    self.exceptionHandler.handler(e)
                else:
                    raise e
            return func_result

        return wrapper
