# pyecharts integration with Flask

## Step 0: let's create a mini flask project

Please create new directory for the new project

```shell
$ make flask-echarts
$ cd flask-echarts
$ mkdir templates
```

## Step 1: provide your own template

Please save the following template as pyecharts.html in `templates` folder

```html
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

## Step 2: render your chart using chart_instance.render_embed()

Please save the following python file as server.py under your project root directory.

```python
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('pyecharts.html', myechart=scatter3d())


def scatter3d():
    from pyecharts import Scatter3D

    import random
    data = [[random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)] for _ in range(80)]
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
                   '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    scatter3D = Scatter3D("3D scattering plot demo", width=1200, height=600)
    scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
    return scatter3D.render_embed()
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
