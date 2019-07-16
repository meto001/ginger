# _*_ coding:utf-8 _*_

from app.libs.redprint import Redprint

__author__ = 'meto'
__date__ = '2019/7/8 17:33'

api = Redprint('user')


@api.route('/get')
def get_user():
    return 'i am meto'


@api.route('/create')
def create_user():
    return 'create user'
