from pyecharts import Map

def test_map():
    value = [20, 190]
    attr = ['福州市', '厦门市']
    map = Map(width=1200, height=600)
    map.add("地图", attr, value, maptype='福建')
    map.show_config()
    map.render()