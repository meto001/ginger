# _*_ coding:utf-8 _*_
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

__author__ = 'meto'
__date__ = '2019/7/9 15:28'

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    # data = request.json
    # data = request.args.to_dict()
    form = ClientForm().validate_for_api()

    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email
    }
    promise[form.type.data]()
    print(Success())

    pass
    return Success()


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
