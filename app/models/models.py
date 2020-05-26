# -*- coding: utf-8 -*-
"""
    models.py
"""
from exts import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='主键')
    mobile = db.Column(db.String(11), nullable=False, comment='手机号码')
    username = db.Column(db.String(50), nullable=False, comment='用户名')
    password = db.Column(db.String(100), nullable=False, comment='密码')
    createtime = db.Column('create_time', db.DateTime, nullable=True, comment='创建时间')


class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='主键')
    title = db.Column(db.String(200), nullable=False, comment='标题')
    content = db.Column(db.Text, nullable=True, comment="内容")
    create_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 如果是now()的话，是服务器创建的时间，会导致数据都是一样的
    createtime = db.Column('create_time', db.DateTime, nullable=False, comment='创建时间', default=datetime.now)

    author = db.relationship('User', backref=db.backref('questions'))
