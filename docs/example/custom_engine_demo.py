# coding=utf8

from __future__ import unicode_literals

from jinja2 import FileSystemLoader
from pyecharts import Bar
from pyecharts.engine import EchartsEnvironment
from pyecharts.utils import write_utf8_html_file

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图数据堆叠示例", jshost='	https://cdn.bootcss.com/echarts/3.6.2')
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True)
env = EchartsEnvironment(loader=FileSystemLoader('my_tpl'))
tpl = env.get_template('tpl_demo.html')
html = tpl.render(bar=bar)
write_utf8_html_file('my_tpl_demo2.html', html)
