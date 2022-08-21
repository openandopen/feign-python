#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-19 9:26
import requests

from pydantic import BaseModel

# 拦截器
from toolbox import ObjectDict

from ldj.common import Constant

from ldj.config import settings
from ldj.feign.enums.Method import Method
from ldj.feign.interceptor.Interceptor import Interceptor, ProcessRequest


# 默认拦截器
from ldj.feign.model.Response import Response


class DefaultInterceptor(Interceptor):
    # 默认请求处理
    def encode(self, method: Method,
                        headers: dict = None,
                        params: dict = None,
                        body: object = None,
                        data: object = None,
                        ) -> ProcessRequest:
        pr = ProcessRequest()
        pr.method = method
        headers["Content-Type"] = "application/json"
        headers["api-token"] = settings.API_TOKEN
        pr.headers = headers
        pr.params = params
        pr.body = body
        pr.data = data
        return pr

    # 默认响应处理
    def decode(self, resp: requests.Response) -> Response:
        if Constant.HTTP_SUCCESS == resp.status_code:
            res_data = ObjectDict(resp.json())
            code = res_data.code
            status = res_data.status
            message = res_data.message
            data = res_data.result

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
        else:
            final_result = Response.fail(status=Constant.HTTP_ERROR, code=Constant.BIZ_ERROR,
                                         message=resp.reason)
        return final_result
