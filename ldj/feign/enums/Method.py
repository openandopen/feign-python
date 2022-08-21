#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author: dejian.liu
# @date:  2022-08-19 16:47
from ldj.feign.enums.BaseEnum import BaseEnum


class Method(BaseEnum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    HEADER = "HEADER"
    OPTION = "OPTION"