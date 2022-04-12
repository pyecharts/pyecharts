# encoding: utf-8
"""
@file: test_stack2.py
@desc:
@author: guozhen3
@time: 2022/2/18
"""

import pandas as pd
from pyecharts.charts import Bar

data = pd.read_csv("test.csv")
data["base_vol"] = data["chg"].map(lambda x: -x if x > 0 else 0) + data["vol"]

bar = (
Bar()
.add_xaxis(xaxis_data=data["item"].tolist())
.add_yaxis(
series_name="Position Vol",
y_axis=data["base_vol"].tolist(),
color="LightSeaGreen",
stack="vol"
)
.add_yaxis(
series_name="Increased",
y_axis=data["chg"].map(lambda x: x if x > 0 else 0).tolist(),
color="red",
stack="vol"
).add_yaxis(
series_name="Dcreased",
y_axis=data["chg"].map(lambda x: -x if x < 0 else 0).tolist(),
color="green",
stack="vol"
)


)
bar.render()