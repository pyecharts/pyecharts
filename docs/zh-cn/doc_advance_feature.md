# pyecharts 文档 - 高级使用篇

本文描述了v0.3.0 新引入的特性：

- 自定义模板文件
- 决定 script 标签的引入方式，即 **内嵌** 和 **外链** 两种方式。

V0.3.0 重写了部分底层代码，支持更多使用场景。

## 脚本环境

### 方式一

一个图表的渲染过程可以描述如下，遵循 “先配置，后执行” 的标准流程。

| 步骤       | 简略代码                                     | 备注   |
| -------- | ---------------------------------------- | ---- |
| 1 创建图表实例 | `bar = Bar()`                            |      |
| 2 添加数据   | `bar.add(**kwargs)`                      |      |
| 3 创建配置实例 | `config = PyEchartsConfig(**kwargs)`     |      |
| 4 构建模板引擎 | `engine = EchartsEnvironment(pyecharts_config=config)` |      |
| 5 获取模板文件 | `tpl = engine.get_template('demo_tpl.html')` |      |
| 6 渲染     | `html = tpl.render(bar=bar)`             |      |
| 7 写入目标文件 | `write_utf8_html_file('my_demo_chart.html', html)` |      |

### 方式二

第二种方式是直接使用图表的 `render` 方法，此种方式为第一方式的快捷方式。

第一步使用 `pyecharts.configure` 或者 `pyecharts.online` 进行配置。

```python
configure(jshost=None, echarts_template_dir=None, force_js_embed=None, **kwargs)
```

第二步，调用图表类的函数 `render` 方法，生成 HTML 文件。

单图表 `render` 方法函数签名：

```python
Chart.render(path='render.html', template_name='simple_chart.html', object_name='chart', extra_context=None)
```

多图表 `render` 方法签名：

```python
Page.render(path='render.html', template='simple_page.html', object='page', extra_context=None)
```

各参数意义如下：

- path ：最终生成文件名称
- template_name: 模板文件名称，其目录可通过 `pyecharts.configure()` 全局函数进行配置
- object_name: 模板文件中，该图表类所使用变量的名称
- extra_context 额外数据字典。

## Jupyter Notebook 

pyecharts 的图表类实现了 `_repr_html_` 接口，支持在 Cell 中显示渲染结果，只需直接调用自身实例即可。



## Flask 框架

由于 pyecharts 默认采用 Jinja2 作为模板引擎，因此非常容易与 Flask 进行整合。下面是进行整合的一个例子。

第一步，编写后台代码：

```python
from flask import Flask
from pyecharts.engine import EchartsEnvironment
from pyecharts.conf import PyEchartsConfig

class FlaskEchartsEnvironment(EchartsEnvironment):
    def __init__(self, app, **kwargs):
        EchartsEnvironment.__init__(self, **kwargs)
        self.app = app

class MyFlask(Flask):
    jinja_environment = FlaskEchartsEnvironment
    jinja_options = {'pyecharts_config': PyEchartsConfig(
        jshost='https://cdn.bootcss.com/echarts/3.7.2',
        echarts_template_dir='templates'
    )}
    
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

只需继承 `flask.Flask` 类并指定 `pyecharts.engine.EchartsEnvironment` 为默认的模板渲染引擎。

第二步，编写模板文件：在同目录下  templates 文件夹中。

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

由于上述例子使用 boot CDN 的 js 文件，因此在最后生成 HTML 文件代码时，使用了下面的外链形式

```html
<script type="text/javascript" src=https://cdn.bootcss.com/echarts/3.7.2/echarts.min.js""></script>
```

使用外链形式优点在于：

- 减少最后生成文件大小
- 更容易与 web 框架整合，便于大型项目开发

## Django 框架

Django 使用了自己的模板引擎，可参考 [django-echarts](https://github.com/kinegratii/django-echarts) 项目。