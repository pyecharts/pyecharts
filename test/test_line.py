from echarts import Line

def test_line():
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 10, 100]
    v2 = [55, 60, 16, 20, 15, 80]

    line = Line()
    line.add("商家A", attr, v1, is_symbol_show=False, is_smooth=True, area_opacity=0.2, label_color=['#123'])
    line.add("商家B", attr, v2, is_symbol_show=False, is_smooth=True, mark_line=["max", "average"])
    line.show_config()
    line.render()