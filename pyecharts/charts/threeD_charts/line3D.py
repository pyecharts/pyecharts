from ... import types
from ...charts.chart import ThreeAxisChart
from ...options import InitOpts


class Line3D(ThreeAxisChart):
    """
    <<< 3D Line-Chart >>>
    """

    def __init__(self, init_opts: types.Init = InitOpts()):
        super().__init__(init_opts)
        self._3d_chart_type = "line3D"
