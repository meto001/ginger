# _*_ coding:utf-8 _*_

from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError

from app.libs.enums import ClientTypeEnum
from app.models.user import User

__author__ = 'meto'
__date__ = '2019/7/9 15:34'
from wtforms import StringField, IntegerField
from app.validators.base import BaseForm


class ClientForm(BaseForm):
    # 账号
    account = StringField(validators=[DataRequired(message='账号不能为空'), length(
        min=5, max=32,message='长度需要在5-32之间'
    )])
    # 密码
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)

        except ValueError as e:
            print(e)
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='invalidate email')
    ])
    secret = StringField(validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       length(min=2, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError('邮箱重复！')

    def validate_nickname(self, value):
        if User.query.filter_by(nickname=value.data).first():
            raise ValidationError('昵称重复！')