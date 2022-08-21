#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author: dejian.liu
# @date:  2022-08-19 16:47
from ldj.feign.enums.BaseEnum import BaseEnum
from ldj.feign.router.HashRouter import HashRouter
from ldj.feign.router.RandomRouter import RandomRouter
from ldj.feign.router.RoundRobinRouter import RoundRobinRouter


# 路由类型
class RouterType(BaseEnum):
    HASH = HashRouter
    RANDOM = RandomRouter
    ROUND_ROBIN = RoundRobinRouter
