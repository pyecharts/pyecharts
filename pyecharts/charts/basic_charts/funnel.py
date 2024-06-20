from ... import options as opts
from ... import types
from ...charts.chart import Chart
from ...globals import ChartType


class Funnel(Chart):
    """
    <<< Funnel >>>

    Funnel diagram is suitable for one-way analysis of single process
    with standardized business process, long cycle and multiple links.
    Through comparison of business data of each link in the funnel,
    the link where the potential problems can be found intuitively,
    and then decisions can be made.
    """

    def add(
        self,
        series_name: str,
        data_pair: types.Sequence,
        *,
        color: types.Optional[str] = None,
        color_by: types.Optional[str] = None,
        min_: types.Numeric = 0,
        max_: types.Numeric = 100,
        min_size: types.Union[str, types.Numeric] = "0%",
        max_size: types.Union[str, types.Numeric] = "100%",
        orient: str = "vertical",
        sort_: str = "descending",
        gap: types.Numeric = 0,
        is_legend_hover_link: bool = True,
        funnel_align: str = "center",
        label_opts: types.Label = opts.LabelOpts(),
        tooltip_opts: types.Tooltip = None,
        itemstyle_opts: types.ItemStyle = None,
        emphasis_opts: types.Emphasis = None,
        selected_mode: types.Union[bool, str] = False,
        z_level: types.Numeric = 0,
        z: types.Numeric = 2,
        pos_top: types.Union[str, types.Numeric, None] = None,
        pos_left: types.Union[str, types.Numeric, None] = None,
        pos_bottom: types.Union[str, types.Numeric, None] = None,
        pos_right: types.Union[str, types.Numeric, None] = None,
        width: types.Union[str, types.Numeric, None] = None,
        height: types.Union[str, types.Numeric, None] = None,
        dataset_index: types.Optional[types.Numeric] = None,
        encode: types.Union[types.JSFunc, dict, None] = None,
        markpoint_opts: types.MarkPoint = None,
        markline_opts: types.MarkLine = None,
        markarea_opts: types.MarkArea = None,
    ):
        self._append_color(color)
        if all([isinstance(d, opts.FunnelItem) for d in data_pair]):
            data = data_pair
            for a in data_pair:
                self._append_legend(a.opts.get("name"))
        else:
            data = [{"name": n, "value": v} for n, v in data_pair]
            for a, _ in data_pair:
                self._append_legend(a)

        _dset = set(self.options.get("legend")[0].get("data"))
        self.options.get("legend")[0].update(data=list(_dset))

        self.options.get("series").append(
            {
                "type": ChartType.FUNNEL,
                "name": series_name,
                "data": data,
                "colorBy": color_by,
                "min": min_,
                "max": max_,
                "minSize": min_size,
                "maxSize": max_size,
                "orient": orient,
                "sort": sort_,
                "gap": gap,
                "legendHoverLink": is_legend_hover_link,
                "funnelAlign": funnel_align,
                "label": label_opts,
                "tooltip": tooltip_opts,
                "itemStyle": itemstyle_opts,
                "emphasis": emphasis_opts,
                "selectedMode": selected_mode,
                "zlevel": z_level,
                "z": z,
                "left": pos_left,
                "right": pos_right,
                "top": pos_top,
                "bottom": pos_bottom,
                "width": width,
                "height": height,
                "datasetIndex": dataset_index,
                "encode": encode,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
                "markArea": markarea_opts,
            }
        )
        return self
