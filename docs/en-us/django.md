# pyecharts integration with django

We are following the official django [tutorials](https://docs.djangoproject.com/en/1.11/intro/tutorial01/) here. We expect you are familar with django and have
gone through the tutorial at least.


## Step 0: Let's create a virtual environment and install pyecharts

```shell
$ virtualenv --no-site-packages pyecharts-env
$ source pyecharts-env/bin/activate
$ pip install django==1.11.4
$ pip install pyecharts
```

Although current dependencies of pyecharts include django, the tutorial is written on top django version **1.11.4**.


## Step 1: create a mini django site and the actual visualization app

```shell
$ django-admin startproject myechartsite
```

And start an app

```shell
$ python manage.py startapp myfirstvis
$ ls
db.sqlite3      manage.py       myechartsite    myfirstvis
```

Then register the app in `myechartsite/settings.py`:

```
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

And then let's create the urls.py which provides the url route to the request handler.
And we will create the request handler views.py in step 3.

```python
myfirstvis/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```

And insert the 'myfirstvis.urls' into `myechartsite/urls.py`

```python
myechartsite/urls.py
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^myfirstvis/', include('myfirstvis.urls'))  # <---
]
```

## Step 2: Now let's write up the view function

Then copy the following code and save as `myfirstvis/views.py` 


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

`script_list` is a list of echarts libraries that are required for the chart rendering on the page.
The number of libraries varies according to the dependency requirements of the charts
to be rendered.

`host` refers to the host for echarts libraries. The default host is
http://chfw.github.io/jupyter-echarts/echarts. You can change them if you wish. And if you do so,
please clone https://github.com/chfw/jupyter-echarts. Then, place `echarts` folder onto your own server.


## Step 3: Now let's create a template

Previous steps follow the [tutorial part 1](https://docs.djangoproject.com/en/1.11/intro/tutorial01/). Now let's jump to [tutorial part 3](https://docs.djangoproject.com/en/1.11/intro/tutorial03/).

Please create a templates directory and save the following file into it.

```shell
$ mkdir templates/myfirstvis -p
```

Please note the absolute path is: `<project root>/myfirstvis/templates/myfirstvis`. Here
is the template file.


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

## Step 4: Run it

Then let's bring up the django site:

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

Please visit http://localhost:8000/myfirstvis/ for your first visualization via pyecharts. Here is your first 3D visualization:

![django-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/django-0.gif)


## Conclusion

As you can see, it is just a few steps to create a visual charts using pyecharts. Django tutorials has 7 parts and we only need 1st and 3rd parts to
make the visualisation.

For your reference, please find the example code in `pyecharts/document` folder.