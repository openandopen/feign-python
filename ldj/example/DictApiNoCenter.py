#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-15 16:53
from requests import Response

from ldj.example import ExampleConfig
from ldj.feign.decorator.FeignApi import FeignApi
from ldj.example.dto.models import QueryDto
from ldj.feign.enums.Method import Method


class DictApiNoCenter:

    @staticmethod
    @FeignApi(method=Method.POST, uri="/shared/dict/api/dict/list",serviceId="shared",
              serviceUrl=ExampleConfig.SERVER_URL, name="字典数据")
    def list(queryDto: QueryDto) -> Response: ...

    @staticmethod
    @FeignApi(method=Method.GET, uri="/shared/dict/api/dict/single",serviceId="shared",
              serviceUrl=ExampleConfig.SERVER_URL,  name="查询枚举详情")
    def single(tenantKey:str,namespaceCode:str,
                    appCode: str, dictCode: str) -> Response: ...
