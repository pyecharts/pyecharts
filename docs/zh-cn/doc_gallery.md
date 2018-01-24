用极坐标系画出一个爱心
```python
import math
from pyecharts import Polar

data = []
for i in range(101):
    theta = i / 100 * 360
    r = 5 * (1 + math.sin(theta / 180 * math.pi))
    data.append([r, theta])
hour = [i for i in range(1, 25)]
polar = Polar("极坐标系示例", width=1200, height=600)
polar.add("Love", data, angle_data=hour, boundary_gap=False,start_angle=0)
polar.render()
```
![example-0](https://user-images.githubusercontent.com/19553554/35080754-8a01a508-fc4a-11e7-8be4-5da46e27103d.png)


用极坐标系画出一朵小花
```python
import math
from pyecharts import Polar

data = []
for i in range(361):
    t = i / 180 * math.pi
    r = math.sin(2 * t) * math.cos(2 * t)
    data.append([r, i])
polar = Polar("极坐标系示例", width=1200, height=600)
polar.add("Flower", data, start_angle=0, symbol=None, axis_range=[0, None])
polar.render()
```
![example-1](https://user-images.githubusercontent.com/19553554/35080781-b029db60-fc4a-11e7-8789-a4070845d56a.png)


还可以给小花涂上颜色
```python
import math
from pyecharts import Polar

data = []
for i in range(361):
    t = i / 180 * math.pi
    r = math.sin(2 * t) * math.cos(2 * t)
    data.append([r, i])
polar = Polar("极坐标系示例", width=1200, height=600)
polar.add("Color-Flower", data, start_angle=0, symbol=None,
          axis_range=[0, None], area_color="#f71f24", area_opacity=0.6)
polar.render()
```
![example-2](https://user-images.githubusercontent.com/19553554/35080790-c61a8ac8-fc4a-11e7-9a47-8e352b944358.png)


用散点图画出一个爱心
```python
from pyecharts import Scatter

scatter = Scatter("散点图示例", width=800, height=480)
v1 ,v2 = scatter.draw("../images/love.png")
scatter.add("Love", v1, v2)
scatter.render()
```
![example-3](https://user-images.githubusercontent.com/19553554/35080813-eda5885e-fc4a-11e7-9f77-3856dced269e.png)


用散点图画出一个火辣的 Bra
```python
from pyecharts import Scatter

scatter = Scatter("散点图示例", width=1000, height=480)
v1 ,v2 = scatter.draw("../images/cup.png")
scatter.add("Cup", v1, v2)
scatter.render()
```
![example-4](https://user-images.githubusercontent.com/19553554/35080804-e0a587e4-fc4a-11e7-9b38-f4defac97b37.png)


用散点图画出一个性感的 Bra
```python
from pyecharts import Scatter

scatter = Scatter("散点图示例", width=1000, height=480)
v1 ,v2 = scatter.draw("../images/cup.png")
scatter.add("Cup", v1, v2, label_color=["#000"])
scatter.render()
```
![example-5](https://user-images.githubusercontent.com/19553554/35080805-e1eec020-fc4a-11e7-8aa2-2d9d58fce144.png)


用极坐标系画出一个蜗牛壳
```python
import math
from pyecharts import Polar

data = []
for i in range(5):
    for j in range(101):
        theta = j / 100 * 360
        alpha = i * 360 + theta
        r = math.pow(math.e, 0.003 * alpha)
        data.append([r, theta])
polar = Polar("极坐标系示例")
polar.add("", data, symbol_size=0, symbol='circle', start_angle=-25,
          is_radiusaxis_show=False, area_color="#f3c5b3",
          area_opacity=0.5, is_angleaxis_show=False)
polar.render()
```
![example-6](https://user-images.githubusercontent.com/19553554/35080856-3cc8eaf2-fc4b-11e7-8ba8-5fdc9e3c64e8.png)
