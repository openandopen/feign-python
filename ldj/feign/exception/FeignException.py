#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-12 14:41

class FeignException(Exception):
    def __init__(self, message):
        self.message = message
