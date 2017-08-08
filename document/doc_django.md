# pyecharts integration with django

We are following the official django [tutorials](https://docs.djangoproject.com/en/1.11/intro/tutorial01/) here. We expect you are familar with django and have
gone through the tutorial at least.


## Step 0: Let's create a virtual environment and install pyecharts

```shell
$ virtualenv --no-site-packages pyecharts-env
$ source pyecharts-env/bin/activate
$ pip install django=1.11.4
$ pip install pyecharts
```

Although current dependencies of pyecharts include django, the tutorial is written on top django version 1.11.4.

## Step 1: create a mini django site and the actual visualization app

```shell
$ djangoadmin startproject myechartsite
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
And we will create the request handler views.py in next step

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


## Step 2: Now let's create a template

Previous steps follow the [tutorial part 1]([tutorials](https://docs.djangoproject.com/en/1.11/intro/tutorial01/). Now let's jump to [tutorial part 3](https://docs.djangoproject.com/en/1.11/intro/tutorial03/).

Please create a templates directory and save the following file into it.

```shell
$ mkdir templates/myfirstvis -p
```

Please note the absolute path is: `<project root>/myfirstvis/templates/myfirstvis`. Here
is the template file.


```html
<!-- myfirstvis/templates/myfirstvis/pyecharts.html -->
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>ECharts</title>
    <script src="http://oog4yfyu0.bkt.clouddn.com/echarts.min.js"></script>
    <script src="http://oog4yfyu0.bkt.clouddn.com/echarts-gl.js"></script>
    <script type="text/javascript " src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/china.js"></script>
    <script type="text/javascript " src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/world.js"></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/wordcloud.js"></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/anhui.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/aomen.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/beijing.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/chongqing.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/fujian.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/gansu.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/guangdong.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/guangxi.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/guizhou.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/hainan.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/hebei.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/heilongjiang.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/henan.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/hubei.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/hunan.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/jiangsu.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/jiangxi.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/jilin.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/liaoning.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/neimenggu.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/ningxia.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/qinghai.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/shangdong.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/shanghai.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/shanxi.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/sichuan.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/taiwan.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/tianjin.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/xianggang.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/xinjiang.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/xizang.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/yunnan.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/zhejiang.js "></script>
</head>

<body>
  {{myechart|safe}}
</body>

</html>
```

Then copy the following code and save as `myfirstvis/views.py` 


```python
#myfirstvis/views.py
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('myfirstvis/pyecharts.html')
	context = {
	    "myechart": line3d()
	}
    return HttpResponse(template.render(context, request))


def line3d():
    from pyecharts import Line3D
    
    import math
    _data = []
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        _data.append([x, y, z])
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
                   '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    line3d = Line3D("3D 折线图示例", width=1200, height=600)
    line3d.add("", _data, is_visualmap=True, visual_range_color=range_color, visual_range=[0, 30],
               is_grid3D_rotate=True, grid3D_rotate_speed=180)
	return line3d.render_embed()
```

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

Please visit http://localhost:8000/myfirstvis/ for your first visualization via pyecharts.


## Conclusion

As you can see, it is just a few steps to create a visual charts using pyecharts. Django tutorials has 7 parts and we only need 1st and 3rd parts to
make the visualisation.

For your reference, please find the example code in `pyecharts/document` folder.