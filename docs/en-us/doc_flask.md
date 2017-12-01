# pyecharts integration with Flask

## Step 0: let's create a mini flask project

Please create new directory for the new project

```shell
$ mkdir flask-echarts
$ cd flask-echarts
$ mkdir templates
```

## Step 1: render your chart using chart_instance.render_embed()

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

## Step 2: provide your own template

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

## Step 3: run it

Now you shall have these:

```shell
$ ls
server.py    templates
$ ls templates
pyecharts.html


```shell
$ pip install flask
$ export FLASK_APP=server.py
$ flask run
* Serving Flask app "server"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Here's what you will get:

![flask-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/flask-0.gif)


## Conclusion

It is extremely simple to include a pyexcharts instance in a Flask app. Please go
ahead and put your own charts in flask.

For your reference, please find the example code in `pyecharts/document` folder.
