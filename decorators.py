# -*- coding: utf-8 -*-
"""
    decorators.py
    装饰器相关文件
"""
from functools import wraps
from flask import session, redirect, url_for


def login_required(func):
    """
    定义一个装饰器，进行登录校验
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))

    return wrapper
