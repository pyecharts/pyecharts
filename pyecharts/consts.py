# coding=utf-8

BUILTIN_THEMES = ["light", "dark", "white"]
ONLINE_HOST = "http://chenjiandongx.com/go-echarts-assets/assets/"
COLOR_LST = [
    "#c23531",
    "#2f4554",
    "#61a0a8",
    "#d48265",
    "#749f83",
    "#ca8622",
    "#bda29a",
    "#6e7074",
    "#546570",
    "#c4ccd3",
    "#f05b72",
    "#ef5b9c",
    "#f47920",
    "#905a3d",
    "#fab27b",
    "#2a5caa",
    "#444693",
    "#726930",
    "#b2d235",
    "#6d8346",
    "#ac6767",
    "#1d953f",
    "#6950a1",
    "#918597",
    "#f6f5ec",
]


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
    PLANE: str = "path://M1705.06,1318.313v-89.254l-319.9-221.799l0.073-208."
    "063c0.521-84.662-26.629-121.796-63.961-121.491c-37.332-0."
    "305-64.482,36.829-63.961,121.491l0.073,208.063l-319.9,221."
    "799v89.254l330.343-157.288l12.238,241.308l-134.449,92.931l0."
    "531,42.034l175.125-42.917l175.125,42.917l0.531-42.034l-134"
    ".449-92.931l12.238-241.308L1705.06,1318.313z"


class _ChartType:
    BAR: str = "bar"
    BOXPLOT: str = "boxplot"
    EFFECT_SCATTER: str = "effectScatter"
    FUNNEL: str = "funnel"
    GAUGE: str = "gauge"
    GEO: str = "geo"
    KLINE: str = "candlestick"
    LINE: str = "line"
    LIQUID: str = "liquidFill"
    MAP: str = "map"
    PARALLEL: str = "parallel"
    PIE: str = "pie"


class _ToolTipFormatterType:
    GEO = """function (params) {
        return params.name + ' : ' + params.value[2];
    }"""
    GAUGE = "{a} <br/>{b} : {c}%"


class _ThemeType:
    LIGHT_THEME = "light"
    DARK_THEME = "dark"
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


RENDER_TYPE = _RenderType()
FILE_TYPE = _FileType()
SYMBOL_TYPE = _SymbolType()
CHART_TYPE = _ChartType
TOOLTIP_FORMATTER_TYPE = _ToolTipFormatterType()
THEME_TYPE = _ThemeType()
GEO_TYPES = _GeoType()
