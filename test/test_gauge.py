from echarts import Gauge

def test_gague():
    gauge = Gauge("")
    gauge.add("业务指标", 66.66, "完成率")
    gauge.show_config()
    gauge.render()