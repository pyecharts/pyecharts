from echarts.base import Base

class Gauge(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)
        self._option.update(series=[])

    def add(self, name, value, value_name):
        self._option.update(tooltip={"formatter": "{a} <br/>{b} : {c}%"})
        self._option.get('series').append({
            "detail": {"formatter": '{value}%'},
            "name": name,
            "type": "gauge",
            "data": [{"value": value, "name": value_name}]
        })

if __name__ == "__main__":
    gauge = Gauge("业务指标")
    gauge.add("业务指标", 50, "完成率")
    gauge.show_config()
    gauge.render()
