#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-15 17:02

from ldj.example import ExampleConfig
from ldj.example.DictApi2 import DictApi2
from ldj.example.dto.models import QueryDto
from ldj.feign.model.Response import Response


def list_all():
    mydict = DictApi2()
    queryDto = QueryDto()
    queryDto.appCode = "shared"
    queryDto.namespaceCode = "default"
    queryDto.tenantKey = "05766005256305607631060124224200"
    print(queryDto.json())
    res = mydict.list(queryDto)
    print(res)


def dict_detail():
    mydict: DictApi2 = DictApi2()
    res: Response = mydict.single("05766005256305607631060124224200", "default", "shared", "PersonalStatus")
    print(res)
    data = res.result
    print(data)


ExampleConfig.init_nacos_config()
list_all()
dict_detail()
