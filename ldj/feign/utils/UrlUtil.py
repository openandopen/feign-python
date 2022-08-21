#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 描述: URL工具类
# @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# @date:  2022-08-19 15:01
class UrlUtil:

    @staticmethod
    def wrap_url(uri: str, prefix: str = None) -> str:
        if prefix is None:
            return uri
        elif prefix is not None:
            if uri.startswith("/") and prefix.endswith("/"):
                return prefix + uri[1, len(uri)]
            elif not uri.startswith("/") and prefix.endswith("/"):
                return prefix + uri
            elif not uri.startswith("/") and not prefix.endswith("/"):
                return prefix + "/" + uri
            elif uri.startswith("/") and not prefix.endswith("/"):
                return prefix + uri
        else:
            return uri
