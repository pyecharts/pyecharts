# coding=utf8

from __future__ import unicode_literals

from pyecharts import configure, Bar

configure(echarts_template_dir='my_tpl')

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图数据堆叠示例", jshost='	https://cdn.bootcss.com/echarts/3.6.2')
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True)
bar.render(path='my_tpl_demo.html', template_name='tpl_demo.html', object_name='bar')
