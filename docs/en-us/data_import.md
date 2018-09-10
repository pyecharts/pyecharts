> Data Analysis and Import: Introduces some commonly used data processing modules and libraries. These are not part of the core of pyecharts.

## numpy data

add method, support for the `numpy.array` object, for example:

```python
from pyecharts import Bar
import numpy as np

clothes = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = np.array([5, 20, 36, 10, 75, 90])
bar = Bar("衣服销量")
bar.add("商家A", clothes, v1, is_stack=True)
bar.render()
```

## zip function

In `pyecharts.base.Base.add(name, x_axis, y_axis)` function, data parameters usually require that the lists have equal length.

```python
from pyecharts import Line

t_data = [(21, '2017-12-01'), (19, '2017-12-02'), (20, '2017-12-03')]
hs, ds = zip(*t_data)
line = Line('High Temperature')
line.add('High', ds, hs)
line.render()
```

## Base.cast function

A data formatting handler that converts source data into pyecharts compliant data.

The detailed conversion format is shown as follows:

1. tuple list  
    [(A1, B1), (A2, B2), (A3, B3), (A4, B4)] --> k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]
2. dict list  
    [{A1: B1}, {A2: B2}, {A3: B3}, {A4: B4}] --> k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]
3. dict 
    {A1: B1, A2: B2, A3: B3, A4: B4} -- > k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]


```python
o_data = [('A', '34'), ('B', '45'), ('C', '12')]
x, y = Base.cast(o_data)
print(x) # ['A', 'B', 'C']
print(y) # ['34', '45', '12']
```

The above example can also use the `zip` function directly.


## borax.fetch module

> Project url :  https://github.com/kinegratii/borax

### Install

borax require Python3.5+, you can install this library with the following command :

```shell
$ pip install borax
```

### Function definition document

The module uses the `fetch` function and the signature is shown as follows:

```python
fetch(iterable, key, *keys, default=EMPTY, defaults=None, getter=None)
```

The meaning of each parameter as follows:

- iterable : data list
- key / keys : index of key-value and attributes access methods
- default : default value, for selecting a single attribute
- defaults : default value dictionary, for selecting multiple attributes
- getter : custom access callback function

It should be noted that the *default*, *defaults* and *getter* parameters must be passed by keyword when used. See more info, please refer to [PEP 3102](https://www.python.org/dev/peps/pep-3102/)。

### Example

Select multiple attributes

```python
from borax.fetch import fetch

objects = [
    {'id': 282, 'name': 'Alice', 'age': 30},
    {'id': 217, 'name': 'Bob', 'age': 56},
    {'id': 328, 'name': 'Charlie', 'age': 56},
]

names, ages = fetch(objects, 'name', 'age')
print(names)
print(ages)
```

Output

```
['Alice', 'Bob', 'Charlie']
[30, 56, 56]
```

## networkx library

> Project url： https://github.com/networkx/networkx

For complicated relationship charts, you can use[networkx](https://github.com/networkx/networkx) library to build nodes and link lines, and then pass them to add function. As is shown below :  

```python
# coding=utf8

from __future__ import unicode_literals

import networkx as nx
from networkx.readwrite import json_graph
from pyecharts import Graph

g = nx.Graph()
categories = ['网关', '节点']
g.add_node('FF12C904', name='Gateway 1', symbolSize=40, category=0)
g.add_node('FF12CA02', name='Node 11', category=1)
g.add_node('FF12C326', name='Node 12', category=1)
g.add_node('FF45C023', name='Node 111', category=1)
g.add_node('FF230933', name='Node 1111', category=1)

g.add_edge('FF12C904', 'FF12CA02')
g.add_edge('FF12C904', 'FF12C326')
g.add_edge('FF12CA02', 'FF45C023')
g.add_edge('FF45C023', 'FF230933')

g_data = json_graph.node_link_data(g)
eg = Graph('设备最新拓扑图')
eg.add('Devices', nodes=g_data['nodes'], links=g_data['links'], categories=categories)
# eg.show_config()
eg.render()
```

Result:

![networkx-demo](http://django-echarts.readthedocs.io/zh_CN/latest/_images/networkx-graph-demo.png)