# coding=utf8
"""
Migrate pyecharts and Flask with custom template functions.
"""
from __future__ import unicode_literals

import random
import datetime

from flask import Flask, render_template

from pyecharts import HeatMap
from pyecharts.engine import EchartsEnvironment
from pyecharts.conf import PyEchartsConfig


# ----- Adapter ---------
class FlaskEchartsEnvironment(EchartsEnvironment):
    def __init__(self, app, **kwargs):
        EchartsEnvironment.__init__(self, **kwargs)
        self.app = app


# ---User Code ----

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
