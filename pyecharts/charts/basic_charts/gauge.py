from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Gauge(Chart):
    """
    <<< Gauge >>>

    The gauge displays a single key business measure.
    """

    def add(
        self,
        series_name: str,
        data_pair: types.Sequence,
        *,
        is_selected: bool = True,
        min_: types.Numeric = 0,
        max_: types.Numeric = 100,
        split_number: types.Numeric = 10,
        radius: types.Union[types.Numeric, str] = "75%",
        start_angle: types.Numeric = 225,
        end_angle: types.Numeric = -45,
        is_clock_wise: bool = True,
        title_label_opts: types.GaugeTitle = opts.GaugeTitleOpts(),
        detail_label_opts: types.GaugeDetail = opts.GaugeDetailOpts(
            formatter="{value}%"
        ),
        pointer: types.GaugePointer = opts.GaugePointerOpts(),
        tooltip_opts: types.Tooltip = None,
        axisline_opts: types.AxisLine = None,
        itemstyle_opts: types.ItemStyle = None,
    ):

        self._append_legend(series_name, is_selected)
        self.options.get("series").append(
            {
                "type": ChartType.GAUGE,
                "title": title_label_opts,
                "detail": detail_label_opts,
                "name": series_name,
                "min": min_,
                "max": max_,
                "splitNumber": split_number,
                "radius": radius,
                "startAngle": start_angle,
                "endAngle": end_angle,
                "clockwise": is_clock_wise,
                "data": [{"name": n, "value": v} for n, v in data_pair],
                "tooltip": tooltip_opts,
                "axisLine": axisline_opts,
                "pointer": pointer,
                "itemStyle": itemstyle_opts,
            }
        )
        return self
