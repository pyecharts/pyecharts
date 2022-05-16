from pyecharts.charts import MapGlobe, Geo

from ... import options as opts
from ... import types
from ...options import InitOpts

class  MapGlobe3D(Geo, MapGlobe):
    '''
        Globe 3D Map 
    '''
    def __init__(self, init_opts: types.Init = InitOpts()):
        super().__init__(init_opts)
        self._3d_chart_type = "MapGlobe3D"
