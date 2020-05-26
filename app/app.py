# -*- coding: utf-8 -*-

"""
    app.py
"""
from flask import Flask, render_template, url_for, request, redirect, session
import config
from exts import db
from app.models.models import User, Question
from decorators import login_required

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route("/")
def index():
    contents = {
        # 倒序
        'questions': Question.query.order_by(Question.createtime.desc()).all()
    }
    return render_template('index.html', **contents)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        mobile = request.form.get('mobile')
        password = request.form.get('password')
        user = User.query.filter(User.mobile == mobile, User.password == password).first()
        if user:
            session['user_id'] = user.id
            # 设置session的有效期为31天
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return u'手机号码或者密码错误'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        mobile = request.form.get('mobile')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # 验证手机号码是否已经注册
        user = User.query.filter(User.mobile == mobile).first()
        if user:
            return u"当前手机号码已经被注册"
        else:
            # 两次密码是否相等
            if password1 != password2:
                return u"两次密码不相同，请核对后再填写"
            else:
                user = User(mobile=mobile, username=username, password=password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))


@app.route('/logout', methods=['GET'])
def logout():
    # del session['user_id']
    # session.pop('user_id')
    session.clear()
    return redirect(url_for('login'))


@app.route('/question', methods=['GET', 'POST'])
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        title = request.form.get('title')
        content = request.form.get('content')
        question = Question(title=title, content=content)
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        question.author = user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))


@app.context_processor
def my_content_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}


if __name__ == '__main__':
    app.run()
