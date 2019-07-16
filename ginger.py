# _*_ coding:utf-8 _*_
from werkzeug.exceptions import HTTPException

from app.app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

__author__ = 'meto'
__date__ = '2019/7/8 17:02'

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    # flask 1.0 可以捕捉所以异常
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        if not app.config['DEBUG']:
            return ServerError()
        return e
    pass


if __name__ == '__main__':
    app.run(debug=True)
