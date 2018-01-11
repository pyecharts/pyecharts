# [pyecharts](https://github.com/pyecharts/pyecharts) [![Build Status](https://travis-ci.org/pyecharts/pyecharts.svg?branch=master)](https://travis-ci.org/chenjiandongx/pyecharts) [![codecov](https://codecov.io/gh/chenjiandongx/pyecharts/branch/master/graph/badge.svg)](https://codecov.io/gh/chenjiandongx/pyecharts) [![PyPI version](https://badge.fury.io/py/pyecharts.svg)](https://badge.fury.io/py/pyecharts) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> pyecharts is a library to generate charts using Echarts. It simply provides the interface between Echarts and Python.


## Introduction
[Echarts](https://github.com/ecomfe/echarts) is an open source library from Baidu for data visualization in javascript. It has awesome demo pages so I started to look out for an interface library so that I could use it in Python. I ended up with [echarts-python](https://github.com/yufeiminds/echarts-python) on github but it lacks of documentation and was not updated for a while. Just like many other Python projects, I started my own project, pyecharts, referencing echarts-python and another library [pygal](https://github.com/Kozea/pygal).

## Installation
pyecharts works on Python2 and Python3. For more information please refer to [changelog.md](https://github.com/chenjiandongx/pyecharts/blob/master/changelog.md)

### Jupyter-Notebook
Make sure you hava installed jupyter-notebook enviroment if you want to show your charts on notebook.   
How to install it?
```
$ pip install notebook
```
### pyecharts
You can install it via pip
```
$ pip install pyecharts -U
```

or clone it and install it
```
$ git clone --recursive https://github.com/pyecharts/pyecharts.git
$ cd pyecharts
$ pip install -r requirements.txt
$ python setup.py install
```

## Basic Usage

### Render To Local Html File

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

It will create a file named *render.html* in the root directory, open file with your borwser.  

![usage-0](https://github.com/pyecharts/pyecharts/blob/master/images/usage-0.gif)

### Export as Images or Pdf

[pyecharts-snapshot](https://github.com/pyecharts/pyecharts-snapshot) is a library which renders the output of pyecharts as a png, jpeg, gif image or a pdf file at command line or in your code.

See more detail at the repositoty.

## Platform Support

pyecharts exposes chart API and template API so that it can work on some common platforms.

### Work on Jupyter Notebook

In the Notebook cell ,you can simply call the instance itself to diplay the chart.

All chart classes in pyecharts implement the `_repr_html_` interface about [IPython Rich Display](http://ipython.readthedocs.io/en/stable/config/integrating.html#rich-display) .

### Integrate With Web Framework

With the help of pyecharts API,it is easy to integrate pyecharts to your web projects, such as Flask and Django.

Flask

![flask-0](https://github.com/pyecharts/pyecharts/blob/master/images/flask-0.gif)

Django

![django-0](https://github.com/pyecharts/pyecharts/blob/master/images/django-0.gif)

## Advance Topics

### Working with pandas & numpy

![pandas_numpy](https://github.com/pyecharts/pyecharts/blob/master/images/pandas-numpy.png)

### Cusom Template FIles and Layout

The `render` function support the *template_file* parameter so that you can custom your template file and integrate with CSS framework.

In addition,pyecharts also ships a lot of jinja2 template functions used in template files.

### Custom User Map

All map is hosted by the repository [echarts-china-cities-js](https://github.com/pyecharts/echarts-china-cities-js) and [echarts-countries-js](https://github.com/pyecharts/echarts-countries-js)

## Documentation

* [中文文档](https://github.com/chenjiandongx/pyecharts/tree/master/docs/zh-cn)
* [English Documentation](https://github.com/chenjiandongx/pyecharts/tree/master/docs/en-us)

## Examples

All examples is hosted on the repository [pyecharts-users-cases](https://github.com/pyecharts/pyecharts-users-cases)

## Test

You should install the libraries in the requirements.txt files.

```
pip install -r test\requirements.txt
```

And run with the following commands.

```shell
$ cd test
$ nosetests --with-coverage --cover-package pyecharts --cover-package test
```

## Author
pyecharts is developed and maintained by chenjiandongx ([chenjiandongx@qq.com](chenjiandongx@qq.com))

## License
pyecharts is released under the MIT License. See LICENSE for more information.
