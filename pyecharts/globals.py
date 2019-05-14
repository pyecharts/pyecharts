import os

from jinja2 import Environment, FileSystemLoader


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
    BOXPLOT: str = "boxplot"
    EFFECT_SCATTER: str = "effectScatter"
    FUNNEL: str = "funnel"
    GAUGE: str = "gauge"
    GEO: str = "geo"
    GRAPH: str = "graph"
    HEATMAP: str = "heatmap"
    KLINE: str = "candlestick"
    LINE: str = "line"
    LINES: str = "lines"
    LIQUID: str = "liquidFill"
    MAP: str = "map"
    PARALLEL: str = "parallel"
    PIE: str = "pie"
    POLAR: str = "polar"
    RADAR: str = "radar"
    SANKEY: str = "sankey"
    SCATTER: str = "scatter"
    SUNBURST: str = "sunburst"
    THEMERIVER: str = "themeRiver"
    TREE: str = "tree"
    TREEMAP: str = "treemap"
    WORDCLOUD: str = "wordCloud"


class _ToolTipFormatterType:
    GEO = """function (params) {
        return params.name + ' : ' + params.value[2];
    }"""
    GAUGE = "{a} <br/>{b} : {c}%"


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


RenderType = _RenderType()
FileType = _FileType()
SymbolType = _SymbolType()
ChartType = _ChartType
TooltipFormatterType = _ToolTipFormatterType()
ThemeType = _ThemeType()
GeoType = _GeoType()
BMapType = _BMapType
NotebookType = _NotebookType()


class _CurrentConfig:
    ONLINE_HOST = "https://assets.pyecharts.org/assets/"
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
