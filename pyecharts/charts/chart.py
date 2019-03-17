# coding=utf-8

import uuid

from pyecharts.charts.base import Base
from pyecharts.commons.consts import RENDER_TYPE, COLOR_LST
from pyecharts.commons.types import *
from pyecharts.options import *


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
        label_opts: Optional[LabelOpts] = None,
        linestyle_opts: Optional[LineStyleOpts] = None,
        splitline_opts: Optional[SplitLineOpts] = None,
        axisline_opts: Optional[AxisLineOpts] = None,
        markpoint_opts: Optional[MarkPointOpts] = None,
        markline_opts: Optional[MarkLineOpts] = None,
    ):
        _series = self.options.get("series")
        if label_opts:
            for s in _series:
                s.update(label=label_opts.opts)
        if linestyle_opts:
            for s in _series:
                s.update(lineStyle=linestyle_opts.opts)
        if splitline_opts:
            for s in _series:
                s.update(splitLine=splitline_opts.opts)
        if axisline_opts:
            for s in _series:
                s.update(axisLine=axisline_opts.opts)
        if markpoint_opts:
            for s in _series:
                s.update(markPoint=markpoint_opts.opts)
        if markline_opts:
            for s in _series:
                s.update(markLine=markline_opts.opts)
        return self

    def set_global_opts(
        self,
        title_opts: TitleOpts = TitleOpts(),
        toolbox_opts: ToolboxOpst = ToolboxOpst(),
        tooltip_opts: TooltipOpts = TooltipOpts(),
        legend_opts: LegendOpts = LegendOpts(),
        visualmap_opts: VisualMapOpts = None,
        datazoom_opts: DataZoomOpts = None,
    ):
        self.options.update(
            title=title_opts.opts,
            toolbox=toolbox_opts.opts,
            tooltip=tooltip_opts.opts,
            legend=legend_opts.opts,
        )
        if visualmap_opts:
            self.options.update(visualMap=visualmap_opts.ops)
        if datazoom_opts:
            self.options.update(dataZoom=datazoom_opts.opts)
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
        name,
        data,
        opacity: Numeric = 1,
        shading: str = None,
        label_opts: LabelOpts = LabelOpts(),
        xaxis3d: Axis3DOpts = Axis3DOpts(),
        yaxis3d: Axis3DOpts = Axis3DOpts(),
        zaxis3d: Axis3DOpts = Axis3DOpts(),
    ):

        self.options.get("legend")[0].get("data").append(name)
        self.options.update(
            xAxis3D=xaxis3d.opts,
            yAxis3D=yaxis3d_type.opts,
            zAxis3D=zaxis3d_type.opts,
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
