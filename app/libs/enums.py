# _*_ coding:utf-8 _*_
__author__ = 'meto'
__date__ = '2019/7/9 15:30'

from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201
