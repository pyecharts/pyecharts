> 主题自定义篇：适用在 pyecharts v0.5.2 以后的版本。

自 0.5.2+ 起，pyecharts 支持更换主体色系。下面是更换为 'dark' 的例子：

```python
from pyecharts import Bar

bar = Bar("我的第一个图表", "这里是副标题")
bar.use_theme('dark')
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar.render()
```
![guide-2](https://user-images.githubusercontent.com/4280312/39617664-79789878-4f78-11e8-9f0e-c3a2c371b6cb.png)

## 如何获得更多主题

伴随 pyecharts v0.5.2, [echarts-themes-pypkg](https://github.com/pyecharts/echarts-themes-pypkg) 提供 vintage, macarons, infographic, shine 和 roma 主题。

## 安装主题插件

```shell
$ pip install echarts-themes-pypkg
```

## 使用主题

```python
bar.use_theme('vintage')    # 更换为你喜欢的主题
```

## 示例

### vintage:

![vintage](https://user-images.githubusercontent.com/19553554/39620159-d42defa4-4fbc-11e8-8e8d-ea9158434ea0.png)

### macarons:

![macarons](https://user-images.githubusercontent.com/19553554/39620161-d529169a-4fbc-11e8-9864-c246f9a2f677.png)

### infographic

![infographic](https://user-images.githubusercontent.com/19553554/39620158-d3e6bfc6-4fbc-11e8-9564-9d2d9f62b2be.png)

### shine:

![shine](https://user-images.githubusercontent.com/19553554/39620177-d6fd0a3a-4fbc-11e8-8abc-a99f6d1f9f74.png)

### roma:

![roma](https://user-images.githubusercontent.com/19553554/39620162-d57380e0-4fbc-11e8-872b-2c1c43b7a1a4.png)
