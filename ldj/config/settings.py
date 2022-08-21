#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-10 14:39



# nacos 统一配置中心
NACOS_SERVER = "http://127.0.0.1:9191"
NACOS_USER_NAME = "admin"
NACOS_PASSWORD = "xxxxxxxx"
NACOS_NAMESPACE = "dev"
NACOS_ALG_WEB_GROUP = "DEFAULT_GROUP"
NACOS_ALG_WEB_DATA_ID = "shared"
NACOS_SERVER_NAME = "user"
# 默认超时
DEFAULT_TIMEOUT = 60

# 注册中心类型 (目前只支持 NACOS)
REGISTER_CENTER = "NACOS"
# 路由类型(HASH,RANDOM,ROUND_ROBIN)
ROUTER_TYPE = "HASH"
HTTP_PROTOCOL = "http"
API_TOKEN = "4297f44b13955235245b2497399d7a93"

# 是否debug
HTTP_DEBUG = False
