from pyecharts import Pie

def test_pie():
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    v1 = [11, 12, 13, 10, 10, 10]
    v2 = [19, 21, 32, 20, 20, 33]

    pie = Pie()
    # pie.add("商品A", attr, v1, center=[25, 50], is_random=True, radius=[30, 75], rosetype=True, is_label_show=True)
    pie.add("商品B", attr, v2, center=[75, 50], is_random=True, radius=[30, 75], rosetype=True, is_legend_show=False)
    pie.show_config()
    pie.render()