# coding=utf-8

from pyecharts.charts.chart import Chart3D


class Bar3D(Chart3D):
    """
    <<< 3D 柱状图 >>>
    """

    def __init__(self, *args, **kwargs):
        super(Bar3D, self).__init__(*args, **kwargs)
        self._3d_chart_type = "bar3D"

    def add(
        self,
        name,
        x_axis,
        y_axis,
        data,
        grid3d_opacity=1,
        grid3d_shading="color",
        **kwargs
    ):
        super(Bar3D, self).add(
            name,
            data,
            grid3d_opacity=grid3d_opacity,
            grid3d_shading=grid3d_shading,
            xaxis3d_type="category",
            yaxis3d_type="category",
            zaxis3d_type="value",
            **kwargs
        )

        self._option.get("xAxis3D").update(data=x_axis)
        self._option.get("yAxis3D").update(data=y_axis)
