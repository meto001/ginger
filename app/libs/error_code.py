# _*_ coding:utf-8 _*_

from app.libs.error import APIException

__author__ = 'meto'
__date__ = '2019/7/10 16:44'


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake'
    error_code = 999

class ClientTypeEroor(APIException):
    # 400 请求参数错误 401 未授权 403 禁止访问  404 页面未找到
    # 500  服务器内部错误
    # 2
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000
