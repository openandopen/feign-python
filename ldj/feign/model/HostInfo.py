#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-19 9:50
from pydantic import BaseModel


class HostInfo(BaseModel):
    ip: str = None
    port: int = None
    weight: int = 1
    healthy: bool = True
    enabled: bool = True
    meta: dict = None