# pyecharts integration with Flask

## Way I:Directly Render

### Step 0: let's create a mini flask project

Please create new directory for the new project

```shell
$ mkdir flask-echarts
$ cd flask-echarts
$ mkdir templates
```

### Step 1: render your chart using chart_instance.render_embed()

Please save the following python file as server.py under your project root directory.

```python
import random
from pyecharts import Scatter3D
from pyecharts.constants import DEFAULT_HOST
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def hello():
    s3d = scatter3d()
    return render_template('pyecharts.html',
                           myechart=s3d.render_embed(),
                           host=DEFAULT_HOST,
                           script_list=s3d.get_js_dependencies())


def scatter3d():
    data = [generate_3d_random_point() for _ in range(80)]
    range_color = [
        '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
        '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    scatter3D = Scatter3D("3D scattering plot demo", width=1200, height=600)
    scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
    return scatter3D


def generate_3d_random_point():
    return [random.randint(0, 100),
            random.randint(0, 100),
            random.randint(0, 100)]
```

`script_list` is a list of echarts libraries that are required for the chart rendering on the page.
The number of libraries varies according to the dependency requirements of the charts
to be rendered.

`host` refers to the host for echarts libraries. The default host is
http://chfw.github.io/jupyter-echarts/echarts. You can change them if you wish. And if you do so,
please clone https://github.com/chfw/jupyter-echarts. Then, place `echarts` folder onto your own server.

### Step 2: provide your own template

Please save the following template as pyecharts.html in `templates` folder

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>Proudly presented by ECharts</title>
	{% for jsfile_name in script_list %}
    <script src="{{host}}/{{jsfile_name}}.js"></script>
    {% endfor %}
</head>

<body>
  {{myechart|safe}}
</body>

</html>
```

### Step 3: run it

Now you shall have these:

```shell
$ ls
server.py    templates
$ ls templates
pyecharts.html


​```shell
$ pip install flask
$ export FLASK_APP=server.py
$ flask run
* Serving Flask app "server"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Here's what you will get:

![flask-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/flask-0.gif)


### Conclusion

It is extremely simple to include a pyexcharts instance in a Flask app. Please go
ahead and put your own charts in flask.

For your reference, please find the example code in `pyecharts/document` folder.



## Way II :Render Using Template Functions

From V0.3.0, pyecharts is support to use `echarts_*`  template functions in Flask web framework.

### Step 0：Implement Custom Template Engine

There are three key points:

- Create a class named  `FlaskEchartsEnvironment`  implement `flask.templating.Environment` .
- Assign a config  using  `pyecharts.engine.PyEchartsConfigMixin` .
- Add temlate functions to the environment object in the method  `__init__` .
- Se\pecified your custom Environment as Flask app instance's engine.

```python
from flask import Flask, render_template
from flask.templating import Environment

from pyecharts import HeatMap
from pyecharts.engine import PyEchartsConfigMixin, ECHAERTS_TEMPLATE_FUNCTIONS
from pyecharts.conf import PyEchartsConfig

class FlaskEchartsEnvironment(Environment, PyEchartsConfigMixin):
    pyecharts_config = PyEchartsConfig(
        jshost='https://cdn.bootcss.com/echarts/3.7.2'
    )

    def __init__(self, *args, **kwargs):
        super(FlaskEchartsEnvironment, self).__init__(*args, **kwargs)
        self.globals.update(ECHAERTS_TEMPLATE_FUNCTIONS)

class MyFlask(Flask):
    jinja_environment = FlaskEchartsEnvironment


app = MyFlask(__name__)

@app.route("/")
def hello():
    hm = create_heatmap()
    return render_template('flask_tpl.html', hm=hm)


def create_heatmap():
    begin = datetime.date(2017, 1, 1)
    end = datetime.date(2017, 12, 31)
    data = [[str(begin + datetime.timedelta(days=i)),
             random.randint(1000, 25000)] for i in
            range((end - begin).days + 1)]
    heatmap = HeatMap("日历热力图示例", "某人 2017 年微信步数情况", width=1100)
    heatmap.add("", data, is_calendar_heatmap=True,
                visual_text_color='#000', visual_range_text=['', ''],
                visual_range=[1000, 25000], calendar_cell_size=['auto', 30],
                is_visualmap=True, calendar_date_range="2017",
                visual_orient="horizontal", visual_pos="center",
                visual_top="80%", is_piecewise=True)
    return heatmap

app.run(port=10200)
```

**NOTE: The view function `render_template` pass the chart instance to the template ,instead of their attributes,which is the main different from to Way I.**

### Step 1：Create Template File

Create flask_demo.html in the same dir templates.

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

The boot CDN is used for js file in the above example,so the end html file generates the following code fragment.

```html
<script type="text/javascript" src=https://cdn.bootcss.com/echarts/3.7.2/echarts.min.js""></script>
```

使用外链形式优点在于：

* Decrease the size of the template file.
* It is more easily to integrate with web framework.

### Step 2: Run

The run steps is the same as the way I.