from echarts import Pie

def test_pie():
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    value = [11, 12, 13, 10, 10, 10]
    pie = Pie()
    pie.add("商品", attr, value, label_show=True, rand_data=True, rad=[30, 70])
    pie.show_config()
    pie.render()