#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-19 9:49
from pydantic import BaseModel

from ldj.common import Constant


class Response(BaseModel):
    """
    :param status 为http状态
    :param msg 响应消息
    :param code 业务编码
    :param data 业务数据
    """
    status: int = Constant.HTTP_SUCCESS
    message: str = ""
    code: int = Constant.BIZ_SUCCESS
    data: object = None

    def toJson(self):
        return self.json()

    @staticmethod
    def success(status=None, message=None, code=None, data=None):
        if status is None:
            status = Constant.HTTP_SUCCESS
        if message is None:
            message = "ok"
        if code is None:
            code = Constant.BIZ_SUCCESS
        res = Response()
        res.status = status
        res.message = message
        res.code = code
        res.data = data
        return res

    @staticmethod
    def fail(status=None, message=None, code=None, data=None):
        res = Response()
        if status is None:
            status = Constant.HTTP_ERROR
        if message is None:
            message = "error"
        if code is None:
            code = Constant.BIZ_ERROR
        res.status = status
        res.message = message
        res.code = code
        res.data = data
        return res