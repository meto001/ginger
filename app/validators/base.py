# _*_ coding:utf-8 _*_
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException

__author__ = 'meto'
__date__ = '2019/7/12 11:20'


class BaseForm(Form):

    def __init__(self):
        data = request.json
        super().__init__(data=data)

    def validate_for_api(self):
        valid = super().validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self
