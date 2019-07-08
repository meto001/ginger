# _*_ coding:utf-8 _*_

from app.libs.redprint import Redprint

__author__ = 'meto'
__date__ = '2019/7/8 17:33'

api = Redprint('book')


@api.route('/get')
def get_book():
    return 'get book'


@api.route('/create')
def create_book():
    return 'create book'
