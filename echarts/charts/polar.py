from echarts.base import Base
from echarts.option import get_all_options

class Polar(Base):
    """
    <<< 极坐标系 >>>
    可以用于散点图和折线图。
    """
    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self.__add(*args, **kwargs)

    def __add(self, name, data, *,
              angle_data=None,
              radius_data=None,
              type='line',
              symbol_size=4,
              start_angle=90,
              rotate_step=0,
              boundary_gap=True,
              clockwise=True,
              effect_brushtype="stroke",
              effect_scale=2.5,
              effect_period=4, **kwargs):
        """

        :param name:
            图例名称
        :param data:
            数据项 [极径，极角 [数据值]]
        :param angle_data:
            角度类目数据
        :param radius_data:
            半径类目数据
        :param type:
            图例类型，有 scatter/effectscatter 可选
        :param symbol_size:
            标记图形大小
        :param start_angle:
            起始刻度的角度，默认为 90 度，即圆心的正上方。0 度为圆心的正右方
        :param rotate_step:
            刻度标签旋转的角度，在类目轴的类目标签显示不下的时候可以通过旋转防止标签之间重叠
            旋转的角度从 -90 度到 90 度
        :param boundary_gap:
            坐标轴两边留白策略
            类目轴中 boundaryGap 可以配置为 true 和 false
            默认为 true，这时候刻度只是作为分隔线，标签和数据点都会在两个刻度之间的带(band)中间
        :param clockwise:
            刻度增长是否按顺时针，默认顺时针
        :param effect_brushtype:
            波纹绘制方式，有 stroke/fill 可选
        :param effect_scale:
            动画中波纹的最大缩放比例
        :param effect_period:
            动画的时间
        :param kwargs:
        """
        chart = get_all_options(**kwargs)
        polar_type = 'value' if type == "line" else "category"
        self._option.get('legend').get('data').append(name)
        if type in ("scatter", "line"):
            self._option.get('series').append({
                "type": type,
                "name": name,
                "coordinateSystem": 'polar',
                "symbol": chart['symbol'],
                "symbolSize": symbol_size,
                "data": data,
                "label": chart['label'],
            })
        elif type == "effectScatter":
            self._option.get('series').append({
                "type": type,
                "name": name,
                "coordinateSystem": 'polar',
                "showEffectOn": "render",
                "rippleEffect": {
                    "brushType": effect_brushtype,
                    "scale": effect_scale,
                    "period": effect_period
                },
                "symbol": chart['symbol'],
                "symbolSize": symbol_size,
                "data": data,
                "label": chart['label'],
            })
        self._option.update(
            angleAxis={
                "type": polar_type,
                "data": angle_data,
                "clockwise": clockwise,
                "startAngle": start_angle,
                "boundaryGap": boundary_gap,
                "splitLine": chart['split_line'],
                "axisLine": chart['axis_line']
            }
        )
        self._option.update(
            radiusAxis={
                "type": polar_type,
                "data": radius_data,
                "axisLine": chart['axis_line'],
                "axisLabel": {"rotate": rotate_step}
            }
        )
        self._option.update(polar={})
        self._legend_visualmap_colorlst(**kwargs)
