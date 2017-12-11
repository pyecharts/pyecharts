> 阅读指引：
>
> 1. 本文所述的整合方式适用于 V0.3.0 及其以上的版本。
> 2. 本文不是一个教程性质的文档，仅描述关键步骤和原理文档。因此在阅读之前，你应当对相关的 web 框架有所了解或者参考示例项目。

pyecharts 现在和 web 框架的整合工作变得十分容易，无论你是刚开始开发 web 项目还是整合已有的项目。这主要得益于 python 语言的灵活性和面向对象特点，使得整合工作不会破坏原有的功能和代码层次结构。

pyecharts 已经开放内部的 jinja2 模板引擎相关接口，因此从理论上来说，pyecharts 能够胜任那些使用 jinja2 模板引擎的 web 框架。

整合工作依据不同的框架和使用场景有不同的具体方法。本文将以 Django 和 Flask 这两个主流框架描述不同方式的整合过程，其他 web 框架可以以此为参考。

## Flask

### 自定义模板引擎

Flask 默认采用 jinja2 作为其模板引擎。根据 Flask 文档，可以在 `Flask.jinja_environment` ，指定自己实现的模板引擎类，以实现特定功能。

在 Flask 中可按下列步骤实现自己的模板引擎类：

- 创建一个继承自 `flask.templating.Environment` 的模板引擎类`FlaskEchartsEnvironment` 。
- 在构造函数 `__init__` 中，为该类添加 `pyecharts_config` 属性， 添加模板函数到全局字典中。
- 在自己的 Flask 应用类中指定 `FlaskEchartsEnvironment` 为默认模板引擎。

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

### 模板函数

在模板文件中可以使用 `echarts_*` 系列模板函数。

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

上述例子使用 boot CDN 的 js 文件，因此在最后生成 HTML 文件代码时，使用了下面的外链形式。不过需要注意的是，最好请确保你挂载的的服务器有 pyecharts 所需要的所有 js 文件，如对应的地图，3D 图等的 js 文件，这些文件均在 pyecharts/template/js 文件夹里面。

```html
<script type="text/javascript" src=https://cdn.bootcss.com/echarts/3.7.2/echarts.min.js""></script>
```

使用外链形式优点在于：

- 减少最后生成文件大小
- 更容易与 web 框架整合，便于大型项目开发

### 示例项目

示例项目可参考 [Flask_demo](https://github.com/kinegratii/flask_demo)， 该项目完全使用本地 echarts 文件。可基于该项目继续开发。

## Django 

### 自定义模板引擎

自 v1.8 起，Django 支持多模板引擎，内置了对 Jinja2 的支持。pyecharts 内部也是使用 Jinja2 作为其默认的模板引擎。因此二者的整合是非常简单的。

首先，需要实现一个返回一个 `jinja2.Environment` 对象的回调函数。下面是仿造 [官方例子](https://docs.djangoproject.com/en/1.11/topics/templates/#django.template.backends.jinja2.Jinja2) 实现的一个例子：

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

其余按照 Django 文档配置 `settings.TEMPLATES` 等变量值。

## 总结

在整合过程中，主要有两种方式实现自己的模板引擎类：

- 直接继承 `pyecharts.engine.BaseEnvironment` ：如 Django。用于可以直接使用的场景。 
- 手动添加模板函数：如 Flask ，Flask 引擎类`flask.templating.Environment` 重写了 `jinja2.Environment` 相关逻辑，因此应当继承该类，并且手动添加相关模板函数 

## 其他

- 关于 Django 使用了自己的模板引擎，可参考 [django-echarts](https://github.com/kinegratii/django-echarts) 项目。