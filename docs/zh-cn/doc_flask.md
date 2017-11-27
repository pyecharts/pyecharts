# pyecharts + Flask 使用指南
> 本指南会以一个小的 Flask 项目为例，说明如何在 Flask 中使用 pyecharts。请确保你已经安装 Flask，还没安装请执行 ```pip install flask``` 或其他方式安装。

pyecharts 支持在 Flask 框架中使用，支持两种使用方式：

## 第一种方式：直接渲染

直接渲染方式是 V0.2.0 所使用的渲染方式。

### Step 0: 首先新建一个 Flask 项目

* Linux/macos 系统  
```shell
$ mkdir flask-echarts
$ cd flask-echarts
$ mkdir templates
```

* Windows 系统  
  新建一个 flask-echarts 文件夹，在其下新建 templates 子文件夹。

### Step 1: 为项目提供自己的模板

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

### Step 2: 调用 chart_instance.render_embed() 方法渲染图表 

请将下面的代码保存为 server.py 文件并移至项目的根目录下。

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
`script_list` 是 Page() 类渲染网页所需要依赖的 echarts js 库，依赖的库的数量取决于所要渲染的图形种类。

`host` 是 echarts js 库的地址，默认的地址为 http://chfw.github.io/jupyter-echarts/echarts  当然，如果你愿意你也可以改变这个地址，先克隆 https://github.com/chfw/jupyter-echarts  然后将 `echarts` 文件夹挂载在你自己的服务器上即可。

此时 flask-echarts 目录下为
```
├── server.py
└── templates
    └── pyecharts.html
```


### Step 3: 运行项目

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

![flask-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/flask-0.gif)

### 小结

可以看到，在 Flask app 中加入 pyecharts 图表只需要简单的几个步骤而已，欢迎尝试更多的图表类型。具体文档可以参考 ```pyecharts/document```  文件夹。



## 第二种方式：模板函数渲染

自 V0.3.0 起， pyecharts 支持在 Flask 使用 `echarts_*` 系列模板函数。

### 第一步：实现 Flask 应用的自定义模板引擎

主要有三个要点：

- 创建一个继承自 `flask.templating.Environment` 的模板引擎类`FlaskEchartsEnvironment` 。
- 通过使用 `pyecharts.engine.PyEchartsConfigMixin` 提供一个配置对象 。
- 在构造函数 `__init__` 中添加模板函数到全局字典中。

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
```

### 第二步：创建模板文件

在同目录下 templates 文件夹创建 flask_demo.html 文件写入如下的代码。

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

上述例子使用 boot CDN 的 js 文件，因此在最后生成 HTML 文件代码时，使用了下面的外链形式

```html
<script type="text/javascript" src=https://cdn.bootcss.com/echarts/3.7.2/echarts.min.js""></script>
```

使用外链形式优点在于：

- 减少最后生成文件大小
- 更容易与 web 框架整合，便于大型项目开发