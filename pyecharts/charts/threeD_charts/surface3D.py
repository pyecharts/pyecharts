from ... import types
from ...charts.chart import Chart3D
from ...options import InitOpts


class Surface3D(Chart3D):
    """
    <<< 3D Surface-Chart >>>
    """

    def __init__(self, init_opts: types.Init = InitOpts()):
        super().__init__(init_opts)
        self._3d_chart_type = "surface"
