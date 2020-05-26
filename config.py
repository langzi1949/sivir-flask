# -*- coding: utf-8 -*-
"""
    config.py
    项目的配置信息
"""
import os

DEBUG = True

SECRET_KEY = os.urandom(24)

DB_HOSTNAME = ''
DB_PORT = 3306
DB_DATABASE = 'dbw_sivir'
DB_USERNAME = ''
DB_PASSWORD = ''
DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DB_USERNAME, DB_PASSWORD, DB_HOSTNAME, DB_PORT,
                                                              DB_DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URL

SQLALCHEMY_TRACK_MODIFICATIONS = False

