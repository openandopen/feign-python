#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-15 16:53
from requests import Response
from ldj.example import ExampleConfig
from ldj.example.dto.models import QueryDto
from ldj.feign.decorator.Api import Api
from ldj.feign.decorator.Feign import Feign
from ldj.feign.enums.Method import Method


@Feign(prefix="/shared/dict/api/dict",serviceId="shared", serviceUrl=ExampleConfig.SERVER_URL, name="共享服务-字典服务")
class DictApi2NoCenter:

    @Api(method=Method.GET, uri="single", name="查询枚举详情")
    def single(self, tenantKey: str, namespaceCode: str,
               appCode: str, dictCode: str) -> Response: ...

    @Api(method=Method.POST, uri="list", name="查询字典列表数据")
    def list(self, queryDto: QueryDto) -> Response: ...
