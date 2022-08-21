#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-18 22:17
# 服务信息缓存
# key={groupName}@@{servieId} value=ServiceInfo
CACHE_SERVICE_INFOS = dict()

# 服务信息
# key=class.__module__+"."+class.__name__  value=ServiceInfo
SERVICE_INFOS = dict()

