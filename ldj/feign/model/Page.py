#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-19 9:50
from pydantic import BaseModel


class Page(BaseModel):
    total: int = 0
    results: list = None

    @staticmethod
    def build(results: list, total: int):
        req = Page()
        req.results = results
        req.total = total
        return req
