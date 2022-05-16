from pyecharts.charts import MapGlobe, Map3D, Geo
from pyecharts import types
from pyecharts.options import InitOpts

class  MapGlobe3D(Geo, MapGlobe):
    def __init__(self, init_opts: types.Init = InitOpts()):
        super().__init__(init_opts)
        self._3d_chart_type = "MapGlobe3D"
