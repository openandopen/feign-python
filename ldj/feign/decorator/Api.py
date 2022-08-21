#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-19 15:04
# 该注解作用在方法上面，用于定义具体的API
import types
from functools import wraps
from http.client import HTTPConnection

import requests
from pydantic import BaseModel

from ldj.config import settings
from ldj.feign.context.ServiceContext import ServiceContext
from ldj.feign.enums.Method import Method
from ldj.feign.exception.BusinessException import BusinessException

from ldj.feign.interceptor.Interceptor import ProcessRequest
from ldj.feign.router.RouterHelper import RouterHelper

from ldj.feign.utils.UrlUtil import UrlUtil
from loguru import logger

HTTPConnection.debuglevel = 1 if settings.HTTP_DEBUG else 0


# 作用在方法上面
class Api(object):
    def __init__(self, method: Method, uri: str, name: str = None, timeout: int = None):
        """
        :param serverId 服务ID, 从注册中心获取服务
        :param method 请求方法（GET|POST|PUT|DELETE）
        :uri uri uri
        :name 服务名
        :service_info 服务信息
        """
        self.method = method
        self.uri = uri
        self.name = name
        self.serviceInfo = None
        self.func = None
        self.funcArgs = None
        self.timeout = timeout
        if self.timeout is None:
            self.timeout = settings.DEFAULT_TIMEOUT

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if type(func).__name__ == 'type':
                raise Exception("@Api can only work on function ")

            if isinstance(func, types.FunctionType):
                arg0 = args[0]
                if type(arg0).__name__ == 'type':
                    module_cls_key = "{}.{}".format(arg0.__module__, arg0.__name__)
                else:
                    mt = type(arg0)
                    module_cls_key = "{}.{}".format(mt.__module__, mt.__name__)
            else:
                logger.error("function={}".format(func))
                raise BusinessException("not support")

            serviceInfo = ServiceContext.get_service_server(module_cls_key)
            self.serviceInfo = serviceInfo
            self.func = func
            self.funcArgs = args
            result = self._execute()
            return result

        return wrapper

    # 执行请求
    def _execute(self):
        func_result = None
        serviceInfo = self.serviceInfo
        serverUrl = serviceInfo.serverUrl
        service_url = "/"
        if serverUrl is not None:
            service_url = UrlUtil.wrap_url(serviceInfo.prefix, prefix=serverUrl)
        elif serviceInfo is not None:
            service_url = RouterHelper.get_host_url(settings.HTTP_PROTOCOL, serviceInfo)
            service_url = UrlUtil.wrap_url(serviceInfo.prefix, prefix=service_url)

        finalUrl = UrlUtil.wrap_url(self.uri, prefix=service_url)
        interceptor = serviceInfo.interceptor
        exceptionHandler = serviceInfo.exceptionHandler
        method = self.method
        headers = {}
        params = {}
        body = {}
        try:
            if method == Method.GET or method == Method.DELETE:
                if len(self.funcArgs) > 0:
                    var_names = self.func.__code__.co_varnames
                    for index, pname in enumerate(var_names):
                        params[pname] = self.funcArgs[index]
            elif method == Method.POST or method == Method.PUT:
                if len(self.funcArgs) > 1:
                    body = self.funcArgs[1]
                    if isinstance(self.funcArgs[1], BaseModel):
                        body = self.funcArgs[1].__dict__
            else:
                raise BusinessException("not support ".format(method))
            # 请求前拦截器
            pr: ProcessRequest = interceptor.encode(method=method,
                                                             headers=headers,
                                                             params=params,
                                                             body=body)
            # 执行请求
            resp = requests.request(method.name, finalUrl,
                                    params=pr.params, json=pr.body,
                                    headers=pr.headers,
                                    data=pr.data, timeout=self.timeout)
            # 响应处理
            func_result = interceptor.decode(resp)

            # func(*args, **kwargs)
        except Exception as e:
            if exceptionHandler is not None:
                exceptionHandler.handler(e)
            else:
                raise e
        return func_result
