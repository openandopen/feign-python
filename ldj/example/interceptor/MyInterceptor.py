#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author: dejian.liu
# @date:  2022-08-21 11:56
import requests
from ldj.feign.enums.Method import Method
from ldj.feign.interceptor.Interceptor import Interceptor, ProcessRequest
class MyInterceptor(Interceptor):
    def decode(self, resp: requests.Response) -> object:
        pass

    def encode(self, method: Method, headers: dict = None,
               params: dict = None, body: dict = None,
               data: object = None) -> ProcessRequest:
        pr = ProcessRequest()
        pr.method = method
        pr.headers = headers
        pr.params = params
        pr.body = body
        pr.data = data
        return pr