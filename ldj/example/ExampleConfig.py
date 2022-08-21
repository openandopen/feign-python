#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author: dejian.liu
# @date:  2022-08-21 9:01
from ldj.config import settings


def init_nacos_config():
    settings.NACOS_SERVER = "http://127.0.0.1:9191"
    settings.NACOS_USER_NAME = "admin"
    settings.NACOS_PASSWORD = "123456"
    settings.NACOS_NAMESPACE = "dev"
    settings.NACOS_ALG_WEB_GROUP = "DEFAULT_GROUP"
    settings.NACOS_ALG_WEB_DATA_ID = "shared"
    settings.NACOS_SERVER_NAME = "user"


SERVER_URL = "http://127.0.0.1:8080"