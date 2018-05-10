> 主题自定义篇：扩展主题插件，多样化图表配色。V0.5.2+ 新增

自 0.5.2+ 起，pyecharts 支持更换主题。下面是更换为 "dark" 的例子：

```python
import random

from pyecharts import Bar


X_AXIS = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
bar = Bar("我的第一个图表", "这里是副标题")
bar.use_theme("dark")
bar.add("商家A", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家B", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家C", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家D", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.render()
```
![dark](https://user-images.githubusercontent.com/19553554/39868563-c136646a-548c-11e8-87c2-dbf7ae85e844.png)

默认主题的效果

![default](https://user-images.githubusercontent.com/19553554/39868566-c20b699e-548c-11e8-861f-5a1b063434c3.png)

## 如何获得更多主题

[echarts-themes-pypkg](https://github.com/pyecharts/echarts-themes-pypkg) 提供了 `dark`, `vintage`, `macarons`, `infographic`, `shine` 和 `roma` 主题。

### 安装主题插件

```shell
$ pip install echarts-themes-pypkg
```

### 使用主题

```python
bar.use_theme("vintage")    # 更换为你喜欢的主题
```

### 示例

**vintage**

![vintage](https://user-images.githubusercontent.com/19553554/39620159-d42defa4-4fbc-11e8-8e8d-ea9158434ea0.png)

**macarons**

![macarons](https://user-images.githubusercontent.com/19553554/39868570-c3563a0e-548c-11e8-9795-e0ebea18853f.png)

**infographic**

![infographic](https://user-images.githubusercontent.com/19553554/39868564-c1884dac-548c-11e8-9009-f61162759be3.png)

**shine**

![shine](https://user-images.githubusercontent.com/19553554/39868565-c1c8951a-548c-11e8-8351-2973cce47679.png)

**roma**

![roma](https://user-images.githubusercontent.com/19553554/39868568-c2c7b798-548c-11e8-9de8-3d3ae148f172.png)
