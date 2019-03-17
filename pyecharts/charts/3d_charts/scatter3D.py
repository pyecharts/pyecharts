# coding=utf-8

from ...charts.chart import Chart3D


class Scatter3D(Chart3D):
    """
    <<< 3D 散点图 >>>
    """

    def __init__(self, *args, **kwargs):
        super(Scatter3D, self).__init__(*args, **kwargs)
        self._3d_chart_type = "scatter3D"
