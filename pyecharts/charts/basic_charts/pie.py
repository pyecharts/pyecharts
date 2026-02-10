from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Pie(Chart):
    """
    <<< Pie >>>

    The pie chart is mainly used to represent the proportion of data of
    different categories in the total. Each radian represents the ratio of
    the number of data points.
    """

    def add(
        self,
        series_name: str,
        data_pair: types.Sequence[types.Union[types.Sequence, opts.PieItem, dict]],
        *,
        color: types.Optional[str] = None,
        color_by: types.Optional[str] = "data",
        is_legend_hover_link: bool = True,
        coordinate_system: types.Optional[str] = None,
        coordinate_system_usage: types.Optional[str] = None,
        coord: types.Union[types.Sequence, types.Numeric, str] = None,
        geo_index: types.Optional[types.Numeric] = None,
        geo_id: types.Optional[types.Numeric] = None,
        calendar_index: types.Optional[types.Numeric] = None,
        calendar_id: types.Optional[types.Numeric] = None,
        matrix_index: types.Optional[types.Numeric] = None,
        matrix_id: types.Optional[types.Numeric] = None,
        selected_mode: types.Union[str, bool] = False,
        selected_offset: types.Numeric = 10,
        radius: types.Optional[types.Sequence] = None,
        center: types.Optional[types.Sequence] = None,
        rosetype: types.Union[str, bool] = None,
        is_clockwise: bool = True,
        start_angle: types.Numeric = 90,
        end_angle: types.Optional[types.Numeric] = None,
        min_angle: types.Numeric = 0,
        min_show_label_angle: types.Numeric = 0,
        is_avoid_label_overlap: bool = True,
        is_still_show_zero_sum: bool = True,
        percent_precision: types.Numeric = 2,
        is_show_empty_circle: bool = True,
        empty_circle_style_opts: types.PieEmptyCircle = opts.PieEmptyCircleStyle(),
        label_opts: types.Label = opts.LabelOpts(),
        label_line_opts: types.PieLabelLine = opts.PieLabelLineOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        emphasis_opts: types.Emphasis = None,
        encode: types.Union[types.JSFunc, dict, None] = None,
        markpoint_opts: types.MarkPoint = None,
        markline_opts: types.MarkLine = None,
        markarea_opts: types.MarkArea = None,
    ):
        if self.options.get("dataset") is not None:
            data = None
            self.options.get("legend")[0].update(
                data=[d[0] for d in self.options.get("dataset")[0].get("source")][1:]
            )
        elif isinstance(data_pair[0], opts.PieItem):
            data = data_pair
        else:
            data = [{"name": n, "value": v} for n, v in data_pair]

            for a, _ in data_pair:
                self.options.get("legend")[0].get("data").append(a)

            _dlst = self.options.get("legend")[0].get("data")
            _dset = list(set(_dlst))
            _dset.sort(key=_dlst.index)
            self.options.get("legend")[0].update(data=list(_dset))

        if not radius:
            radius = ["0%", "75%"]
        if not center:
            center = ["50%", "50%"]

        self._append_color(color)
        self.options.get("series").append(
            {
                "type": ChartType.PIE,
                "name": series_name,
                "colorBy": color_by,
                "legendHoverLink": is_legend_hover_link,
                "coordinateSystem": coordinate_system,
                "coordinateSystemUsage": coordinate_system_usage,
                "coord": coord,
                "geoIndex": geo_index,
                "geoId": geo_id,
                "calendarIndex": calendar_index,
                "calendarId": calendar_id,
                "matrixIndex": matrix_index,
                "matrixId": matrix_id,
                "selectedMode": selected_mode,
                "selectedOffset": selected_offset,
                "clockwise": is_clockwise,
                "startAngle": start_angle,
                "endAngle": end_angle,
                "minAngle": min_angle,
                "minShowLabelAngle": min_show_label_angle,
                "avoidLabelOverlap": is_avoid_label_overlap,
                "stillShowZeroSum": is_still_show_zero_sum,
                "percentPrecision": percent_precision,
                "showEmptyCircle": is_show_empty_circle,
                "emptyCircleStyle": empty_circle_style_opts,
                "data": data,
                "radius": radius,
                "center": center,
                "roseType": rosetype,
                "label": label_opts,
                "labelLine": label_line_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "emphasis": emphasis_opts,
                "encode": encode,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
                "markArea": markarea_opts,
            }
        )
        return self
