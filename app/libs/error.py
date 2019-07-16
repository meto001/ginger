# _*_ coding:utf-8 _*_
from flask import request, json
from werkzeug.exceptions import HTTPException

__author__ = 'meto'
__date__ = '2019/7/11 14:39'


class APIException(HTTPException):
    code = 500
    msg = 'sorry, we make a mistake'
    error_code = 999

    def __init__(self, msg=None, code=None, error_code=None,
                 headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        # python3 中super()里面可以为空，python2需要写为super(APIException,self)
        super().__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            request=request.method+' '+self.get_url_no_param()
        )
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        return [('Content-Type','application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]