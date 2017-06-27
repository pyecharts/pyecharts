from echarts import Line

def test_line():
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    value_A = [5, 20, 36, 10, 10, 100]
    value_B = [55, 60, 16, 20, 15, 80]

    line = Line()
    line.add("商家A", attr, value_A, is_symbol_show=False, is_smooth=True, is_fill=True, area_opacity=0.2)
    # line.add("商家B", attr, value_B, is_symbol_show=False, is_smooth=True, is_fill=True, area_opacity=0.2)
    line.show_config()
    line.render()