#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author: dejian.liu
# @date:  2023-05-18 17:31
import json
from typing import List

from pydantic import BaseModel, BaseSettings


class DictDetailDto(BaseModel, json.JSONEncoder):
    codeCn: str = None,
    codeEn: str = None,
    code: int = None,


class DictDto(BaseModel, json.JSONEncoder):
    namespace: str = None,
    appCode: str = None,
    dictName: str = None,
    dictCode: str = None,
    dictDetails: list = None

    def default(self, obj):
        """
        只要检查到了是bytes类型的数据就把它转为str类型
        :param obj:
        :return:
        """
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)


class QueryDto(BaseModel, json.JSONEncoder):
    tenantKey: str = None,
    namespaceCode: str = None,
    appCode: str = None

    def default(self, obj):
        """
        只要检查到了是bytes类型的数据就把它转为str类型
        :param obj:
        :return:
        """
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)
