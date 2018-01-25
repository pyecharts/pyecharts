# pyecharts document - Web Integration 

> Before You Read
>
> 1. This web integration requires pyecharts V0.3.0+.
> 2. This article is principle-described instead of a tutorial.So you should learn a lot about the  relevant web framework.

Now, it is more easy to integrate pyecharts with your web framework ,whatever you start a project or integrate a exist one.The integration will not break down origin features because of the flexibility and OOP in Python language.

pyecharts exposes the API of builtin jinja2 template engine.In theory, it is easy to integrate the web framework which use jinja2 template engine.

In different use case,different specific methods and procedures will be used. This arctile will use the common framework,Django and Flask to describe the procedures ,which other framework can be inspired from.

## Flask

### Custom Template Engine

pyecharts use jinja2 as its template engine.According to Flask document.It is easy to integrate pyechart and Flask.This is a example.

You can follow these steps to create custom template engine.

- In the constructor `__init__` , addd attribute `pyecharts_config` and add template functions.
- Assign this class to your Flask app class.

```python
from flask import Flask, render_template
from flask.templating import Environment

from pyecharts import HeatMap
from pyecharts.engine import ECHAERTS_TEMPLATE_FUNCTIONS
from pyecharts.conf import PyEchartsConfig

class FlaskEchartsEnvironment(Environment):
    def __init__(self, *args, **kwargs):
        super(FlaskEchartsEnvironment, self).__init__(*args, **kwargs)
        self.pyecharts_config = PyEchartsConfig(jshost='https://cdn.bootcss.com/echarts/3.7.2')
        self.globals.update(ECHAERTS_TEMPLATE_FUNCTIONS)

class MyFlask(Flask):
    jinja_environment = FlaskEchartsEnvironment

app = MyFlask(__name__)
```

### Template Function

You can use `echarts_*` template function in the template file.

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>自定义模板</title>
    {{ echarts_js_dependencies(hm) }}
</head>
<body>
    <p>在 Flask 下使用 echarts_* 系列模板函数(Template Functions)渲染页面。</p>
    {{ echarts_container(hm) }}
    {{ echarts_js_content(hm) }}
</body>
</html>
```

In the demo, boo CDN js is used, so the output `<script>` will use external link to reference the js files.\

```html
<script type="text/javascript" src=https://cdn.bootcss.com/echarts/3.7.2/echarts.min.js""></script>
```

### Example Project

The github repositoriy [Flask_demo](https://github.com/kinegratii/flask_demo) is a more complete example, which use local echarts library javascript files.You can continue development based on this project.

## Django 

### Custom Template Engine

From v1.8, you can directly use jinja2 as template engine in Django.

In the integration,you should define a callable function which returns a  `jinja2.Environment`  object.This is a example following  [Django Document](https://docs.djangoproject.com/en/1.11/topics/templates/#django.template.backends.jinja2.Jinja2) :

```python
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

from pyecharts.conf import PyEchartsConfig
from pyecharts.engine import BaseEnvironment


def environment(**options):
    env = BaseEnvironment(pyecharts_config=PyEchartsConfig(jshost='/static/'), **options)
    # Add template functions to the environment object
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env

```

See more detail at Django document.

## Summary

You can has two way to create your own engine class.

- Inherit  `pyecharts.engine.BaseEnvironment` :e.g Django. Used for用于可以直接使用的场景。 
- Add template function:e.g Flask, The class `flask.templating.Environment` overwrites some features from `jinja2.Environment` .So you should inherit this class,and add template function handly.

## More

- If you use Django's default template engine, see the project [django-echarts](https://github.com/kinegratii/django-echarts)  for more detail.

