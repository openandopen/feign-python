#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-15 17:02

from ldj.example import ExampleConfig
from ldj.example.DictApi import DictApi
from ldj.example.dto.models import QueryDto
from ldj.feign.model.Response import Response


def list_all():
    queryDto = QueryDto()
    queryDto.appCode = "shared"
    queryDto.namespaceCode = "default"
    queryDto.tenantKey = "05766005256305607631060124224200"
    print(queryDto.json())
    res: Response = DictApi.list(queryDto)
    print(res)


def dict_detail():
    res: Response = DictApi.single("05766005256305607631060124224200", "default", "shared", "PersonalStatus")
    print(res)
    data = res.result
    print(data)


ExampleConfig.init_nacos_config()
list_all()
dict_detail()
