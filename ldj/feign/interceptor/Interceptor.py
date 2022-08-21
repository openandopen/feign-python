#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-19 9:25
import requests
from pydantic import BaseModel
from ldj.feign.enums.Method import Method


class ProcessRequest(BaseModel):
    method: Method = None,
    headers: dict = None,
    # 请求参数 放在URL中的参数对象
    params: dict = None,
    #  A JSON serializable Python object to send in the body of the :class:`Request`.
    body: object = None,
    #  Dictionary, list of tuples, bytes, or file-like
    data: object = None


# 拦截器
class Interceptor(BaseModel):

    # 请求前编码
    def encode(self, method: Method, headers: dict = None,
               params: dict = None, body: dict = None,
               data: object = None) -> ProcessRequest: ...

    """
    :param method 请求方式GET|PUT|POST|DELETE
    :param headers 请求头
    :param params 请求参数
    :param body 请求body
    :param data 请求body二进制|list|tuble
    """

    # 响应解码处理
    def decode(self, resp: requests.Response) -> object: ...

    """
    :param resp 响应对象
    """
