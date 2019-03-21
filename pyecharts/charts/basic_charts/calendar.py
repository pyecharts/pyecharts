# coding=utf-8
from ...charts.chart import Chart
from ...commons.types import ListTuple, Union
from ...options import InitOpts, LabelOpts, MarkLineOpts, MarkPointOpts


class Calendar(Chart):
    """
    <<< 日历图 >>>

    热力图主要通过颜色去表现数值的大小，必须要配合 visualMap 组件使用。
    直角坐标系上必须要使用两个类目轴。
    """

    def __init__(self, init_opts: Union[InitOpts, dict] = InitOpts()):
        super().__init__(init_opts=init_opts)

    def add_yaxis(
        self,
        name: str,
        yaxis_data: ListTuple,
        *,
        label_opts: Union[LabelOpts, dict] = LabelOpts(),
    ):
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts

        # if _is_calendar:
        #     name, data = args

        # if "yaxis_formatter" not in kwargs:
        #     kwargs["yaxis_formatter"] = None
        #     self._append_legend(name)

        self.options.get("series").append(
            {
                "type": "heatmap",
                "name": name,
                "data": yaxis_data,
                "label": label_opts,
            }
        )

        # if _is_calendar:
        #     self.options.get("toolbox").update(left="98%", top="26%")
        #     self.options.get("series")[0].update(coordinateSystem="calendar")
        #     self.options.update(calendar=chart["calendar"])
        return self
