#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-19 14:12
from pydantic import BaseModel
from ldj.feign.model.ServiceInfo import ServiceInfo


class RegisterCenter(BaseModel):

    # 获取注册服务，待子类实现
    @staticmethod
    def _obtain_service(serviceId: str, groupName: str) -> ServiceInfo:
        ...

