#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-15 16:36
import json
import sys
import threading
import time

from loguru import logger

from ldj.center.nacos.NacosClient import NacosClient
from ldj.center.prop.Properties import Properties
from ldj.config import settings

# 可调用NacosIns.init_nacos() 启动nacos
class NacosIns:
    WEB_NACOS_PROP: Properties = None

    @staticmethod
    def get_current_host_port():
        host = "0.0.0.0"
        port = 8000
        if len(sys.argv) == 4:
            host_port = sys.argv[3]
            host_ports = host_port.split(":", 2)
            host = host_ports[0]
            port = host_ports[1]
        return {"host": host, "port": port}

    @staticmethod
    def __hearbeat():
        host_port = NacosIns.get_current_host_port()
        host = host_port.get("host")
        port = host_port.get("port")
        while True:
            try:
                time.sleep(5)
                hearbeat = NacosClient.get_client().send_heartbeat(settings.NACOS_SERVER_NAME, host, port)
                # print(hearbeat)
            except Exception as e:
                print(e)

    @staticmethod
    # 配置变化监听
    def __config_change_callback(newProp: Properties):
        print(json.dumps(newProp.prop))

    # 初始化配置
    @staticmethod
    def init_nacos():
        # 初始化获取配置
        NacosIns.WEB_NACOS_PROP = NacosClient.get_config(settings.NACOS_ALG_WEB_DATA_ID,
                                                              settings.NACOS_ALG_WEB_GROUP)
        # 监听nacos配置变化
        NacosClient.add_config_watcher(settings.NACOS_ALG_WEB_DATA_ID, settings.NACOS_ALG_WEB_GROUP,
                                       NacosIns.__config_change_callback)
        instance_meta = dict();
        instance_meta["preserved.center.source"] = "SPRING_CLOUD"
        host_port = NacosIns.get_current_host_port()
        host = host_port.get("host")
        port = host_port.get("port")
        instance_meta["preserved.center.ip"] = host_port.get("host")
        instance = NacosClient.get_client().add_naming_instance(settings.NACOS_SERVER_NAME, host,
                                                                port,
                                                                ephemeral=True, healthy=True,
                                                                metadata=instance_meta)
        logger.info("center service:{}".format(instance))
        thread = threading.Thread(target=NacosIns.__hearbeat, daemon=True)
        thread.start()

    # 根据KEY获取配置
    @staticmethod
    def get_value(key: str):
        return NacosIns.WEB_NACOS_PROP.get_value(key)
