from typing import (
    Any,
    Callable,
    Iterable,
    List,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Union,
)

from . import options as opts
from .options.series_options import JsCode, JSFunc, Numeric

Init = Union[opts.InitOpts, dict]


AxisLine = Union[opts.AxisLineOpts, dict, None]
AreaStyle = Union[opts.AreaStyleOpts, dict, None]
Effect = Union[opts.EffectOpts, dict, None]
ItemStyle = Union[opts.ItemStyleOpts, dict, None]
MarkPoint = Union[opts.MarkPointOpts, dict, None]
MarkLine = Union[opts.MarkLineOpts, dict, None]
Label = Union[opts.LabelOpts, dict, None]
LineStyle = Union[opts.LineStyleOpts, dict, None]
TextStyle = Union[opts.TextStyleOpts, dict, None]
Tooltip = Union[opts.TooltipOpts, dict, None]
SplitLine = Union[opts.SplitLineOpts, dict, None]
SplitArea = Union[opts.SplitAreaOpts, dict, None]
SingleAxis = Union[opts.SingleAxisOpts, dict, None]

Calendar = Union[opts.CalendarOpts, dict, None]

GraphNode = Union[opts.GraphNode, dict]
GraphLink = Union[opts.GraphLink, dict]
GraphCategory = Union[opts.GraphCategory, dict]

RadiusAxis = Union[opts.RadiusAxisOpts, dict]
AngleAxis = Union[opts.AngleAxisOpts, dict]

BMapOverviewMapControl = Union[opts.BMapOverviewMapControlOpts, dict, None]
BMapNavigationControl = Union[opts.BMapNavigationControlOpts, dict, None]
BMapScaleControl = Union[opts.BMapScaleControlOpts, dict, None]
BMapTypeControl = Union[opts.BMapTypeControlOpts, dict, None]
BMapCopyrightType = Union[opts.BMapCopyrightTypeOpts, dict, None]
BMapGeoLocationControl = Union[opts.BMapGeoLocationControlOpts, dict, None]
