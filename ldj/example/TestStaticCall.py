#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author: dejian.liu
# @date:  2023-12-14 16:03
from requests import Response

from ldj.example import ExampleConfig
from ldj.feign.decorator.FeignApi import FeignApi
from ldj.feign.enums.Method import Method
from models import QueryDto


class DictExampleApi:
    '''
    静态方法直接调用【无注册中心】,serviceUrl为请求地址前缀, serviceId无效
    '''
    @staticmethod
    @FeignApi(method=Method.POST, uri="/sd/api/gc/dict/list",serviceId="sd",
              serviceUrl=ExampleConfig.SERVER_URL, name="字典数据")
    def list(esQueryDto: QueryDto) -> Response: ...


queryDto = QueryDto()
queryDto.appCode = "gc"
queryDto.tenantKey="123"
queryDto.namespaceCode='default'
response = DictExampleApi.list(queryDto)

print(response)
