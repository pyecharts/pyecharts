> Chart Style : This document is a pyecharts chart style detail document.

To simplify writing configuration items, a Style class is provided that can be used to maintain a uniform style in the same or multiple charts.

## Initialize Style
```python
from pyecharts import Style

style = Style(
    title_color="#fff",
    title_pos="center",
    width=1100,
    height=600,
    background_color='#404a59'
)
# style.init_style will return the Style class initialization dictionary
geo = Geo("全国主要城市空气质量", "data from pm2.5", **style.init_style)
```

## Update Style
```python
pie = Pie('各类电影中"好片"所占的比例', "数据来着豆瓣", title_pos='center')
# Use Style.add() to update the Style class dictionary
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
This will make each chart follow the custom style.
