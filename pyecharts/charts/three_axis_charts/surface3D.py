from ... import options as opts
from ... import types
from ...charts.chart import ThreeAxisChart
from ...globals import ChartType
from ...options import InitOpts, RenderOpts


class Surface3D(ThreeAxisChart):
    """
    <<< 3D Surface-Chart >>>
    """

    def __init__(
        self,
        init_opts: types.Init = InitOpts(),
        render_opts: types.RenderInit = RenderOpts(),
    ):
        super().__init__(init_opts, render_opts)
        self._3d_chart_type = ChartType.SURFACE
