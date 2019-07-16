# _*_ coding:utf-8 _*_

from app.libs.redprint import Redprint

__author__ = 'meto'
__date__ = '2019/7/8 17:33'

api = Redprint('book')


@api.route('/',methods=['GET'])
def get_book():
    return 'get book'


@api.route('/',methods=['POST'])
def create_book():
    return 'create book'
