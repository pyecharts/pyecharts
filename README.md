# pyecharts

pyecharts is a library to generate charts using Echarts. It simply provides the interface between Echarts and Python.

[![Build Status](https://travis-ci.org/chenjiandongx/pyecharts.svg?branch=master)](https://travis-ci.org/chenjiandongx/pyecharts) [![codecov](https://codecov.io/gh/chenjiandongx/pyecharts/branch/master/graph/badge.svg)](https://codecov.io/gh/chenjiandongx/pyecharts) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Introduction
[Echarts](https://github.com/ecomfe/echarts) is an open source library from Baidu for data visualization in javascript. It has awesome demo pages so I started to look out for an interface library so that I could use it in Python. I ended up with [echarts-python](https://github.com/yufeiminds/echarts-python) on github but it lacks of documentation and was not updated for a while. Just like many other Python projects, I started my own project, pyecharts, referencing echarts-python and another library [pygal](https://github.com/Kozea/pygal).

## Installation
pyecharts works on Python2 and Python3. The latest release is 0.2.1. For more information please refer to [changelog.md](https://github.com/chenjiandongx/pyecharts/blob/master/changelog.md)

You can install it via pip
```
$ pip install pyecharts
```

or clone it and install it
```
$ git clone --recursive https://github.com/chenjiandongx/pyecharts.git
$ cd pyecharts
$ python setup.py install
```

## Basic Usage
```python
from pyecharts import Bar

attr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
bar = Bar("Bar chart", "precipitation and evaporation one year")
bar.add("precipitation", attr, v1, mark_line=["average"], mark_point=["max", "min"])
bar.add("evaporation", attr, v2, mark_line=["average"], mark_point=["max", "min"])
bar.render()
```

It will create a file named render.html in the root directory, open file with your borwser.  

![usage-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/usage-0.gif)


## Working with pandas & numpy

![pandas_numpy](https://github.com/chenjiandongx/pyecharts/blob/master/images/pandas-numpy.png)


## working with Flask & Django
Flask

![flask-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/flask-0.gif)

Django

![django-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/django-0.gif)

* 中文文档
    * [pyecharts + Flask](https://github.com/chenjiandongx/pyecharts/blob/master/docs/zh-cn/doc_flask.md)
    * [pyecharts + Django](https://github.com/chenjiandongx/pyecharts/blob/master/docs/zh-cn/doc_django.md)
* English
    * [pyecharts + Flask](https://github.com/chenjiandongx/pyecharts/blob/master/docs/en-us/doc_flask.md)
    * [pyecharts + Django](https://github.com/chenjiandongx/pyecharts/blob/master/docs/en-us/doc_django.md)


## Documentation
* [中文文档](https://github.com/chenjiandongx/pyecharts/blob/master/docs/zh-cn/documentation.md)
* [English](https://github.com/chenjiandongx/pyecharts/blob/master/docs/en-us/documentation.md)

## Author
pyecharts is developed and maintained by chenjiandongx ([chenjiandongx@qq.com](chenjiandongx@qq.com))

## License
pyecharts is released under the MIT License. See LICENSE for more information.

