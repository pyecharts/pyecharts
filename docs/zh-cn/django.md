> 本指南按照 Django [官方教程](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)，通过完成一个 Django 小项目来说明如何在 Django 中使用 pyecharts。如果对 Django 还不太熟悉的开发者，可仔细阅读官方提供的最新文档。


## Step 0: 使用新的 virtualenv 环境
建议开发者使用 1.11.4 版本的 Django

```shell
$ virtualenv --no-site-packages pyecharts-env
$ source pyecharts-env/bin/activate
$ pip install django==1.11.4
$ pip install pyecharts
```


## Step 1: 新建一个 django 项目

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


## Step 2: 处理视图功能部分

将下列代码保存到 `myfirstvis/views.py` 中。

```python
from __future__ import unicode_literals
import math

from django.http import HttpResponse
from django.template import loader
from pyecharts import Line3D


REMOTE_HOST = "https://pyecharts.github.io/assets/js"


def index(request):
    template = loader.get_template('myfirstvis/pyecharts.html')
    l3d = line3d()
    context = dict(
        myechart=l3d.render_embed(),
        host=REMOTE_HOST,
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

`host` 是 echarts js 库的地址，默认提供的地址为 https://pyecharts.github.io/assets/js 当然，如果你愿意你也可以改变这个地址，先克隆 https://github.com/pyecharts/assets 然后将 `js` 文件夹挂载在你自己的服务器上即可。



## Step 3: 为项目提供自己的模板

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


```
<!-- myfirstvis/templates/pyecharts.html -->
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>Proudly presented by PycCharts</title>
	{% for jsfile_name in script_list %}
        <script src="{{ host }}/{{ jsfile_name }}.js"></script>
    {% endfor %}
</head>

<body>
  { {myechart|safe }}
</body>

</html>
```


## Step 4: 运行项目

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

![django-0](https://user-images.githubusercontent.com/19553554/35081440-21efcf58-fc4f-11e7-8427-ed73306533e8.gif)


## 小结

看到了吧，只需要简单的几步就可以使用 pyecharts 创建可视化的图表。Django 官方教程需要七步的这里我们三步就搞定了。

具体文档可以参考 pyecharts/docs 文件夹。
