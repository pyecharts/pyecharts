# coding=utf-8

from pyecharts.chart import Chart3D


class Surface3D(Chart3D):
    """
    <<< 3D 曲面图 >>>
    """

    def __init__(self, *args, **kwargs):
        super(Surface3D, self).__init__(*args, **kwargs)
        self._3d_chart_type = "surface"
