# coding=utf-8
from pyecharts.echarts.json_serializable import JsonSerializable


class Tooltip(JsonSerializable):
    def __init__(
        self,
        tooltip_trigger="item",
        tooltip_trigger_on="mousemove|click",
        tooltip_axispointer_type="line",
        tooltip_formatter=None,
        tooltip_text_color=None,
        tooltip_font_size=14,
        tooltip_background_color="rgba(50,50,50,0.7)",
        tooltip_border_color="#333",
        tooltip_border_width=0,
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
        self._config = {
            "trigger": tooltip_trigger,
            "triggerOn": tooltip_trigger_on,
            "axisPointer": {"type": tooltip_axispointer_type},
            "formatter": tooltip_formatter,
            "textStyle": {
                "color": tooltip_text_color,
                "fontSize": tooltip_font_size,
            },
            "backgroundColor": tooltip_background_color,
            "borderColor": tooltip_border_color,
            "borderWidth": tooltip_border_width,
        }
