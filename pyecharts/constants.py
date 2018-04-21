# coding=utf-8
from __future__ import unicode_literals

CANVAS_RENDERER = "canvas"
SVG_RENDERER = "svg"
PAGE_TITLE = "Echarts"

# presentation types for jupyter
# output file types for pure python
SVG = 'svg'
PNG = 'png'
JPEG = 'jpeg'
DEFAULT_HTML = 'html'
JUPYTER_PRESENTATIONS = [SVG, PNG, JPEG, DEFAULT_HTML]
ENVIRONMENT_PLUGIN_TYPE = 'pyecharts_environment'
JS_EXTENSION_PLUGIN_TYPE = 'pyecharts_js_extension'

ERROR_MESSAGE = "You need python 3.5+ and pyecharts-javascripthon"

SYMBOL = {
    "plane": 'path://M1705.06,1318.313v-89.254l-319.9-221.799l0.073-208.'
    '063c0.521-84.662-26.629-121.796-63.961-121.491c-37.332-0.'
    '305-64.482,36.829-63.961,121.491l0.073,208.063l-319.9,221.'
    '799v89.254l330.343-157.288l12.238,241.308l-134.449,92.931l0.'
    '531,42.034l175.125-42.917l175.125,42.917l0.531-42.034l-134'
    '.449-92.931l12.238-241.308L1705.06,1318.313z'
}


# Mouse Events

MOUSE_CLICK = 'click'
MOUSE_DBCLICK = 'dbclick'
MOUSE_DOWN = 'mousedown'
MOUSE_OVER = 'mouseover'
MOUSE_GLOBALOUT = 'globalout'

# Other Events

LEGEND_SELECT_CHANGED = 'legendselectchanged'
LEGEND_SELECTED = 'legendselected'
LEGEND_UNSELECTAED = 'legendunselected'
LEGEND_SCROLL = 'legendscroll'
DATA_ZOOM = 'datazoom'
DATA_RANGE_SELECTED = 'datarangeselected'
TIMELINE_CHANGED = 'timelinechanged'
TIMELINE_PLAY_CHANGED = 'timelineplaychanged'
RESTORE = 'restore'
DATA_VIEW_CHANGED = 'dataviewchanged'
MAGIC_TYPE_CHANGED = 'magictypechanged'
GEO_SELECT_CHANGED = 'geoselectchanged'
GEO_SELECTED = 'geoselected'
GEO_UNSELECTED = 'geounselected'
PIE_SELECT_CHANGED = 'pieselectchanged'
PIE_SELECTED = 'pieselected'
PIE_UNSELECTED = 'pieunselected'
MAP_SELECT_CHANGED = 'mapselectchanged'
MAP_SELECTED = 'mapselected'
MAP_UNSELECTED = 'mapunselected'
AXIS_AREA_SELECTED = 'axisareaselected'
FOCUS_NODE_ADJACENCY = 'focusnodeadjacency'
UNFOCUS_NODE_ADJACENCY = 'unfocusnodeadjacency'
BRUSH = 'brush'
BRUSH_SELECTED = 'brushselected'
