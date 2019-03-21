# coding=utf-8
from ... import options as opts
from ...charts.chart import AxisChart
from ...commons.types import ListTuple, Union


class Boxplot(AxisChart):
    """
    <<< 箱形图 >>>

    箱形图是一种用作显示一组数据分散情况资料的统计图。它能显示出一组数据
    的最大值、最小值、中位数、下四分位数及上四分位数。
    """

    def __init__(self, init_opts: Union[opts.InitOpts, dict] = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options.update(yAxis=[opts.AxisOpts().opts])

    def add_yaxis(
        self,
        name: str,
        y_axis: ListTuple,
        *,
        label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),
        markpoint_opts: Union[opts.MarkPointOpts, dict] = opts.MarkPointOpts(),
        markline_opts: Union[opts.MarkLineOpts, dict] = opts.MarkLineOpts(),
    ):
        if isinstance(label_opts, opts.LabelOpts):
            label_opts = label_opts.opts
        if isinstance(markpoint_opts, opts.MarkPointOpts):
            markpoint_opts = markpoint_opts.opts
        if isinstance(markline_opts, opts.MarkLineOpts):
            markline_opts = markline_opts.opts

        self._append_legend(name)
        self.options.get("series").append(
            {
                "type": "boxplot",
                "name": name,
                "data": y_axis,
                "label": label_opts,
                "markPoint": markpoint_opts,
                "markLine": markline_opts,
            }
        )
        return self
