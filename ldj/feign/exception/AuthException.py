#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author: dejian.liu
# @date:  2022-08-19 17:39
# 认证异常
from ldj.feign.exception.FeignException import FeignException


class AuthException(FeignException): ...