# coding=utf-8

from pyecharts.chart import Chart3D


class Line3D(Chart3D):
    """
    <<< 3D 折线图 >>>
    """

    def __init__(self, *args, **kwargs):
        super(Line3D, self).__init__(*args, **kwargs)
        self._3d_chart_type = "line3D"
