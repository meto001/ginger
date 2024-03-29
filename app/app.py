# _*_ coding:utf-8 _*_
from flask import Flask

__author__ = 'meto'
__date__ = '2019/7/8 17:03'


def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')

def register_pulgin(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    # 注册蓝图
    register_blueprints(app)
    register_pulgin(app)
    return app
