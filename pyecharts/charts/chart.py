# coding=utf-8

import uuid

from ..charts.base import Base
from ..commons.consts import COLOR_LST, RENDER_TYPE, CHART_TYPE
from ..options import (
    Axis3DOpts,
    AxisLineOpts,
    AxisOpts,
    DataZoomOpts,
    InitOpts,
    LabelOpts,
    LegendOpts,
    LineStyleOpts,
    MarkLineOpts,
    MarkPointOpts,
    SplitLineOpts,
    TitleOpts,
    ToolboxOpst,
    TooltipOpts,
    VisualMapOpts,
)
from pyecharts.commons.types import ListTuple, Numeric, Optional, Union


class Chart(Base):
    """
    `Chart`类是所有非自定义类的基类，继承自 `Base` 类
    """

    def __init__(self, init_opts: Union[InitOpts, dict] = InitOpts()):
        super().__init__(init_opts=init_opts)
        self._colorlst = COLOR_LST
        self.options.update(
            series_id=uuid.uuid4().hex, series=[], legend=[{"data": []}]
        )
        _chart_type = "!"

    def set_series_opts(
        self,
        label_opts: Union[LabelOpts, dict, None] = None,
        linestyle_opts: Union[LineStyleOpts, dict, None] = None,
        splitline_opts: Union[SplitLineOpts, dict, None] = None,
        axisline_opts: Union[AxisLineOpts, dict, None] = None,
        markpoint_opts: Union[MarkPointOpts, dict, None] = None,
        markline_opts: Union[MarkLineOpts, dict, None] = None,
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
        title_opts: Union[TitleOpts, dict] = TitleOpts(),
        toolbox_opts: Union[ToolboxOpst, dict] = ToolboxOpst(),
        tooltip_opts: Union[TooltipOpts, dict] = TooltipOpts(),
        legend_opts: Union[LegendOpts, dict] = LegendOpts(),
        xaxis_opt: Union[AxisOpts, dict, None] = None,
        yaxis_opt: Union[AxisOpts, dict, None] = None,
        visualmap_opts: Union[VisualMapOpts, dict, None] = None,
        datazoom_opts: Union[DataZoomOpts, dict, None] = None,
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

        # TODO: xaxis -> list
        if xaxis_opt and self.options.get("xAxis", None):
            if isinstance(xaxis_opt, AxisOpts):
                xaxis_opt = xaxis_opt.opts
                for x in self.options["xAxis"]:
                    x.update(xaxis_opt)

        # TODO: yaxis -> list
        if yaxis_opt and self.options.get("yAxis", None):
            if isinstance(yaxis_opt, AxisOpts):
                yaxis_opt = yaxis_opt.opts
                for y in self.options["yAxis"]:
                    y.update(yaxis_opt)

        if visualmap_opts:
            if isinstance(visualmap_opts, VisualMapOpts):
                visualmap_opts = visualmap_opts.ops
            self.options.update(visualMap=visualmap_opts)

        if datazoom_opts:
            if isinstance(datazoom_opts, DataZoomOpts):
                datazoom_opts = datazoom_opts.opts
            self.options.update(dataZoom=datazoom_opts)
        return self


class AxisChart(Chart):
    def extend_axis(
        self, xaxis: Optional[AxisOpts] = None, yaxis: Optional[AxisOpts] = None
    ):
        if xaxis:
            if isinstance(xaxis, AxisOpts):
                xaxis = xaxis.opts
            self.options["xAxis"].append(xaxis)
        if yaxis:
            if isinstance(yaxis, AxisOpts):
                yaxis = yaxis.opts
            self.options["yAxis"].append(yaxis)

    def add_xaxis(self, xaxis_data: ListTuple):
        self.options.update(xAxis=[AxisOpts().opts])
        self.options["xAxis"][0].update(data=xaxis_data)
        self._xaxis_data = xaxis_data
        return self


class Chart3D(Chart):
    """
    `Chart3D`类是所有 3D 类图表的基类，继承自 `Chart` 类
    """

    def __init__(self, init_opts: Union[InitOpts, dict] = InitOpts()):
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
        label_opts: Union[LabelOpts, dict] = LabelOpts(),
        xaxis3d: Union[Axis3DOpts, dict] = Axis3DOpts(),
        yaxis3d: Union[Axis3DOpts, dict] = Axis3DOpts(),
        zaxis3d: Union[Axis3DOpts, dict] = Axis3DOpts(),
    ):
        if isinstance(label_opts, LabelOpts):
            label_opts = label_opts.opts
        if isinstance(xaxis3d, Axis3DOpts):
            xaxis3d = xaxis3d.opts
        if isinstance(yaxis3d, Axis3DOpts):
            yaxis3d = yaxis3d.opts
        if isinstance(zaxis3d, Axis3DOpts):
            zaxis3d = zaxis3d.opts

        self.options.get("legend")[0].get("data").append(name)
        self.options.update(
            xAxis3D=xaxis3d,
            yAxis3D=yaxis3d,
            zAxis3D=zaxis3d,
            # grid3D=chart["grid3D"],
        )

        self.options.get("series").append(
            {
                "type": self._3d_chart_type,
                "name": name,
                "data": data,
                "label": label_opts,
                "shading": shading,
                "itemStyle": {"opacity": opacity},
            }
        )
