> 图表风格篇：本篇文档为 pyecharts 图表风格详情文档。

> 重要：从 v0.6.0 开始，类 Style 已经废弃。可以使用原生 dict 代替。

为了简化配置项编写，提供了一个 Style 类，可用于在同一个图或者多个图内保持统一的风格

## 初始化图
```python
from pyecharts import Style

style = Style(
    title_color="#fff",
    title_pos="center",
    width=1100,
    height=600,
    background_color='#404a59'
)
# style.init_style 会返回类初始化的风格配置字典
geo = Geo("全国主要城市空气质量", "data from pm2.5", **style.init_style)
```

## 增加图例
```python
pie = Pie('各类电影中"好片"所占的比例', "数据来着豆瓣", title_pos='center')
# 使用 Style.add() 可配置增加图例的风格配置字典
pie_style = style.add(
    radius=[18, 24],
    label_pos="center",
    is_label_show=True,
    label_text_color=None
)
pie.add("", ["剧情", ""], [25, 75], center=[10, 30], **pie_style)
pie.add("", ["奇幻", ""], [24, 76], center=[30, 30], **pie_style)
pie.add("", ["爱情", ""], [14, 86], center=[50, 30], **pie_style)
pie.add("", ["惊悚", ""], [11, 89], center=[70, 30], **pie_style)
```
这样会使得每个图例都会按照设定的风格
