from ... import options as opts
from ... import types
from ...charts.chart import Chart3D
from ...globals import ChartType
from ...options import InitOpts, RenderOpts


class GraphGL(Chart3D):
    """
    <<< GraphGL Relational graphs using WebGL to support the layout and
    drawing of large-scale network/relational data. >>>
    """

    def __init__(
        self,
        init_opts: types.Init = InitOpts(),
        render_opts: types.RenderInit = RenderOpts(),
    ):
        super().__init__(init_opts, render_opts)
        self._3d_chart_type = ChartType.GRAPHGL

    def add(
        self,
        series_name: str,
        nodes: types.Sequence[types.GraphGLNode],
        links: types.Sequence[types.GraphGLLink],
        *,
        layout: str = "forceAtlas2",
        force_atlas2_opts: types.GraphGLForceAtlas2 = None,
        symbol: types.Optional[str] = "circle",
        symbol_size: types.Numeric = 5,
        itemstyle_opts: types.ItemStyle = None,
        linestyle_opts: types.LineStyle = opts.LineStyleOpts(),
        z_level: types.Numeric = 10,
    ):
        self.options.get("series").append(
            {
                "type": ChartType.GRAPHGL,
                "name": series_name,
                "layout": layout,
                "forceAtlas2": force_atlas2_opts,
                "nodes": nodes,
                "links": links,
                "symbol": symbol,
                "symbolSize": symbol_size,
                "itemStyle": itemstyle_opts,
                "lineStyle": linestyle_opts,
                "zlevel": z_level,
            }
        )
        return self
