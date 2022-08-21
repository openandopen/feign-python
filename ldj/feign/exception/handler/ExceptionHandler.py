#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述: 异常处理器
# @author: dejian.liu
# @date:  2022-08-19 17:38
from pydantic import BaseModel


class ExceptionHandler(BaseModel):

    def handler(self, e: Exception): ...
