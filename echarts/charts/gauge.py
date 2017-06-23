from echarts.base import Base

class Gauge(Base):

    def __init__(self, title="", subtitle="", **kwargs):
        super().__init__(title, subtitle, **kwargs)

    def add(self, *args, **kwargs):
        self._add(*args, **kwargs)

    def _add(self, name, attr, value):
        self._option.update(tooltip={"formatter": "{a} <br/>{b} : {c}%"})
        self._option.get('series').append({
            "detail": {"formatter": '{value}%'},
            "name": name,
            "type": "gauge",
            "data": [{"value": value, "name": attr}]
        })

if __name__ == "__main__":
    gauge = Gauge()
    gauge.add("业务指标", "完成率", 66.66)
    gauge.show_config()
    gauge.render()
