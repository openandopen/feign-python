#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author: dejian.liu
# @date:  2022-08-19 18:08
from loguru import logger

from ldj.feign.exception.handler.ExceptionHandler import ExceptionHandler


class DefaultExceptionHandler(ExceptionHandler):
    def handler(self, e: Exception):
        logger.error(e)


