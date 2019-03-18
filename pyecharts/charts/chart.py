# coding=utf-8

import uuid

from ..charts.base import Base
from ..commons.consts import COLOR_LST, RENDER_TYPE
from ..options import *
from ..types import *


class Chart(Base):
    """
    `Chart`类是所有非自定义类的基类，继承自 `Base` 类
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        super().__init__(init_opts=init_opts)
        self._colorlst = COLOR_LST
        self.options.update(
            series_id=uuid.uuid4().hex, series=[], legend=[{"data": []}]
        )

    def set_series_opts(
        self,
        label_opts: Union[LabelOpts, Dict, None] = None,
        linestyle_opts: Union[LineStyleOpts, Dict, None] = None,
        splitline_opts: Union[SplitLineOpts, Dict, None] = None,
        axisline_opts: Union[AxisLineOpts, Dict, None] = None,
        markpoint_opts: Union[MarkPointOpts, Dict, None] = None,
        markline_opts: Union[MarkLineOpts, Dict, None] = None,
    ):
        _series = self.options.get("series")
        if label_opts:
            if isinstance(label_opts, LabelOpts):
                label_opts = label_opts.opts
            for s in _series:
                s.update(label=label_opts)

        if linestyle_opts:
            if isinstance(linestyle_opts, LineStyleOpts):
                linestyle_opts = linestyle_opts.opts
            for s in _series:
                s.update(lineStyle=linestyle_opts)

        if splitline_opts:
            if isinstance(splitline_opts, SplitLineOpts):
                splitline_opts = splitline_opts.opts
            for s in _series:
                s.update(splitLine=splitline_opts)

        if axisline_opts:
            if isinstance(axisline_opts, AxisLineOpts):
                axisline_opts = axisline_opts.opts
            for s in _series:
                s.update(axisLine=axisline_opts)

        if markpoint_opts:
            if isinstance(markpoint_opts, MarkPointOpts):
                markpoint_opts = markpoint_opts.opts
            for s in _series:
                s.update(markPoint=markpoint_opts)

        if markline_opts:
            if isinstance(markline_opts, MarkLineOpts):
                markline_opts = markline_opts.opts
            for s in _series:
                s.update(markLine=markline_opts)
        return self

    def _append_legend(self, name):
        self.options.get("legend")[0].get("data").append(name)

    def set_global_opts(
        self,
        title_opts: TitleOpts = TitleOpts(),
        toolbox_opts: ToolboxOpst = ToolboxOpst(),
        tooltip_opts: TooltipOpts = TooltipOpts(),
        legend_opts: LegendOpts = LegendOpts(),
        visualmap_opts: VisualMapOpts = None,
        datazoom_opts: DataZoomOpts = None,
    ):
        if isinstance(title_opts, TitleOpts):
            title_opts = title_opts.opts
        if isinstance(toolbox_opts, ToolboxOpst):
            toolbox_opts = toolbox_opts.opts
        if isinstance(tooltip_opts, TooltipOpts):
            tooltip_opts = tooltip_opts.opts
        if isinstance(legend_opts, LegendOpts):
            legend_opts = legend_opts.opts

        self.options.update(
            title=title_opts, toolbox=toolbox_opts, tooltip=tooltip_opts
        )

        for _s in self.options["legend"]:
            _s.update(legend_opts)

        if visualmap_opts:
            if isinstance(visualmap_opts, VisualMapOpts):
                visualmap_opts = visualmap_opts.ops
            self.options.update(visualMap=visualmap_opts)

        if datazoom_opts:
            if isinstance(datazoom_opts, DataZoomOpts):
                datazoom_opts = datazoom_opts.opts
            self.options.update(dataZoom=datazoom_opts)
        return self


class Chart3D(Chart):
    """
    `Chart3D`类是所有 3D 类图表的基类，继承自 `Chart` 类
    """

    def __init__(self, init_opts: InitOpts = InitOpts()):
        init_opts.renderer = RENDER_TYPE.canvas
        super().__init__(init_opts)
        self.js_dependencies.add("echartsgl")
        self._3d_chart_type = None  # 3d chart type, don't use it directly

    def add(
        self,
        name: str,
        data: ListTuple,
        opacity: Numeric = 1,
        shading: Optional[str] = None,
        label_opts: LabelOpts = LabelOpts(),
        xaxis3d: Axis3DOpts = Axis3DOpts(),
        yaxis3d: Axis3DOpts = Axis3DOpts(),
        zaxis3d: Axis3DOpts = Axis3DOpts(),
    ):

        self.options.get("legend")[0].get("data").append(name)
        self.options.update(
            xAxis3D=xaxis3d.opts,
            yAxis3D=yaxis3d.opts,
            zAxis3D=zaxis3d.opts,
            # grid3D=chart["grid3D"],
        )

        self.options.get("series").append(
            {
                "type": self._3d_chart_type,
                "name": name,
                "data": data,
                "label": label_opts.opts,
                "shading": shading,
                "itemStyle": {"opacity": opacity},
            }
        )
