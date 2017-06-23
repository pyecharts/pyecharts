from echarts import Line

def test_line():
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    value_A = [5, 20, 36, 10, 10, 100]
    value_B = [55, 60, 16, 14, 15, 80]
    line = Line()
    line.add("商家A", attr, value_A, mark_point=["max", "min", "average"])
    line.add("商家B", attr, value_B, mark_line=["max", "min", "average"])
    line.show_config()
    line.render()