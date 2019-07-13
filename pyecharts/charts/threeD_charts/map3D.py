from ... import types
from ...charts.basic_charts.map import MapMixin
from ...charts.chart import Chart3D
from ...options import InitOpts


class Map3D(Chart3D, MapMixin):
    """
    3D map
    """

    def __init__(self, init_opts: types.Init = InitOpts()):
        super().__init__(init_opts)
        self._3d_chart_type = "map3D"

    def add_schema(self, maptype: str = "china", box_opts: dict = None):
        self.js_dependencies.add(maptype)
        self.options.update(geo3D={"map": maptype})
        return self
