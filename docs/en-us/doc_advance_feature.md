# pyecharts document - Advance Uage 

This artile describe some new features in V0.3.0.

- Custom Template File
- How to Reference the Javascript file.

## Python Script

### Way I

A chart render proccess can be described as the following table.

| Step                        | Simple Code                              | remark |
| --------------------------- | ---------------------------------------- | ------ |
| 1 Create chart instance     | `bar = Bar()`                            |        |
| 2 Add the data              | `bar.add(**kwargs)`                      |        |
| 3 Create config instance    | `config = PyEchartsConfig(**kwargs)`     |        |
| 4 Build the template engine | `engine = EchartsEnvironment(pyecharts_config=config)` |        |
| 5 Load template file        | `tpl = engine.get_template('demo_tpl.html')` |        |
| 6 Render                    | `html = tpl.render(bar=bar)`             |        |
| 7 Write to target file      | `write_utf8_html_file('my_demo_chart.html', html)` |        |

### Way II

You can also use `render` method of chart class, with is the shortcut of way I.

Step 1:Use `pyecharts.configure` or `pyecharts.online` to config items.

```python
configure(jshost=None, echarts_template_dir=None, force_js_embed=None, **kwargs)
```

Step 2: Call the `render` method to generate HTML file.

the method sigin for simple chart:

```python
Chart.render(path='render.html', template_name='simple_chart.html', object_name='chart', extra_context=None)
```

the method sigin for page:

```python
Page.render(path='render.html', template='simple_page.html', object='page', extra_context=None)
```

Each parameter marod

- path ：the file name of target HTML file.
- template_name: the file name of template.
- object_name: the variable name of chart in the template file.
- extra_context: the exra data dictionary.

## Jupyter Notebook 

Chart class implement  `_repr_html_` interface，You can directly call the instance to show the chart in a cell.



## Flask 

It is easy to integrate pyechart and Flask.This is a example.

Step 1: Create server code.

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

Step 2:Create template file.

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

In the example,the js file of boot CDN is used, so the following code fragment is generate.

The advance of using external link are listed as following:

- Descrease the file size of HTML file
- More easy to integrate with web framework

## Django

Django use its own template engine, see the project  [django-echarts](https://github.com/kinegratii/django-echarts) for more detail.