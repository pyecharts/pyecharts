from echarts import Gauge

def test_gague():
    gauge = Gauge()
    gauge.add("业务指标", "完成率", 66.66, angle_range=[180, 0])
    gauge.show_config()
    gauge.render()