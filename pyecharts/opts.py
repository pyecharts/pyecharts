from typing import Optional, Union


class TitleOpts:
    def __init__(
        self,
        title: str,
        subtitle: str = "",
        title_left: str = "auto",
        title_top: str = "auto",
        title_color: Optional[str] = None,
        title_text_size: Optional[int, float] = None,
        subtitle_color: Optional[str] = None,
        subtitle_text_size: Optional[int, float] = None,
    ):
        self.opts = (
            [
                {
                    "text": title,
                    "subtext": subtitle,
                    "left": title_left,
                    "top": title_top,
                    "textStyle": {"color": title_color, "fontSize": title_text_size},
                    "subtextStyle": {
                        "color": subtitle_color,
                        "fontSize": subtitle_text_size,
                    },
                }
            ],
        )


class DataZoomOpts:
    def __init__(
        self,
        is_show: bool = False,
        type: str = "slider",
        range_start: Union[int, float] = 50,
        range_end: Union[int, float] = 100,
        orient: str = "horizontal",
        xaxis_index: int = 0,
        yaxis_index: int = 0,
    ):
        self.opts = {
            "show": is_show,
            "type": type,
            "start": range_start,
            "end": range_end,
            "orient": orient,
            "xAxisIndex": xaxis_index,
            "yAxisIndex": yaxis_index,
        }


class LegendOpts:
    def __init__(
        self,
        selected_mode: str,
        is_show: bool = True,
        left: Optional[str] = None,
        top: Optional[str] = None,
        orient: Optional[str] = None,
        text_size: Optional[float, int] = None,
        text_color: Optional[str] = None,
    ):
        self.opts = {
            "selectedMode": selected_mode,
            "show": is_show,
            "left": left,
            "top": top,
            "orient": orient,
            "textStyle": {"fontSize": text_size, "color": text_color},
        }


class VisualMapOpts:
    def __init__(
        self,
        type: str = "color",
        range_min: Union[int, float] = 0,
        range_max: Union[int, float] = 100,
        text_color: Optional[str] = None,
        range_text: Union[list, tuple] = None,
        range_color=None,
        range_size=None,
        orient="vertical",
        visual_pos="left",
        visual_top="bottom",
        visual_split_number=5,
        visual_dimension=None,
        is_calculable=True,
        is_piecewise=False,
        pieces=None,
    ):

        _inrange_op = {}
        if type == "color":
            range_color = ["#50a3ba", "#eac763", "#d94e5d"]
            if range_color and len(range_color) >= 2:
                range_color = range_color
            _inrange_op.update(color=range_color)

        if type == "size":
            range_size = [20, 50]
            if range_size:
                if len(range_size) >= 2:
                    range_size = range_size
            _inrange_op.update(symbolSize=range_size)

        _type = "piecewise" if is_piecewise else "continuous"

        self.ops = {
            "type": _type,
            "min": range_min,
            "max": range_max,
            "text": range_text,
            "textStyle": {"color": text_color},
            "inRange": _inrange_op,
            "calculable": is_calculable,
            "splitNumber": visual_split_number,
            "dimension": visual_dimension,
            "orient": orient,
            "left": visual_pos,
            "top": visual_top,
            "showLabel": True,
        }
        if is_piecewise:
            self.ops.update(pieces=pieces)


class Tooltip:
    def __init__(
        self,
        trigger="item",
        trigger_on="mousemove|click",
        axispointer_type="line",
        formatter=None,
        text_color=None,
        text_size=14,
        background_color="rgba(50,50,50,0.7)",
        border_color="#333",
        border_width=0,
        **kwargs
    ):
        """
        提示框组件，用于移动或点击鼠标时弹出数据内容

        :param tooltip_trigger:
            触发类型。默认为 'item'
                'item': 数据项图形触发，主要在散点图，饼图等无类目轴的图表中使用。
                'axis': 坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用。
                'none': 什么都不触发。
        :param tooltip_trigger_on:
            提示框触发的条件。默认为 "mousemove|click"
                'mousemove': 鼠标移动时触发。
                'click': 鼠标点击时触发。
                'mousemove|click': 同时鼠标移动和点击时触发。
                'none': 不在 'mousemove' 或 'click' 时触发
        :param tooltip_axispointer_type:
            指示器类型。默认为 "line"
                'line': 直线指示器
                'shadow': 阴影指示器
                'cross': 十字准星指示器。其实是种简写，表示启用两个正交的轴的 axisPointer。
        :param tooltip_formatter:
            模板变量有 {a}, {b}，{c}，{d}，{e}，分别表示系列名，数据名，数据值等。
            使用示例，如 label_formatter='{a}'
            在 trigger 为 'axis' 的时候，会有多个系列的数据，此时可以通过 {a0}, {a1}, {a2}
            这种后面加索引的方式表示系列的索引。不同图表类型下的 {a}，{b}，{c}，{d} 含义不一样。
            其中变量 {a}, {b}, {c}, {d} 在不同图表类型下代表数据含义为：
                折线（区域）图、柱状（条形）图、K线图 :
                    {a}（系列名称），{b}（类目值），{c}（数值）, {d}（无）
                散点图（气泡）图 :
                    {a}（系列名称），{b}（数据名称），{c}（数值数组）, {d}（无）
                地图 :
                    {a}（系列名称），{b}（区域名称），{c}（合并数值）, {d}（无）
                饼图、仪表盘、漏斗图:
                    {a}（系列名称），{b}（数据项名称），{c}（数值）, {d}（百分比）
            yaxis_formatter -> function

            def tooltip_formatter(params):
                return params.value + ' [Good!]'

            回调函数格式，更多内容请参考 [高级用法篇](zh-cn/advanced)
            ```
            (params: Object|Array) => string
            参数 params 是 formatter 需要的单个数据集。格式如下：
            {
                componentType: 'series',
                // 系列类型
                seriesType: string,
                // 系列在传入的 option.series 中的 index
                seriesIndex: number,
                // 系列名称
                seriesName: string,
                // 数据名，类目名
                name: string,
                // 数据在传入的 data 数组中的 index
                dataIndex: number,
                // 传入的原始数据项
                data: Object,
                // 传入的数据值
                value: number|Array,
                // 数据图形的颜色
                color: string,
            }
        :param tooltip_text_color:
            提示框字体颜色，默认为 '#fff'
        :param tooltip_font_size:
            提示框字体大小，默认为 14
        :param tooltip_background_color:
            提示框浮层的背景颜色。默认为 "rgba(50,50,50,0.7)"
        :param tooltip_border_color:
            提示框浮层的边框颜色。默认为 "#333"
        :param tooltip_border_width:
            提示框浮层的边框宽。默认为 0
        """
        self.opts = {
            "trigger": trigger,
            "triggerOn": trigger_on,
            "axisPointer": {"type": axispointer_type},
            "formatter": formatter,
            "textStyle": {"color": text_color, "fontSize": text_size},
            "backgroundColor": background_color,
            "borderColor": border_color,
            "borderWidth": border_width,
        }
