from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Chord(Chart):
    """
    <<< Chord >>>

    The chord diagram visually presents the flow and weights
    within complex relationship networks, making it particularly
    suitable for multidimensional relationship analysis in scenarios
    such as financial transactions and social networks.
    """

    def add(
        self,
        series_name: str,
        data: types.Sequence[types.ChordData],
        links: types.Sequence[types.ChordLink],
        *,
        is_clockwise: bool = False,
        coordinate_system: types.Optional[str] = None,
        coordinate_system_usage: types.Optional[str] = None,
        coord: types.Union[types.Sequence, types.Numeric, str] = None,
        color_by: types.Optional[str] = None,
        pos_left: types.Optional[str] = None,
        pos_top: types.Optional[str] = None,
        pos_right: types.Optional[str] = None,
        pos_bottom: types.Optional[str] = None,
        width: types.Optional[str] = None,
        height: types.Optional[str] = None,
        center: types.Optional[types.Sequence] = None,
        radius: types.Optional[types.Union[types.Sequence, str]] = None,
        start_angle: types.Numeric = 90,
        end_angle: types.Optional[types.Numeric] = None,
        min_angle: types.Optional[types.Numeric] = None,
        pad_angle: types.Optional[types.Numeric] = None,
        tooltip_opts: types.Tooltip = None,
        label_opts: types.Label = None,
        linestyle_opts: types.LineStyle = None,
        itemstyle_opts: types.ItemStyle = None,
        emphasis_opts: types.Emphasis = None,
    ):
        self.options.get("series").append({
            "type": ChartType.CHORD,
            "name": series_name,
            "data": data,
            "links": links,
            "clockwise": is_clockwise,
            "coordinateSystem": coordinate_system,
            "coordinateSystemUsage": coordinate_system_usage,
            "coord": coord,
            "colorBy": color_by,
            "left": pos_left,
            "top": pos_top,
            "right": pos_right,
            "bottom": pos_bottom,
            "width": width,
            "height": height,
            "center": center,
            "radius": radius,
            "startAngle": start_angle,
            "endAngle": end_angle,
            "minAngle": min_angle,
            "padAngle": pad_angle,
            "tooltip": tooltip_opts,
            "label": label_opts,
            "lineStyle": linestyle_opts,
            "itemStyle": itemstyle_opts,
            "emphasis": emphasis_opts,
        })

        return self
