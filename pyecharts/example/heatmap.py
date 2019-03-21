import random

from pyecharts.charts import HeatMap

x_axis = [
    "12a",
    "1a",
    "2a",
    "3a",
    "4a",
    "5a",
    "6a",
    "7a",
    "8a",
    "9a",
    "10a",
    "11a",
    "12p",
    "1p",
    "2p",
    "3p",
    "4p",
    "5p",
    "6p",
    "7p",
    "8p",
    "9p",
    "10p",
    "11p",
]

y_axis = ["Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"]
value = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]

hm = HeatMap()
hm.add_xaxis(x_axis).add_yaxis("series0", y_axis, value).render()
