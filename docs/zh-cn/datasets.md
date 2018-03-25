> 数据集 篇：本文档主要介绍 pyecharts 项目相关的原始数据和访问接口。

## 概述

pyecharts 项目包含了一系列的地理地图数据，这些数据或者已经内置，或者需要额外安装和加载。

## 地理经纬度坐标

### 原始数据

pyecharts 内置了一些常用的城市地理坐标数据，这些数据保存在 `pyecharts.datasets.coordinates._COORDINATE_DATASET` 这个字典常量中，格式可描述为以下形式：

```
{<name>: [<longitude>, <latitude>]}
```

示例

```python
_COORDINATE_DATASET = {
    '阿城': [126.58, 45.32],
    '阿克苏': [80.19, 41.09],
    '阿勒泰': [88.12, 47.50],
    ...
}
```

### 检索地理坐标

`get_coordinate(name)` 返回城市名称的地理坐标，如果未定义将返回 None 。

```python
from pyecharts.datasets.coordinates import get_coordinate

coordinate = get_coordinate('北京')
print(coordinate) # [116.46, 39.92]

coordinate1 = get_coordinate('A市')
print(coordinate1) # None
```

### 按关键字搜索地理坐标

`search_coordinates_by_keyword(*args)` 根据一个或多个关键字，返回一个匹配的字典对象。

用法1：单个关键字模糊搜索

```python
from pyecharts.datasets.coordinates import search_coordinates_by_keyword

result = search_coordinates_by_keyword('北京')
print(result) # {'北京':[116.46, 39.92], '北京市': [116.4, 39.9]}
```

用法2：多个关键字模糊搜索

```python
from pyecharts.datasets.coordinates import search_coordinates_by_keyword
result = search_coordinates_by_keyword('福州', '杭州')
print(result) # {'福州市': [119.3, 26.08], '杭州市': [120.15, 30.28] ...} 
```

### 按过滤函数搜索地理坐标

`search_coordinates_by_filter(func)` 根据过滤函数，返回一个匹配的字典对象。
用法（结果同上）

```python
from pyecharts.datasets.coordinates import search_coordinates_by_filter

result = search_coordinates_by_filter(
    func=lambda name: '福州' in name or '杭州' in name
)
print(result)
```

## 地图数据

地图数据均托管在 https://github.com/echarts-maps 。