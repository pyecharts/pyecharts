# encoding: utf-8
"""
@file: test_chart_diff.py
@desc:
@author: guozhen3
@time: 2022/1/28
"""
from pyecharts.charts import Line

x_data = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
y_data1 = [140, 232, 101, 264, 90, 340, 250]
y_data2 = [120, 282, 111, 234, 220, 340, 310]

c = (
        Line()
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            series_name="品类 1",
            y_axis=y_data1,
            color='#80FFA5')
            .add_yaxis(
            series_name="品类 2",
            y_axis=y_data2,
            color='#00DDFF')
    )

c.render('rend2.html')