import os

from jinja2 import Environment, FileSystemLoader

from pyecharts.commons.utils import JsCode


class _RenderType:
    CANVAS: str = "canvas"
    SVG: str = "svg"


class _FileType:
    SVG: str = "svg"
    PNG: str = "png"
    JPEG: str = "jpeg"
    HTML: str = "html"


class _SymbolType:
    RECT: str = "rect"
    ROUND_RECT: str = "roundRect"
    TRIANGLE: str = "triangle"
    DIAMOND: str = "diamond"
    ARROW: str = "arrow"


class _ChartType:
    BAR: str = "bar"
    BAR3D: str = "bar3D"
    BOXPLOT: str = "boxplot"
    EFFECT_SCATTER: str = "effectScatter"
    FUNNEL: str = "funnel"
    FLOWGL: str = "flowGL"
    GAUGE: str = "gauge"
    GEO: str = "geo"
    GRAPH: str = "graph"
    GRAPHGL: str = "graphGL"
    HEATMAP: str = "heatmap"
    KLINE: str = "candlestick"
    LINE: str = "line"
    LINE3D: str = "line3D"
    LINES: str = "lines"
    LINESGL: str = "linesGL"
    LINES3D: str = "lines3D"
    LIQUID: str = "liquidFill"
    MAP: str = "map"
    MAP3D: str = "map3D"
    PARALLEL: str = "parallel"
    PICTORIALBAR: str = "pictorialBar"
    PIE: str = "pie"
    POLAR: str = "polar"
    RADAR: str = "radar"
    SANKEY: str = "sankey"
    SCATTER: str = "scatter"
    SCATTER3D: str = "scatter3D"
    SCATTERGL: str = "scatterGL"
    SUNBURST: str = "sunburst"
    SURFACE: str = "surface"
    THEMERIVER: str = "themeRiver"
    TREE: str = "tree"
    TREEMAP: str = "treemap"
    WORDCLOUD: str = "wordCloud"
    CUSTOM: str = "custom"


ToolTipFormatterType = {
    _ChartType.GEO: JsCode(
        """function (params) {
        return params.name + ' : ' + params.value[2];
    }"""
    ),
    _ChartType.GAUGE: "{a} <br/>{b} : {c}%",
}


class _ThemeType:
    BUILTIN_THEMES = ["light", "dark", "white"]
    LIGHT = "light"
    DARK = "dark"
    WHITE = "white"
    CHALK: str = "chalk"
    ESSOS: str = "essos"
    INFOGRAPHIC: str = "infographic"
    MACARONS: str = "macarons"
    PURPLE_PASSION: str = "purple-passion"
    ROMA: str = "roma"
    ROMANTIC: str = "romantic"
    SHINE: str = "shine"
    VINTAGE: str = "vintage"
    WALDEN: str = "walden"
    WESTEROS: str = "westeros"
    WONDERLAND: str = "wonderland"
    HALLOWEEN: str = "halloween"


class _GeoType:
    SCATTER: str = "scatter"
    EFFECT_SCATTER: str = "effectScatter"
    HEATMAP: str = "heatmap"
    LINES: str = "lines"


class _BMapType:
    # BMap Control location
    ANCHOR_TOP_LEFT = 0
    ANCHOR_TOP_RIGHT = 1
    ANCHOR_BOTTOM_LEFT = 2
    ANCHOR_BOTTOM_RIGHT = 3

    # BMap Navigation Control Type
    NAVIGATION_CONTROL_LARGE = 0
    NAVIGATION_CONTROL_SMALL = 1
    NAVIGATION_CONTROL_PAN = 2
    NAVIGATION_CONTROL_ZOOM = 3

    # BMap Maptype Control Type
    MAPTYPE_CONTROL_HORIZONTAL = 0
    MAPTYPE_CONTROL_DROPDOWN = 1
    MAPTYPE_CONTROL_MAP = 2


class _NotebookType:
    JUPYTER_NOTEBOOK = "jupyter_notebook"
    JUPYTER_LAB = "jupyter_lab"
    NTERACT = "nteract"
    ZEPPELIN = "zeppelin"


class _OnlineHost:
    DEFAULT_HOST = "https://assets.pyecharts.org/assets/v5/"
    NOTEBOOK_HOST = "http://localhost:8888/nbextensions/assets/"


class _RenderSepType:
    SepType = os.linesep


RenderType = _RenderType()
FileType = _FileType()
SymbolType = _SymbolType()
ChartType = _ChartType
ThemeType = _ThemeType()
GeoType = _GeoType()
BMapType = _BMapType
NotebookType = _NotebookType()
OnlineHostType = _OnlineHost()
RenderSepType = _RenderSepType()


class _CurrentConfig:
    PAGE_TITLE = "Awesome-pyecharts"
    ONLINE_HOST = OnlineHostType.DEFAULT_HOST
    NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK
    GLOBAL_ENV = Environment(
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
        loader=FileSystemLoader(
            os.path.join(
                os.path.abspath(os.path.dirname(__file__)), "render", "templates"
            )
        ),
    )


CurrentConfig = _CurrentConfig()
