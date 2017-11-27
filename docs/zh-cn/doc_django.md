# pyecharts + Django 使用指南
> 本指南按照 Django [官方教程](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)，通过完成一个 Django 小项目来说明如何在 Django 中使用 pyecharts。如果对 Django 还不太熟悉的开发者，可仔细阅读官方提供的最新文档。

## 第一种方式：直接渲染

该方法直接使用依赖文件变量和选项文字。


### Step 0: 使用新的 virtualenv 环境
建议开发者使用 1.11.4 版本的 Django

```shell
$ virtualenv --no-site-packages pyecharts-env
$ source pyecharts-env/bin/activate
$ pip install django==1.11.4
$ pip install pyecharts
```


### Step 1: 新建一个 django 项目

```shell
$ django-admin startproject myechartsite
```

创建一个应用程序

```shell
$ python manage.py startapp myfirstvis
$ ls
db.sqlite3      manage.py       myechartsite    myfirstvis
```

在 `myechartsite/settings.py` 中注册应用程序

```python
# myechartsite/settings.py
...
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myfirstvis'  # <---
]
...
```


我们先编辑 urls.py.这文件在 Django 里的功能是把前段的 HTTP 需求和后台服务函数挂钩。在 Step3，我们再引入后端服务函数

```python
# myfirstvis/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```

在 `myechartsite/urls.py` 中新增 'myfirstvis.urls'

```python
myechartsite/urls.py
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'myfirstvis/', include('myfirstvis.urls'))  # <---
]
```


### Step 2: 处理视图功能部分

将下列代码保存到 `myfirstvis/views.py` 中。

```python
from __future__ import unicode_literals
import math

from django.http import HttpResponse
from django.template import loader
from pyecharts import Line3D

from pyecharts.constants import DEFAULT_HOST


def index(request):
    template = loader.get_template('myfirstvis/pyecharts.html')
    l3d = line3d()
    context = dict(
        myechart=l3d.render_embed(),
        host=DEFAULT_HOST,
        script_list=l3d.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))


def line3d():
    _data = []
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        _data.append([x, y, z])
    range_color = [
        '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
        '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    line3d = Line3D("3D line plot demo", width=1200, height=600)
    line3d.add("", _data, is_visualmap=True,
               visual_range_color=range_color, visual_range=[0, 30],
               is_grid3D_rotate=True, grid3D_rotate_speed=180)
    return line3d
```

`script_list` 是 Page() 类渲染网页所需要依赖的 echarts js 库，依赖的库的数量取决于所要渲染的图形种类。

`host` 是 echarts js 库的地址，默认的地址为 http://chfw.github.io/jupyter-echarts/echarts  当然，如果你愿意你也可以改变这个地址，先克隆 https://github.com/chfw/jupyter-echarts  然后将 `echarts` 文件夹挂载在你自己的服务器上即可。


### Step 3: 为项目提供自己的模板

前面的步骤是按照 [tutorial part 1](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)，接下来我们跳到 [tutorial part 3](https://docs.djangoproject.com/en/1.11/intro/tutorial03/)


Linux/macos 系统
```shell
$ mkdir templates/myfirstvis -p
```

Windows 系统  
在 myfirstvis 目录下，新建 templates/myfirstvis 子目录

myfirstvis 目录
```
─ myfirstvis
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   ├── __init__.py
    ├── models.py
    ├── templates
    │   └── myfirstvis
    │       └── pyecharts.html
    ├── tests.py
    ├── urls.py
    └── views.py
```
将下面 html 模板代码保存为 pyecharts.html，请确保 pyecharts.html 文件的绝对路径为 `<project root>/myfirstvis/templates/myfirstvis`


```html
<!-- myfirstvis/templates/pyecharts.html -->
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>Proudly presented by PycCharts</title>
	{% for jsfile_name in script_list %}
    <script src="{{host}}/{{jsfile_name}}.js"></script>
    {% endfor %}
</head>

<body>
  {{myechart|safe}}
</body>

</html>
```


### Step 4: 运行项目

```shell
$ cd myechartsite
$ python manage.py runserver

You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

August 08, 2017 - 05:48:38
Django version 1.11.4, using settings 'myechartsite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

访问 [http://localhost:8000/myfirstvis/](http://localhost:8000/myfirstvis/)，你就可以看到酷炫的 3D 图了

![django-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/django-0.gif)


### 小结

看到了吧，只需要简单的几步就可以使用 pyecharts 创建可视化的图表。Django 官方教程需要七步的这里我们三步就搞定了。

具体文档可以参考 pyecharts/document 文件夹。

## 第二种方式：jinja2模板引擎

> 在使用本方式之前，应当对 Django 多模板引擎有所了解。请选认真阅读相关内容 [Django自定义模板引擎](https://docs.djangoproject.com/en/1.11/topics/templates/#django.template.backends.jinja2.Jinja2)

该方法第一种方式最大的区别有：

- 使用同一的配置，适用于所有的图表对象
- 传给模板页面的是 chart 这个对象，而不再是由其属性(`js_dependencies` 、`options` 等)组成的一个字典。

自 1.8 起，Django 模板支持多引擎，内置了对 Jinja2 的支持。pyecharts 内部也是使用 Jinja2 作为其默认的模板引擎。因此二者的整合是非常简单的。

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

 ## 第三种方式：django自带模板引擎

此种方式请参考项目  [django-echarts](https://github.com/kinegratii/django-echarts) 。