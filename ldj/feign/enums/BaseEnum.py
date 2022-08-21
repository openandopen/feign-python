#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述: 枚举基类
# @author: dejian.liu
# @date:  2022-08-19 17:08
from enum import Enum
from typing import Union


class BaseEnum(Enum):

    @classmethod
    def parse(cls, name: str) -> Union[str, None]:
        if name is None or len(name) == 0:
            return None
        name = name.upper()
        return cls._member_map_[name].value
