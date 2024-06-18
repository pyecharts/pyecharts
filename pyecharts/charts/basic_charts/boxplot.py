from ... import options as opts
from ... import types
from ...charts.chart import RectChart
from ...globals import ChartType


class Boxplot(RectChart):
    """
    <<< Boxplot >>>

    A box-plot is a statistical chart used to show a set of data dispersion data.
    It displays the maximum, minimum, median, lower quartile, and upper quartile
    of a set of data.
    """

    def add_yaxis(
        self,
        series_name: str,
        y_axis: types.Optional[
            types.Sequence[types.Union[opts.BoxplotItem, dict]]
        ] = None,
        *,
        chart_type: str = ChartType.BOXPLOT,
        xaxis_index: types.Optional[types.Numeric] = None,
        yaxis_index: types.Optional[types.Numeric] = None,
        dataset_index: types.Optional[types.Numeric] = None,
        color_by: types.Optional[str] = None,
        is_legend_hover_link: bool = True,
        is_hover_animation: bool = True,
        layout: types.Optional[str] = None,
        box_width: types.Optional[types.Sequence] = None,
        selected_mode: types.Union[bool, str] = False,
        dimensions: types.Union[types.Sequence, None] = None,
        label_opts: types.Label = opts.LabelOpts(),
        markpoint_opts: types.MarkPoint = opts.MarkPointOpts(),
        markline_opts: types.MarkLine = opts.MarkLineOpts(),
        markarea_opts: types.MarkArea = None,
        z_level: types.Numeric = 0,
        z: types.Numeric = 2,
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        emphasis_opts: types.Emphasis = None,
        blur_opts: types.Blur = None,
        select_opts: types.Select = None,
        encode: types.Union[types.JSFunc, dict, None] = None,
    ):
        if box_width is None:
            box_width = [7, 50]

        self._append_legend(series_name)
        self.options.get("series").append(
            {
                "type": chart_type,
                "name": series_name,
                "xAxisIndex": xaxis_index,
                "yAxisIndex": yaxis_index,
                "datasetIndex": dataset_index,
                "colorBy": color_by,
                "legendHoverLink": is_legend_hover_link,
                "hoverAnimation": is_hover_animation,
                "layout": layout,
                "boxWidth": box_width,
                "selectedMode": selected_mode,
                "dimensions": dimensions,
                "data": y_axis,
                "label": label_opts,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
                "markArea": markarea_opts,
                "zlevel": z_level,
                "z": z,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "emphasis": emphasis_opts,
                "blur": blur_opts,
                "select": select_opts,
                "encode": encode,
            }
        )
        return self

    @staticmethod
    def prepare_data(items):
        data = []
        for item in items:
            if not item:
                data.append([])
            try:
                d, res = sorted(item), []
                for i in range(1, 4):
                    n = i * (len(d) + 1) / 4
                    k = int(n)
                    m = n - k
                    if m == 0:
                        res.append(d[k - 1])
                    elif m == 1 / 4:
                        res.append(d[k - 1] * 0.75 + d[k] * 0.25)
                    elif m == 1 / 2:
                        res.append(d[k - 1] * 0.50 + d[k] * 0.50)
                    elif m == 3 / 4:
                        res.append(d[k - 1] * 0.25 + d[k] * 0.75)
                data.append([d[0]] + res + [d[-1]])
            except TypeError:
                # one of the item element is None
                data.append([])
        return data
