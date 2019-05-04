from ... import options as opts
from ...charts.basic_charts.geo import GeoChartBase
from ...commons.types import Optional, Sequence, Union

BAIDU_MAP_API = "http://api.map.baidu.com/api?v=2.0&ak={}"
BAIDU_MAP_GETSCRIPT = "http://api.map.baidu.com/getscript?v=2.0&ak={}"


class BMap(GeoChartBase):
    """
    <<< Baidu coordinate system >>>
    Support scatter plot, line
    """

    def __init__(self, init_opts: Union[opts.InitOpts, dict] = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self.js_dependencies.add("bmap")
        self._is_geo_chart = True
        self._coordinate_system: Optional[str] = "bmap"

    def add_schema(
        self,
        baidu_ak: str,
        center: Sequence,
        zoom: Optional[int] = None,
        is_roam: bool = True,
        map_style: Optional[dict] = None,
    ):
        self.js_dependencies.add(
            BAIDU_MAP_API.format(baidu_ak), BAIDU_MAP_GETSCRIPT.format(baidu_ak)
        )
        self.options.update(
            bmap={
                "center": center,
                "zoom": zoom,
                "roam": is_roam,
                "mapStyle": map_style,
            }
        )
        return self
