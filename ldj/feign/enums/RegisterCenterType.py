#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author: dejian.liu
# @date:  2022-08-19 16:48


# 注册中心类型
from ldj.feign.center.NacosCenter import NacosCenter
from ldj.feign.enums.BaseEnum import BaseEnum


class RegisterCenterType(BaseEnum):
    NACOS = NacosCenter


