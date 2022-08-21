#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-15 17:02

from ldj.example.DictApiNoCenter import  DictApiNoCenter
from ldj.example.dto.models import QueryDto
from ldj.feign.model.Response import Response


def list_all():
    queryDto = QueryDto()
    queryDto.appCode = "shared"
    queryDto.namespaceCode = "default"
    queryDto.tenantKey = "05766005256305607631060124224200"
    print(queryDto.json())
    res: Response = DictApiNoCenter.list(queryDto)
    print(res)


def dict_detail():
    res: Response = DictApiNoCenter.single("05766005256305607631060124224200", "default", "shared", "PersonalStatus")
    print(res)
    data = res.result
    print(data)



list_all()
dict_detail()
