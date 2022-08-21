#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述:
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-03 15:34
import json


class Properties(object):
    # '''
    # :param prop_str 为key=value类型的字符串
    # '''
    def __init__(self, prop_str: str):
        self.prop_str = prop_str
        self.prop = dict()
        self.__parse()

    # 解析配置文件
    def __parse(self):
        contents = self.prop_str.splitlines()
        for line in contents:
            try:
                line = line.strip()
                if len(line) == 0:
                    continue
                if line.find("#") != -1:
                    line = line[line.find("#"):len(line)]
                    # print(line)
                    continue
                if line.find('=') > 0:
                    strs = line.split('=')
                    key = strs[0].strip()
                    value = line[len(strs[0]) + 1:].strip()
                    self.prop[key] = value
            except Exception as e:
                print(e)

    # 配置合并
    def add_all(self, dict_prop: dict):
        if type(dict_prop).__name__ == 'dict':
            self.prop = dict(self.prop, **dict_prop)
        elif type(dict_prop).__name__ == 'Properties':
            self.prop = dict(self.prop, **dict_prop.prop)

    def get_value(self, key):
        return self.prop.get(key)

    def remove_prop(self, key):
        self.prop.pop(key)
        return self

    def clear(self):
        self.prop.clear()
        return self

    def get_source_prop(self) -> dict:
        return self.prop
