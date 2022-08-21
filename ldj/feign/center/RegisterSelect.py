# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# # 描述:
# # @author:  <a href="mailto:zuiwoxing@qq.com">dejian.liu</a>
# # @date:  2022-08-19 14:11
# from pydantic import BaseModel
#
# from ldj.config import settings
# from ldj.feign.center.NacosCenter import NacosCenter
#
# from ldj.feign.exception.exceptions import BusinessException
#
#
# class RegisterSelect(BaseModel):
#
#     # 获取当前配置的注册中心
#     @staticmethod
#     def current_register_center() -> type:
#         if settings.REGISTER_CENTER is None:
#             raise BusinessException("please set settings.REGISTER_CENTER")
#         if "nacos" == settings.REGISTER_CENTER:
#             return NacosCenter
#         else:
#             raise BusinessException("settings.REGISTER_CENTER not support")