#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Parallel


def test_parallel_line_style():
    schema = ["data", "AQI", "PM2.5", "PM10", "CO", "NO2"]
    data = [[1, 91, 45, 125, 0.82, 34]]
    parallel = Parallel()
    parallel.config(schema)
    parallel.add("parallel", data, line_width=20, line_opacity=0.5)
    html_content = parallel._repr_html_()
    assert '"width": 20' in html_content
    assert '"opacity": 0.5' in html_content
