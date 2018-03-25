> Datasets:This article describes the raw data and acces interface for builtin data.

## Overview

pyecharts contains a lot of data of geography and map, which is provided or can be installed and loaded.

## Geography Coordinates

### Raw Data

pyecharts contains some coordinates of cities, which are stored in the variable `pyecharts.datasets.coordinates._COORDINATE_DATASET` .

The format can be described as the following:

```
{<name>: [<longitude>, <latitude>]}
```

Example:

```python
_COORDINATE_DATASET = {
    '阿城': [126.58, 45.32],
    '阿克苏': [80.19, 41.09],
    '阿勒泰': [88.12, 47.50],
    ...
}
```

### Get Coordinate

Function `get_coordinate(name)` returns coordinate for a city name.This funcion will return `None` if not found.

```python
from pyecharts.datasets.coordinates import get_coordinate

coordinate = get_coordinate('北京')
print(coordinate) # [116.46, 39.92]

coordinate1 = get_coordinate('A市')
print(coordinate1) # None
```

### Search Coordindates by Keyword

Function `search_coordinates_by_keyword(*args)` returns result list with one or multiple keywords.

Usage 1: Use single keyword

```python
from pyecharts.datasets.coordinates import search_coordinates_by_keyword

result = search_coordinates_by_keyword('北京')
print(result) # {'北京':[116.46, 39.92], '北京市': [116.4, 39.9]}
```

Usage 2: Use multiple keywords

```python
from pyecharts.datasets.coordinates import search_coordinates_by_keyword
result = search_coordinates_by_keyword('福州', '杭州')
print(result) # {'福州市': [119.3, 26.08], '杭州市': [120.15, 30.28] ...} 
```

### Search Coordindates by Filter Function

Function `search_coordinates_by_filter(func)` returns result list with filter function.

Usage : Use filter function

```python
from pyecharts.datasets.coordinates import search_coordinates_by_filter

result = search_coordinates_by_filter(
    func=lambda name: '福州' in name or '杭州' in name
)
print(result)
```

## Map Data

All map are hosted on  https://github.com/echarts-maps 。