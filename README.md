## Sivir-Flask

>  这是一个简单的学习Flask的项目，基于`Flask-Web开发：基于Python的Web应用开发实战`这本书而来。

## manager.py的使用
* 为了方便数据库的迁移，以及相关的脚本的处理
* 使用方法
    1. `python manage.py db init`
    2. `python manage.py db migrate`
    3. `python manage.py db upgrade`

## hook函数
1. **before_request**
    * 在请求之前执行
    * 在视图函数执行之前执行
    * 这个也是一个装饰器
2. **content_processor**
    * 上下文处理器应该返回一个字典(哪怕是空也要返回{})，字典中的`key`会被模板当成变量来渲染
    * 上下文处理器返回的字典，在所有的页面中都可以使用

## 保存全局变量g的属性
1. global
2. g对象是专门用来存储用户的数据的
3. g对象在一次请求中的所有代码的地方都可以使用。

## 装饰器
1. 装饰器其实就是一个函数
2. 返回值也必须是一个函数
```python
# 自定义一个装饰器
from functools import wraps
def my_log(func):
    # wraps的作用就是装饰器不用修改原始func的__name__等私有属性
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('先执行装饰器....')
        func(*args,**kwargs)
    return wrapper

@my_log
def run():
    print('Running Man......')

@my_log
def statis(a,b):
    c = a+b
    print('结果为%s',c)
    
```

