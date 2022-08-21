#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-16 15:27
from pydantic import BaseModel


class DictDetailDto(BaseModel):
    codeCn: str = None
    codeEn: str = None
    code: int = None


class QueryDto(BaseModel):
    tenantKey:str = None
    namespaceCode: str = "default"
    appCode: str = None

