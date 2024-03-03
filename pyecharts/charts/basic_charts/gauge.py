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
        min_: types.Numeric = 0,
        max_: types.Numeric = 100,
        split_number: types.Numeric = 10,
        center: types.Sequence = None,
        radius: types.Union[types.Numeric, str] = "75%",
        start_angle: types.Numeric = 225,
        end_angle: types.Numeric = -45,
        is_clock_wise: bool = True,
        title_label_opts: types.GaugeTitle = opts.GaugeTitleOpts(
            offset_center=["0%", "20%"],
        ),
        detail_label_opts: types.GaugeDetail = opts.GaugeDetailOpts(
            formatter="{value}%",
            offset_center=["0%", "40%"],
        ),
        progress: types.GaugeProgress = opts.GaugeProgressOpts(),
        pointer: types.GaugePointer = opts.GaugePointerOpts(),
        anchor: types.GaugeAnchor = opts.GaugeAnchorOpts(),
        tooltip_opts: types.Tooltip = None,
        axisline_opts: types.AxisLine = None,
        axistick_opts: types.AxisTick = None,
        axislabel_opts: types.AxisLabel = None,
        itemstyle_opts: types.ItemStyle = None,
        emphasis_opts: types.Emphasis = None,
    ):
        if center is None:
            center = ["50%", "50%"]

        self._append_legend(series_name)
        self.options.get("series").append(
            {
                "type": ChartType.GAUGE,
                "title": title_label_opts,
                "detail": detail_label_opts,
                "name": series_name,
                "min": min_,
                "max": max_,
                "splitNumber": split_number,
                "center": center,
                "radius": radius,
                "startAngle": start_angle,
                "endAngle": end_angle,
                "clockwise": is_clock_wise,
                "data": [{"name": n, "value": v} for n, v in data_pair],
                "tooltip": tooltip_opts,
                "axisLine": axisline_opts,
                "axisTick": axistick_opts,
                "axisLabel": axislabel_opts,
                "progress": progress,
                "anchor": anchor,
                "pointer": pointer,
                "itemStyle": itemstyle_opts,
                "emphasis": emphasis_opts,
            }
        )
        return self
