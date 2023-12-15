#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author: dejian.liu
# @date:  2023-12-14 16:03
from requests import Response

from ldj.example import ExampleConfig
from ldj.example.interceptor.MyInterceptor import MyInterceptor
from ldj.feign.decorator.Api import Api
from ldj.feign.decorator.Feign import Feign
from ldj.feign.decorator.FeignApi import FeignApi
from ldj.feign.enums.Method import Method
from models import QueryDto
'''
自定义编码与解码器实例
'''
my_interceptor = MyInterceptor()

class DictNacosApi:
    '''
    静态方法直接调用【nacos注册中心】  serviceId为注册中心服务名
    '''

    @staticmethod
    @FeignApi(method=Method.POST, uri="/sd/api/gc/dict/list", serviceId="sd", name="字典数据",interceptor=my_interceptor)
    def list(esQueryDto: QueryDto) -> Response: ...





@Feign(prefix="/sd/api/gc/dict", serviceId="sd", name="共享服务-字典服务", interceptor=my_interceptor)
class DictNacosApi2:
    '''
    实例方式调用  【nacos注册中心】 serviceId为注册中心服务名
    '''

    @Api(method=Method.POST, uri="list", name="查询字典列表数据")
    def list(self, queryDto: QueryDto) -> Response: ...


'''
设置nacos地址
'''
ExampleConfig.init_nacos_config();
queryDto = QueryDto()
queryDto.appCode = "gc"
queryDto.tenantKey = "123"
queryDto.namespaceCode = 'default'
response = DictNacosApi.list(queryDto)
print(response.data)
print("===================================")
api2 = DictNacosApi2()
response = api2.list(queryDto)
print(response)
