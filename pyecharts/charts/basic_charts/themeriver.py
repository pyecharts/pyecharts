# coding=utf-8
from ...charts.chart import Chart
from ...commons.types import ListTuple, Union
from ...options import InitOpts, LabelOpts


class ThemeRiver(Chart):
    """
    <<< 主题河流图 >>>

    主题河流图是一种特殊的流图, 它主要用来表示事件或主题等在一段时间内的变化。
    """

    def __init__(self, init_opts: Union[InitOpts, dict] = InitOpts()):
        super().__init__(init_opts=init_opts)

    def add(
        self,
        name: str,
        data: ListTuple,
        label_opts: Union[LabelOpts, dict] = LabelOpts(),
    ):
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts

        self._append_legend(name)
        self.options.get("series").append(
            {"type": "themeRiver", "name": name, "data": data, "label": label_opts}
        )

        self.options.update(singleAxis={"type": "time"})
        self.options.get("tooltip").update(trigger="axis")
        return self
