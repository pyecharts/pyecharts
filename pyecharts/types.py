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
from .options.charts_options import BaseGraphic, GlobeLayersOpts
from .options.series_options import JsCode, JSFunc, Numeric

Init = Union[opts.InitOpts, dict]
RenderInit = Union[opts.RenderOpts, dict]

Axis = Union[opts.AxisOpts, dict, None]
Axis3D = Union[opts.Axis3DOpts, dict]
AxisLine = Union[opts.AxisLineOpts, dict, None]
AxisLabel = Union[opts.LabelOpts, dict, None]
AxisPointer = Union[opts.AxisPointerOpts, dict, None]
AxisTick = Union[opts.AxisTickOpts, dict, None]
AreaStyle = Union[opts.AreaStyleOpts, dict, None]
BarBackground = Union[opts.BarBackgroundStyleOpts, dict, None]
Blur = Union[opts.BlurOpts, dict, None]
Brush = Union[opts.BrushOpts, dict, None]
_DataZoomType = Union[opts.DataZoomOpts, dict]
DataZoom = Union[_DataZoomType, Sequence[_DataZoomType], None]
Effect = Union[opts.EffectOpts, dict, None]
Emphasis = Union[opts.EmphasisOpts, dict, None]
Emphasis3D = Union[opts.Emphasis3DOpts, dict, None]
GaugeAnchor = Union[opts.GaugeAnchorOpts, dict, None]
GaugeTitle = Union[opts.GaugeTitleOpts, dict, None]
GaugeDetail = Union[opts.GaugeDetailOpts, dict, None]
GaugePointer = Union[opts.GaugePointerOpts, dict, None]
GaugeProgress = Union[opts.GaugeProgressOpts, dict, None]
GeoRegions = Union[opts.GeoRegionsOpts, dict, None]
_GraphicType = Union[BaseGraphic, dict]
Graphic = Union[_GraphicType, Sequence[_GraphicType], None]
GraphGLForceAtlas2 = Union[opts.GraphGLForceAtlas2Opts, dict, None]
_GlobeLayersType = Union[GlobeLayersOpts, dict]
GlobeLayers = Union[_GlobeLayersType, Sequence[_GlobeLayersType], None]
ItemStyle = Union[opts.ItemStyleOpts, dict, None]
Map3DColorMaterial = Union[opts.Map3DColorMaterialOpts, dict, None]
Map3DLabel = Union[opts.Map3DLabelOpts, dict, None]
Map3DLight = Union[opts.Map3DLightOpts, dict, None]
Map3DLambertMaterial = Union[opts.Map3DLambertMaterialOpts, dict, None]
Map3DPostEffect = Union[opts.Map3DPostEffectOpts, dict, None]
Map3DRealisticMaterial = Union[opts.Map3DRealisticMaterialOpts, dict, None]
Map3DViewControl = Union[opts.Map3DViewControlOpts, dict, None]
MarkArea = Union[opts.MarkAreaOpts, dict, None]
MarkPoint = Union[opts.MarkPointOpts, dict, None]
MarkLine = Union[opts.MarkLineOpts, dict, None]
MinorTick = Union[opts.MinorTickOpts, dict, None]
Label = Union[opts.LabelOpts, dict, None]
Legend = Union[opts.LegendOpts, dict]
LineStyle = Union[opts.LineStyleOpts, dict, None]
Lines3DEffect = Union[opts.Lines3DEffectOpts, dict, None]
PieLabelLine = Union[opts.PieLabelLineOpts, dict, None]
PieEmptyCircle = Union[opts.PieEmptyCircleStyle, dict, None]
TextStyle = Union[opts.TextStyleOpts, dict, None]
TimeLineControl = Union[opts.TimelineControlStyle, dict, None]
TimeLinkCheckPoint = Union[opts.TimelineCheckPointerStyle, dict, None]
Title = Union[opts.TitleOpts, dict]
Tooltip = Union[opts.TooltipOpts, dict, None]
Toolbox = Union[opts.ToolboxOpts, dict]
TreeMapBreadcrumb = Union[opts.TreeMapBreadcrumbOpts, dict, None]
Select = Union[opts.SelectOpts, dict, None]
SplitLine = Union[opts.SplitLineOpts, dict, None]
SplitArea = Union[opts.SplitAreaOpts, dict, None]
SingleAxis = Union[opts.SingleAxisOpts, dict, None]
SunburstLabelLayout = Union[opts.SunburstLabelLayoutOpts, dict, None]
SunburstLabelLine = Union[opts.SunburstLabelLineOpts, dict, None]
SunburstLevelOpts = Union[opts.SunburstLevelOpts, dict, None]
_VisualMapType = Union[opts.VisualMapOpts, dict]
VisualMap = Union[_VisualMapType, Sequence[_VisualMapType], None]

Calendar = Union[opts.CalendarOpts, dict, None]
CalendarDayLabelOpts = Union[opts.CalendarDayLabelOpts, dict, None]
CalendarMonthLabelOpts = Union[opts.CalendarMonthLabelOpts, dict, None]
CalendarYearLabelOpts = Union[opts.CalendarYearLabelOpts, dict, None]

GraphNode = Union[opts.GraphNode, dict]
GraphLink = Union[opts.GraphLink, dict]
GraphCategory = Union[opts.GraphCategory, dict]
GraphGLNode = Union[opts.GraphGLNode, dict]
GraphGLLink = Union[opts.GraphGLLink, dict]
Grid3D = Union[opts.Grid3DOpts, dict]

RadiusAxis = Union[opts.RadiusAxisOpts, dict]
AngleAxis = Union[opts.AngleAxisOpts, dict]

BMapOverviewMapControl = Union[opts.BMapOverviewMapControlOpts, dict, None]
BMapNavigationControl = Union[opts.BMapNavigationControlOpts, dict, None]
BMapScaleControl = Union[opts.BMapScaleControlOpts, dict, None]
BMapTypeControl = Union[opts.BMapTypeControlOpts, dict, None]
BMapCopyrightType = Union[opts.BMapCopyrightTypeOpts, dict, None]
BMapGeoLocationControl = Union[opts.BMapGeoLocationControlOpts, dict, None]

_SankeyLevelType = Union[opts.SankeyLevelsOpts, dict]
SankeyLevel = Union[Sequence[_SankeyLevelType], None]

TreeLeavesOpts = Union[opts.TreeLeavesOpts, dict, None]

TreeMapItemStyleOpts = Union[opts.TreeMapItemStyleOpts, dict, None]
_TreeMapLevelType = Union[opts.TreeMapLevelsOpts, dict]
TreeMapLevel = Union[_TreeMapLevelType, Sequence[_TreeMapLevelType], None]

Polar = Union[opts.PolarOpts, dict, None]
