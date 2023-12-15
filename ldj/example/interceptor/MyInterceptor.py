#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author: dejian.liu
# @date:  2022-08-21 11:56
import requests
from pydantic import BaseModel
from toolbox import ObjectDict

from ldj.common import Constant
from ldj.feign.enums.Method import Method
from ldj.feign.interceptor.Interceptor import Interceptor, ProcessRequest
from ldj.feign.model.Response import Response


class MyInterceptor(Interceptor):
    def decode(self, resp: requests.Response) -> object:
        '''
         自定义拦截器
        :param resp:
        :return:
        '''
        if Constant.HTTP_SUCCESS == resp.status_code:
            ##解析原始JSON对象
            res_data = ObjectDict(resp.json())
            ## 封装自定义返回对象code,status,message,data为业务后端响应，使用者根据业务需要调整
            code = res_data.code
            status = res_data.status
            message = res_data.message
            data = res_data.data

            if isinstance(data, list):
                result = list()
                for d in data:
                    result.append(ObjectDict(d))
            elif isinstance(data, BaseModel) or type(data).__name__ == 'dict':
                result = ObjectDict(data)
            else:
                result = data
            if Constant.HTTP_SUCCESS == status:
                final_result = Response.success(status, code, message, result)
            else:
                final_result = Response.fail(status, code, message)

        elif Constant.HTTP_405 == resp.status_code:
            final_result = Response.fail(status=Constant.HTTP_405, code=Constant.BIZ_ERROR,
                                         message="Method not allowed")
        elif Constant.HTTP_401 == resp.status_code:
            final_result = Response.fail(status=Constant.HTTP_401, code=Constant.BIZ_ERROR,
                                         message="Unauthorized")
        elif Constant.HTTP_403 == resp.status_code:
            final_result = Response.fail(status=Constant.HTTP_403, code=Constant.BIZ_ERROR,
                                         message="forbidden")
        elif Constant.HTTP_404 == resp.status_code:
            final_result = Response.fail(status=Constant.HTTP_404, code=Constant.BIZ_ERROR,
                                         message="url Not Found")
        elif Constant.HTTP_504 == resp.status_code:
            final_result = Response.fail(status=Constant.HTTP_504, code=Constant.BIZ_ERROR,
                                         message="Gateway Timeout")
        else:
            final_result = Response.fail(status=Constant.HTTP_ERROR, code=Constant.BIZ_ERROR,
                                         message=resp.reason)
        return final_result

    def encode(self, method: Method, headers: dict = None,
               params: dict = None, body: dict = None,
               data: object = None) -> ProcessRequest:
        '''
        请求编码
        :param method: 请求方式
        :param headers: 头信息
        :param params: 请求参数
        :param body: 请求dict body
        :param data: 请求对象轻
        :return:
        '''
        pr = ProcessRequest()
        pr.method = method
        pr.headers = headers
        pr.params = params
        pr.body = body
        pr.data = data
        return pr
