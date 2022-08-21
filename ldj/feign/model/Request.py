#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-19 9:49
# 请求对象
from pydantic import BaseModel


class Request(BaseModel):
    body: object = None
    start: int = 0
    limit: int = 10
    params: dict = None

    @staticmethod
    def build(body: object, start: int, limit: int):
        req = Request()
        req.body = body
        req.start = start
        req.limit = limit
        return req