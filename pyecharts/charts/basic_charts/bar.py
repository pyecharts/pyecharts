# coding=utf-8
from ...charts.chart import AxisChart
from ...commons.types import ListTuple, Optional, Union
from ...options import AxisOpts, InitOpts, LabelOpts, MarkLineOpts, MarkPointOpts


class Bar(AxisChart):
    """
    <<< 柱状图/条形图 >>>

    柱状/条形图，通过柱形的高度/条形的宽度来表现数据的大小。
    """

    def __init__(self, init_opts: Union[InitOpts, dict] = InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options.update(yAxis=[AxisOpts().opts])

    def reversal_axis(self):
        self.options["yAxis"][0]["data"] = self._xaxis_data
        self.options["xAxis"][0]["data"] = None
        return self

    def add_yaxis(
        self,
        series_name: str,
        yaxis_data: ListTuple,
        *,
        stack: Optional[str] = None,
        category_gap: str = "20%",
        label_opts: Union[LabelOpts, dict] = LabelOpts(),
        markpoint_opts: Union[MarkPointOpts, dict, None] = None,
        markline_opts: Union[MarkLineOpts, dict, None] = None,
    ):
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts
        if isinstance(markpoint_opts, MarkPointOpts):
            markpoint_opts = markpoint_opts.opts
        if isinstance(markline_opts, MarkLineOpts):
            markline_opts = markline_opts.opts

        self._append_legend(series_name)
        self.options.get("series").append(
            {
                "type": "bar",
                "name": series_name,
                "data": yaxis_data,
                "stack": stack,
                "barCategoryGap": category_gap,
                "label": label_opts,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
            }
        )
        return self
