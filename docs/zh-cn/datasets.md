> 数据集篇：本文档主要介绍 pyecharts 项目相关的原始数据和访问接口。

## 概述

pyecharts 项目包含了一系列的地理地图数据，这些数据或者已经内置，或者需要额外安装和加载。

从 v0.5.0 开始，pyecharts 重构了内部代码，不再支持对原有数据存储对象进行修改，对外提供了这些数据的访问接口。

## 地理经纬度坐标

### 原始数据

pyecharts 内置了一些常用的城市地理坐标数据，这些数据保存在 *pyecharts/datasets/city_coordinates.json* 文件中。格式可描述为以下形式：

```
{<name>: [<longitude>, <latitude>]}
```

示例

```json
{
    "阿城": [126.58, 45.32],
    "阿克苏": [80.19, 41.09],
    "阿勒泰": [88.12, 47.50],
    ...
}
```

### 提供自定义数据

具体可参考 [pyecharts/geo-region-coords](https://github.com/pyecharts/geo-region-coords)


### 检索中国地理坐标

`get_coordinate(name, region="中国")` 返回城市名称的地理坐标，如果未定义将返回 None 。

```python
from pyecharts.datasets.coordinates import get_coordinate

coordinate = get_coordinate('北京')
print(coordinate) # [116.46, 39.92]

coordinate1 = get_coordinate('A市')
print(coordinate1) # None
```

### 按关键字搜索地理坐标

`search_coordinates_by_keyword(*args)` 根据一个或多个关键字，返回一个匹配的字典对象。

用法 1：单个关键字模糊搜索

```python
from pyecharts.datasets.coordinates import search_coordinates_by_keyword

result = search_coordinates_by_keyword('北京')
print(result) # {'北京':[116.46, 39.92], '北京市': [116.4, 39.9]}
```

用法 2：多个关键字模糊搜索

```python
from pyecharts.datasets.coordinates import search_coordinates_by_keyword
result = search_coordinates_by_keyword('福州', '杭州')
print(result) # {'福州市': [119.3, 26.08], '杭州市': [120.15, 30.28] ...}
```

### 按过滤函数搜索地理坐标

`search_coordinates_by_filter(func, region="中国")` 根据过滤函数，返回一个匹配的字典对象。
用法（结果同上）

```python
from pyecharts.datasets.coordinates import search_coordinates_by_filter

result = search_coordinates_by_filter(
    func=lambda name: '福州' in name or '杭州' in name
)
print(result)
```

### 使用例子

Geo/Geolines:

* `add_coordinate` 用于新增一个自定义城市地理位置的功能。
* `add_coordinate_json`  用于导入自定义地理位置 JSON 文件。

方法接口如下：

```
class Geo:
    add_coordinate(self, name: six.text_type, longitude: float, latitude: float): -> None
    """
    example:
        add_coordinate("某地", 100.0, 20.0)
    """
    
    # v0.5.9+
    add_coordinate_json(self, json_file: six.text_type): -> None
    """
    example:
        add_coordinate_json("my_coords.json")
    """

    # my_coords.json
    """
    {
        "某地": [100.0, 20.0],
        ...
    }
    """
```

整个使用例子如下：

```python
from pyecharts import Geo

data = [('广州', 45), ('漳州', 35), ('A市', 43)]
geo = Geo("全国主要城市空气质量", "data from pm2.5", **style.init_style)
attr, value = geo.cast(data)
geo.add_coordinate('A市', 119.3, 26.08) # 添加 pyecharts 未提供的城市地理坐标
geo.add(
    "全国主要城市空气质量",
    attr,
    value,
    type="effectScatter",
    is_random=True,
    is_visualmap=True,
    is_piecewise=True,
    visual_text_color="#fff",
    pieces=[
        {"min": 0, "max": 13, "label": "0 < x < 13"},
        {"min": 14, "max": 16, "label": "14 < x < 16"},
    ],
    effect_scale=5,
)
geo.render()
```

## 国际城市地理坐标

自 v0.5.7 之后，[echarts-cities-pypkg](https://github.com/pyecharts/echarts-cities-pypkg) 给 pyecharts 补充了 [138,398 个城市地理坐标](https://github.com/echarts-maps/echarts-cities-js)，覆盖了200 多个国家。你可以配合 echarts-countries-pypkg 画地理散点图。

### 安装方法

```
pip install echarts-cities-pypkg
```

### 使用方法

```python
from pyecharts.datasets.coordinates import get_coordinate

coordinate = get_coordinate('Oxford', region="英国")
print(coordinate) # [-1.25596, 51.75222]
```

### 按关键字搜索地理坐标

`search_coordinates_by_region_and_keyword(*args)` 根据一个或多个关键字，返回一个匹配的字典对象。

用法 1：单个关键字模糊搜索

```python
from pyecharts.datasets.coordinates import search_coordinates_by_region_and_keyword

result = search_coordinates_by_region_and_keyword("英国", 'London')
print(result)
#{
#    "Londonderry County Borough": [-7.30917, 54.99721],
#    "City of London": [-0.09184, 51.51279],
#    "London": [-0.12574, 51.50853],
#}
```

用法 2：多个关键字模糊搜索

```python
from pyecharts.datasets.coordinates import search_coordinates_by_region_and_keyword
result = search_coordinates_by_region_and_keyword('中国香港', 'Central', 'Hong Kong')
print(result) # { "Hong Kong": [114.15769, 22.28552], "Central": [114.15846, 22.28299]}
```

### 按过滤函数搜索地理坐标

```python
from pyecharts.datasets.coordinates import search_coordinates_by_filter

result = search_coordinates_by_filter(
    func=lambda name: "Central" in name or "Hong Kong" in name,
    region="中国香港",

)
print(result) # { "Hong Kong": [114.15769, 22.28552], "Central": [114.15846, 22.28299]}
```

## 地图数据

以下是 pyecharts 开发组托管的地图扩展（map extension）:

1. [World countries include China map and World map](https://echarts-maps.github.io/echarts-countries-js/): [echarts-countries-pypkg](https://github.com/pyecharts/echarts-countries-pypkg) (1.9MB)
2. [Chinese provinces and regions](https://echarts-maps.github.io/echarts-china-provinces-js/): [echarts-china-provinces-pypkg](https://github.com/pyecharts/echarts-china-provinces-pypkg) (730KB)
3. [Chinese cities](https://echarts-maps.github.io/echarts-china-cities-js/): [echarts-china-cities-pypkg](https://github.com/pyecharts/echarts-china-cities-pypkg) (3.8MB)
4. [Chinese counties](https://echarts-maps.github.io/echarts-china-counties-js/): [echarts-china-counties-pypkg](https://github.com/pyecharts/echarts-china-counties-pypkg) (4.1MB)
5. [Custom Chinese regions](https://echarts-maps.github.io/echarts-china-misc-js/): [echarts-china-misc-pypkg](https://github.com/pyecharts/echarts-china-misc-pypkg) (148KB)
6. [United Kingdom map](https://echarts-maps.github.io/echarts-united-kingdom-js/): [echarts-united-kingdom-pypkg](https://github.com/pyecharts/echarts-united-kingdom-pypkg) (1MB)

更多的地图数据可查看 https://github.com/echarts-maps 。

可以使用 *pip* 安装这些地图扩展。

```bash
$ pip install echarts-countries-pypkg
$ pip install echarts-china-provinces-pypkg
$ pip install echarts-china-cities-pypkg
$ pip install echarts-china-counties-pypkg
$ pip install echarts-china-misc-pypkg
$ pip install echarts-united-kingdom-pypkg
```
