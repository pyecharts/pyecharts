# [pyecharts](https://github.com/pyecharts/pyecharts) [![Build Status](https://travis-ci.org/pyecharts/pyecharts.svg?branch=master)](https://travis-ci.org/pyecharts/pyecharts) [![Build status](https://ci.appveyor.com/api/projects/status/81cbsfjpfryv1cl8?svg=true)](https://ci.appveyor.com/project/chenjiandongx/pyecharts) [![codecov](https://codecov.io/gh/pyecharts/pyecharts/branch/master/graph/badge.svg)](https://codecov.io/gh/pyecharts/pyecharts) [![PyPI version](https://badge.fury.io/py/pyecharts.svg)](https://badge.fury.io/py/pyecharts) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> pyecharts is a library to generate charts using Echarts. It simply provides the interface of 28+ kinds of charts between Echarts and Python.


## Introduction
[Echarts](https://github.com/ecomfe/echarts) is an open source library from Baidu for data visualization in javascript. It has awesome demo pages so I started to look out for an interface library so that I could use it in Python. I ended up with [echarts-python](https://github.com/yufeiminds/echarts-python) on github but it lacks of documentation and was not updated for a while. Just like many other Python projects, I started my own project, pyecharts, referencing echarts-python and another library [pygal](https://github.com/Kozea/pygal).

## Installation
### Python Compatibility

pyecharts works on Python2.7 and Python3.4+.

pyecharts handles all strings and files with unicode encoding and you **MUST** use unicode string on Python 2.

```python
#coding=utf-8
from __future__ import unicode_literals
```

### pyecharts

You can install it via pip
```
$ pip install pyecharts
```

or clone it and install it
```
$ git clone https://github.com/pyecharts/pyecharts.git
$ cd pyecharts
$ pip install -r requirements.txt
$ python setup.py install
```

Please note: since version 0.3.2, NO LONGER pyecharts comes with any map files. Please read next section for more informations.

### map extensions

Here is a list of map extensions from pyecharts dev team:

1. [World countries include China map and World map](https://echarts-maps.github.io/echarts-countries-js/): [echarts-countries-pypkg](https://github.com/pyecharts/echarts-countries-pypkg) (1.9MB)
2. [Chinese provinces and regions](https://echarts-maps.github.io/echarts-china-provinces-js/): [echarts-china-provinces-pypkg](https://github.com/pyecharts/echarts-china-provinces-pypkg) (730KB)
3. [Chinese cities](https://echarts-maps.github.io/echarts-china-cities-js/): [echarts-china-cities-pypkg](https://github.com/pyecharts/echarts-china-cities-pypkg) (3.8MB)

In order to install them, you can try one of them or all:

```
$ pip install echarts-countries-pypkg
$ pip install echarts-china-provinces-pypkg
$ pip install echarts-china-cities-pypkg
```

## Basic Usage

### Render to Local Html File

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

![usage-0](https://user-images.githubusercontent.com/19553554/35388262-078a4afc-020e-11e8-8acc-cc7bc8a4e8a6.gif)

### Export as Images or Pdf

[pyecharts-snapshot](https://github.com/pyecharts/pyecharts-snapshot) is a library which renders the output of pyecharts as a png, jpeg, gif image or a pdf file at command line or in your code.

See more detail at the repositoty.

## Platform Support

pyecharts exposes chart API and template API so that it can work on some common platforms.

### Work on Jupyter Notebook

In the Notebook cell ,you can simply call the instance itself to diplay the chart.

All chart classes in pyecharts implement the `_repr_html_` interface about [IPython Rich Display](http://ipython.readthedocs.io/en/stable/config/integrating.html#rich-display) .

In the case of online jshost mode,you can also download as some file formats (ipynb/py/html/pdf) and run without jupyter notebook enviromnment.

![pandas_numpy](https://user-images.githubusercontent.com/19553554/35104252-3e36cee2-fca3-11e7-8e43-09bbe8dbbd1e.png)

### Integrate With Web Framework

With the help of pyecharts API,it is easy to integrate pyecharts to your web projects, such as Flask and Django.

Demo

![flask-0](https://user-images.githubusercontent.com/19553554/35081158-3faa7c34-fc4d-11e7-80c9-2de79371374f.gif)

## Advance Topics

### Cusom Template FIles and Layout

pyecharts exposes engine API so that you can use your own template file and integrate with CSS framework.

In addition,pyecharts also ships a lot of jinja2 template functions used in template files.

### Custom Map Library

All map is hosted by the repository [echarts-china-cities-js](https://github.com/pyecharts/echarts-china-cities-js) and [echarts-countries-js](https://github.com/pyecharts/echarts-countries-js) .

## Documentation

* [中文文档](http://pyecharts.org/#/zh-cn/)
* [English Documentation](http://pyecharts.org/#/en-us/)

## Examples

All examples is hosted on the repository [pyecharts-users-cases](https://github.com/pyecharts/pyecharts-users-cases) .

## Test

### Unit Test

You should install the libraries in the requirements.txt files.

```
pip install -r test\requirements.txt
```

And run with the [nose](https://nose.readthedocs.io/en/latest/) commands.

```shell
$ make
```

### Quality Assurance

 [flake8](http://flake8.pycqa.org/en/latest/index.html) and [pylint](https://www.pylint.org/) are used to improve the quality of code.

### Continuous Integration

The project is developed with [Travis CI](https://travis-ci.org/) and [AppVeyor](https://ci.appveyor.com/).

## Author

[![chenjiandongx](https://user-images.githubusercontent.com/19553554/35315207-02ea37ea-0106-11e8-9f9f-8fb26922c492.png)](https://github.com/chenjiandongx)  [![chfw](https://user-images.githubusercontent.com/19553554/35315208-032a38a4-0106-11e8-85f1-7f601330027f.png)](https://github.com/chfw)  [![kinegratii](https://user-images.githubusercontent.com/19553554/35315209-0368f8fa-0106-11e8-99f6-c71d7624a2c9.png)](https://github.com/kinegratii)

## License
pyecharts is released under the MIT License. See LICENSE for more information.
