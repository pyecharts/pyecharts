from pyecharts import Funnel

def test_funnel():
    attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    value = [20, 40, 60, 80, 100, 120]

    funnel = Funnel()
    funnel.add("商品", attr, value, is_label_show=True, label_pos="inside", label_text_color="#fff")
    funnel.show_config()
    funnel.render()