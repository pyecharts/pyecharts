# coding=utf-8
from ... import options as opts
from ...charts.chart import AxisChart
from ...commons.types import ListTuple, Union


class HeatMap(AxisChart):
    """
    <<< 热力图 >>>

    热力图主要通过颜色去表现数值的大小，必须要配合 visualMap 组件使用。
    直角坐标系上必须要使用两个类目轴。
    """

    def __init__(self, init_opts: Union[opts.InitOpts, dict] = opts.InitOpts()):
        super().__init__(init_opts=init_opts)
        self.options.update(yAxis=[opts.AxisOpts().opts])
        self.set_global_opts(visualmap_opts=opts.VisualMapOpts(orient="horizontal"))

    def add_yaxis(
        self,
        name: str,
        yaxis_data: ListTuple,
        value: ListTuple,
        *,
        label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),
        markpoint_opts: Union[opts.MarkPointOpts, dict, None] = None,
        markline_opts: Union[opts.MarkLineOpts, dict, None] = None,
    ):
        if isinstance(label_opts, opts.LabelOpts):
            label_opts = label_opts.opts
        if isinstance(markpoint_opts, opts.MarkPointOpts):
            markpoint_opts = markpoint_opts.opts
        if isinstance(markline_opts, opts.MarkLineOpts):
            markline_opts = markline_opts.opts

        self.options.get("yAxis")[0].update(data=yaxis_data)
        self.options.get("series").append(
            {
                "type": "heatmap",
                "name": name,
                "data": value,
                "label": label_opts,
                "markLine": markline_opts,
                "markPoint": markpoint_opts,
            }
        )
        return self
