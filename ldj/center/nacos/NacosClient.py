#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述: 统一配置/注册中心
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-03 14:23
import nacos

from ldj.config import settings
from ldj.center.prop.Properties import Properties


class NacosClient:
    client: nacos.NacosClient = None
    # dict 字典类型
    prop_dict = dict()

    # 获取nacos客户端
    @staticmethod
    def get_client() -> nacos.NacosClient:
        try:
            if NacosClient.client is None:
                server = settings.NACOS_SERVER
                env = settings.NACOS_NAMESPACE
                NacosClient.client = nacos.NacosClient(server, endpoint=None, namespace=env, ak=None, sk=None,
                                                       username=settings.NACOS_USER_NAME,
                                                       password=settings.NACOS_PASSWORD)

            return NacosClient.client
        except Exception as e:
            print(e)
            raise Exception("获取nacos client 失败:{}".format(e.__cause__))



    @staticmethod
    def get_config(dataId: str, group: str) -> Properties:
        '''
          :param dataId  节点ID
          :param group 分组
          :return kli_alg_platform.common.utils.prop.Properties
          '''
        config_key = group + "_" + dataId
        properties = NacosClient.prop_dict.get(config_key)
        print(properties)
        if properties is None:
            prop_str = NacosClient.get_client().get_config(dataId, group)
            properties = Properties(prop_str)
            NacosClient.prop_dict[config_key] = properties
        return properties

    '''
    :param dataId  节点ID
    :param group 分组
    :param callback 回调函数
    '''

    @staticmethod
    def add_config_watcher(dataId: str, group: str, callback):
        config_key = group + "_" + dataId

        # 定义内部回调函数
        def __config_callback(data):
            print("group:{} data_id:{} config change!".format(data.get("group"), data.get("data_id")))
            prop_str = data["content"]
            new_prop = Properties(prop_str)
            source_prop = NacosClient.get_config(dataId, group)
            source_prop.add_all(new_prop.prop)
            NacosClient.prop_dict[config_key] = source_prop
            callback(source_prop)

        # 增加配置监听
        NacosClient.get_client().add_config_watcher(dataId, group, __config_callback)

    @staticmethod
    def remove_config_watcher(dataId: str, group: str, callback):
        NacosClient.get_client().remove_config_watcher(dataId, group, callback)


