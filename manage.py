# -*- coding: utf-8 -*-
"""
    manage.py
    存放外部的脚本信息
"""
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.app import app
from exts import db
from app.models.models import User, Question

manager = Manager(app)

# 使用Migrate绑定app和db
migrate = Migrate(app, db)

# 添加迁移脚本的命令到manager中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
