# coding=utf-8
from ...charts.chart import Chart3D
from ...commons.types import Union
from ...options import InitOpts


class Bar3D(Chart3D):
    """
    <<< 3D 柱状图 >>>
    """

    def __init__(self, init_opts: Union[InitOpts, dict] = InitOpts()):
        super().__init__(init_opts)
        self._3d_chart_type = "bar3D"

    # def add(self, name, x_axis, y_axis, data, grid3d_opacity=1, grid3d_shading="color"):
    #     super().add(
    #         name,
    #         data,
    #         opacity=grid3d_opacity,
    #         shading=grid3d_shading,
    #         xaxis3d="category",
    #         yaxis3d="category",
    #         zaxis3d="value",
    #     )
    #
    #     self.options.get("xAxis3D").update(data=x_axis)
    #     self.options.get("yAxis3D").update(data=y_axis)
