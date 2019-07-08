# _*_ coding:utf-8 _*_
from app.app import create_app

__author__ = 'meto'
__date__ = '2019/7/8 17:02'


app = create_app()





if __name__ == '__main__':
    app.run(debug=True)
