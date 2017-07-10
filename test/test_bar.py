from pyecharts import Bar, Line

def test_bar():
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    v3 = [first + second + 35 for first, second in zip(v1, v2)]

    bar = Bar("TITLE", "SUBTITLE")
    bar.add("B", attr, v2, isstack=True)
    bar.add("A", attr, v1, label_text_size=20, isstack=True)
    line = Line()
    line.add("C", attr, v3, label_text_size=20)
    bar.custom(line.get_series())
    bar.show_config()
    bar.render()
