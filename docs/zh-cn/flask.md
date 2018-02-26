> 本指南会以一个小的 Flask 项目为例，说明如何在 Flask 中使用 pyecharts。请确保你已经安装 Flask，还没安装请执行 ```pip install flask``` 或其他方式安装。

## Step 0: 首先新建一个 Flask 项目

* Linux/macos 系统  
```shell
$ mkdir flask-echarts
$ cd flask-echarts
$ mkdir templates
```

* Windows 系统  
新建一个 flask-echarts 文件夹，在其下新建 templates 子文件夹。

## Step 1: 为项目提供自己的模板

将下面 html 模板代码保存为 pyecharts.html 文件并移至上一步新建的 templates 文件夹中。

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>Proudly presented by ECharts</title>
	{% for jsfile_name in script_list %}
        <script src="{{ host }}/{{ jsfile_name }}.js"></script>
    {% endfor %}
</head>

<body>
  {{ myechart|safe }}
</body>

</html>
```

## Step 2: 调用 chart_instance.render_embed() 方法渲染图表 

请将下面的代码保存为 server.py 文件并移至项目的根目录下。

```python
import random

from pyecharts import Scatter3D
from flask import Flask, render_template


app = Flask(__name__)


REMOTE_HOST = "https://pyecharts.github.io/assets/js"

@app.route("/")
def hello():
    s3d = scatter3d()
    return render_template('pyecharts.html',
                           myechart=s3d.render_embed(),
                           host=REMOTE_HOST,
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
`script_list` 是 Page() 类渲染网页所需要依赖的 echarts js 库，依赖的库的数量取决于所要渲染的图形种类。


`host` 是 echarts js 库的地址，默提供的地址为 https://pyecharts.github.io/assets/js  当然，如果你愿意你也可以改变这个地址，先克隆 https://github.com/pyecharts/assets 然后将 `js` 文件夹挂载在你自己的服务器上即可。

此时 flask-echarts 目录下为
```
├── server.py
└── templates
    └── pyecharts.html
```


## Step 3: 运行项目

Linux/macos 系统
```shell
$ export FLASK_APP=server.py
$ flask run
* Serving Flask app "server"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Windows 系统
```shell
$ set FLASK_APP=server.py
$ flask run
* Serving Flask app "server"
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

效果

![flask-0](https://user-images.githubusercontent.com/19553554/35081158-3faa7c34-fc4d-11e7-80c9-2de79371374f.gif)

## 模板扩展

这里对模板进行一些说明，实际上 {{ myechart|safe }} 封装的是

```html
<div id="{{ chart_id }}" style="width:{{ my_width }}px;height:{{ my_height }}px;"></div>
<script type="text/javascript">
    var myChart_{{ chart_id }} = echarts.init(document.getElementById('{{ chart_id }}'));
    var option_{{ chart_id }} = {{ my_option|safe }};
    myChart_{{ chart_id }}.setOption(option_{{ chart_id }});
</script>
```

所以实际组合起来的模板是这样的

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>Proudly presented by ECharts</title>
	{% for jsfile_name in script_list %}
        <script src="{{ host }}/{{ jsfile_name }}.js"></script>
    {% endfor %}
</head>

<body>
  <div id="{{ chart_id }}" style="width:{{ my_width }}px;height:{{ my_height }}px;"></div>
    <script type="text/javascript">
        var myChart_{{ chart_id }} = echarts.init(document.getElementById('{{ chart_id }}'));
        var option_{{ chart_id }} = {{ my_option|safe }};
        myChart_{{ chart_id }}.setOption(option_{{ chart_id }});
    </script>
</body>

</html>
```

有需要的开发者可以对模板进行更改，这里演示如何使 pyecharts 生成的图可自适应宽度，利用 `resize` 方法。模板修改为如下所示

```html
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>Proudly presented by ECharts</title>
	{% for jsfile_name in script_list %}
        <script src="{{ host }}/{{ jsfile_name }}.js"></script>
    {% endfor %}
</head>

<body>
  <div id="{{ chart_id }}" style="width:{{ my_width }};height:{{ my_height }}px;"></div>
    <script type="text/javascript">
        window.onload = function() {
			setTimeout(function() {
				var myChart_{{ chart_id }} = echarts.init(document.getElementById('{{ chart_id }}'));
				var option_{{ chart_id }} = {{ my_option|safe }};
				myChart_{{ chart_id }}.setOption(option_{{ chart_id }});
				window.onresize = function() {
					myChart_{{ chart_id }}.resize();
				};
			}, 1000);
		};
    </script>
</body>

</html>
```

代码修改为如下所示

```python
from pyecharts import Bar
from pyecharts.utils import json_dumps
from flask import Flask, render_template


REMOTE_HOST = "https://pyecharts.github.io/assets/js"

app = Flask(__name__)


@app.route("/")
def hello():
    _bar = bar_chart()
    return render_template('pyecharts.html',
                           chart_id=_bar.chart_id,
                           host=REMOTE_HOST,
                           my_width="100%",
                           my_height=600,
                           my_option=json_dumps(_bar.options),
                           script_list=_bar.get_js_dependencies())


def bar_chart():
    bar = Bar("我的第一个图表", "这里是副标题")
    bar.add("服装",
            ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
            [5, 20, 36, 10, 75, 90])
    return bar

```

效果

![flask-1](https://user-images.githubusercontent.com/19553554/35081437-1f42073a-fc4f-11e7-8479-ca2a0581d966.gif)
## 小结

可以看到，在 Flask app 中加入 pyecharts 图表只需要简单的几个步骤而已，欢迎尝试更多的图表类型。具体文档可以参考 ```pyecharts/docs```  文件夹。
