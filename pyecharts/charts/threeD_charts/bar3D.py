from ...charts.chart import Chart3D
from ...commons.types import Union
from ...options import InitOpts


class Bar3D(Chart3D):
    """
    <<< 3D Bar-Chart >>>
    """

    def __init__(self, init_opts: Union[InitOpts, dict] = InitOpts()):
        super().__init__(init_opts)
        self._3d_chart_type = "bar3D"
