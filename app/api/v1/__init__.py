# _*_ coding:utf-8 _*_
from flask import Blueprint

from app.api.v1 import user, book,client

__author__ = 'meto'
__date__ = '2019/7/8 17:32'


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    user.api.register(bp_v1)
    book.api.register(bp_v1)
    client.api.register(bp_v1)
    return bp_v1
