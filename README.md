<p align="center">
    <img src="https://user-images.githubusercontent.com/19553554/39612358-499eb2ae-4f91-11e8-8f56-179c4f0bf2df.png" alt="pyecharts logo" width=200 height=200 />
</p>
<h1 align="center">pyecharts</h1>
<p align="center">
    <em>pyecharts is a library to generate charts using Echarts. It simply provides the interface of 28+ kinds of charts between Echarts and Python.</em>
</p>
<p align="center">
    <a href="https://travis-ci.org/pyecharts/pyecharts">
        <img src="https://travis-ci.org/pyecharts/pyecharts.svg?branch=master" alt="Travis Build Status">
    </a>
    <a href="https://ci.appveyor.com/project/chenjiandongx/pyecharts">
        <img src="https://ci.appveyor.com/api/projects/status/81cbsfjpfryv1cl8?svg=true" alt="Appveyor Build Status">
    </a>
    <a href="https://codecov.io/gh/pyecharts/pyecharts">
        <img src="https://codecov.io/gh/pyecharts/pyecharts/branch/master/graph/badge.svg" alt="Codecov">
    </a>
    <a href="https://badge.fury.io/py/pyecharts">
        <img src="https://badge.fury.io/py/pyecharts.svg" alt="Package version">
    </a>
    <a href="https://pypi.org/project/pyecharts/">
        <img src="https://img.shields.io/pypi/pyversions/pyecharts.svg?colorB=brightgreen" alt="PyPI - Python Version">
    </a>
</p>
<p align="center">
    <a href="https://pypi.org/project/pyecharts">
        <img src="https://img.shields.io/pypi/format/pyecharts.svg" alt="PyPI - Format">
    </a>
     <a href="https://github.com/pyecharts/pyecharts/pulls">
        <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions welcome">
    </a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" alt="License">
    </a>
</p>

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
```shell
$ pip install pyecharts
```

or clone it and install it
```shell
$ git clone https://github.com/pyecharts/pyecharts.git
$ cd pyecharts
$ pip install -r requirements.txt
$ python setup.py install
```

Please note: since version 0.3.2, **NO LONGER** pyecharts comes with any map files. Please read next section for more informations.

### Geo Data extensions (0.5.7+)

From geonames.org, [138,398](https://github.com/echarts-maps/echarts-cities-js) cities of the world with a population of at least 1000 inhabitants: [echarts-cities-pypkg](https://github.com/pyecharts/echarts-cities-pypkg)

Install data extensions:

```shell
$ pip install echarts-cities-pypkg
```

### Map extensions

Here is a list of map extensions from pyecharts dev team:

1. [World countries include China map and World map](https://echarts-maps.github.io/echarts-countries-js/): [echarts-countries-pypkg](https://github.com/pyecharts/echarts-countries-pypkg) (1.9MB)
2. [Chinese provinces and regions](https://echarts-maps.github.io/echarts-china-provinces-js/): [echarts-china-provinces-pypkg](https://github.com/pyecharts/echarts-china-provinces-pypkg) (730KB)
3. [Chinese cities](https://echarts-maps.github.io/echarts-china-cities-js/): [echarts-china-cities-pypkg](https://github.com/pyecharts/echarts-china-cities-pypkg) (3.8MB)
4. [Chinese counties](https://echarts-maps.github.io/echarts-china-counties-js/): [echarts-china-counties-pypkg](https://github.com/pyecharts/echarts-china-counties-pypkg) (4.1MB)
5. [Custom Chinese regions](https://echarts-maps.github.io/echarts-china-misc-js/): [echarts-china-misc-pypkg](https://github.com/pyecharts/echarts-china-misc-pypkg) (148KB)
6. [United Kingdom map](https://echarts-maps.github.io/echarts-united-kingdom-js/): [echarts-united-kingdom-pypkg](https://github.com/pyecharts/echarts-united-kingdom-pypkg) (1MB)


In order to install them, you can try one or all of them below:

```shell
$ pip install echarts-countries-pypkg
$ pip install echarts-china-provinces-pypkg
$ pip install echarts-china-cities-pypkg
$ pip install echarts-china-counties-pypkg
$ pip install echarts-china-misc-pypkg
$ pip install echarts-united-kingdom-pypkg
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

![](https://user-images.githubusercontent.com/19553554/35388262-078a4afc-020e-11e8-8acc-cc7bc8a4e8a6.gif)

### Export as Images or Pdf

[pyecharts-snapshot](https://github.com/pyecharts/pyecharts-snapshot) is [a command line utility](https://github.com/pyecharts/pyecharts-snapshot#usage) and [a library extension](https://github.com/pyecharts/pyecharts-snapshot#example-programs) which renders the output of pyecharts as a svg, png, jpeg, gif image or a pdf file.

After you will have installed pyecharts-snapshot, you can modify previous example file slightly and get png output directly:


```python
bar.render(path="render.png")
```

So please see installation instruction and other usage at that repository.

## Platform Support

pyecharts exposes chart API and template API so that it can work on other python frameworks.

### Integration with Jupyter Notebook/nteract

#### Notebook

In the Notebook cell, you can simply pass on chart instance itself to Jupyter, which will diplay the chart. Please note **render_notebook** function has been removed.

All chart classes in pyecharts implement the `_repr_html_` interface about [IPython Rich Display](http://ipython.readthedocs.io/en/stable/config/integrating.html#rich-display) .

In the case of online jshost mode, you can also download as some file formats (ipynb/py/html/pdf) and run without jupyter notebook enviromnment.

![](https://user-images.githubusercontent.com/19553554/35104252-3e36cee2-fca3-11e7-8e43-09bbe8dbbd1e.png)

#### nteract

Since pyecharts 0.5.5+, [nteract](https://nteract.io) is supported. Once the following two lines should added to your notebook, you could use pyecharts in nteract in the same way as in jupyter notebook.

```python
from pyecharts import enable_nteract

enable_nteract()
```

![](https://user-images.githubusercontent.com/19553554/40266807-2c3ddcc2-5b84-11e8-8240-d3398243d4a6.png)

However, when rendering output as image, the instructions are the same as jupyter notebook. Only default html(including js) output should call `enable_nteract()`.

### Integrate With Web Framework

With the help of pyecharts API, it is easy to integrate pyecharts to your web projects, such as Flask and Django.

Demo

![](https://user-images.githubusercontent.com/19553554/35081158-3faa7c34-fc4d-11e7-80c9-2de79371374f.gif)

## Advanced Topics

### Custom Template Files and Layout

pyecharts exposes engine API so that you can use your own template file and custom CSS.

In addition, pyecharts also ships a lot of jinja2 template functions used in template files.

### Custom Map Libraries

All maps are developed and maintained by [echarts-maps](https://github.com/echarts-maps) github organisation.

## Documentation

* [中文文档](http://pyecharts.org/#/zh-cn/)
* [English Documentation](http://pyecharts.org/#/en-us/)

## Examples

All examples is hosted on the repository [pyecharts-users-cases](https://github.com/pyecharts/pyecharts-users-cases).

## Test

### Unit Test

You should install the libraries in the requirements.txt files.

```shell
$ pip install -r test\requirements.txt
```

And run with the [nose](https://nose.readthedocs.io/en/latest/) commands.

```shell
$ make
```

### Quality Assurance

[flake8](http://flake8.pycqa.org/en/latest/index.html), [Codecov](https://codecov.io/) and [pylint](https://www.pylint.org/) are used to improve the quality of code.

### Continuous Integration

The project is developed with [Travis CI](https://travis-ci.org/) and [AppVeyor](https://ci.appveyor.com/).

## Author

[![](https://sourcerer.io/fame/chenjiandongx/pyecharts/pyecharts/images/0)](https://sourcerer.io/fame/chenjiandongx/pyecharts/pyecharts/links/0)[![](https://sourcerer.io/fame/chenjiandongx/pyecharts/pyecharts/images/1)](https://sourcerer.io/fame/chenjiandongx/pyecharts/pyecharts/links/1)[![](https://sourcerer.io/fame/chenjiandongx/pyecharts/pyecharts/images/2)](https://sourcerer.io/fame/chenjiandongx/pyecharts/pyecharts/links/2)[![](https://sourcerer.io/fame/chenjiandongx/pyecharts/pyecharts/images/3)](https://sourcerer.io/fame/chenjiandongx/pyecharts/pyecharts/links/3)[![](https://sourcerer.io/fame/chenjiandongx/pyecharts/pyecharts/images/4)](https://sourcerer.io/fame/chenjiandongx/pyecharts/pyecharts/links/4)[![](https://sourcerer.io/fame/chenjiandongx/pyecharts/pyecharts/images/5)](https://sourcerer.io/fame/chenjiandongx/pyecharts/pyecharts/links/5)[![](https://sourcerer.io/fame/chenjiandongx/pyecharts/pyecharts/images/6)](https://sourcerer.io/fame/chenjiandongx/pyecharts/pyecharts/links/6)[![](https://sourcerer.io/fame/chenjiandongx/pyecharts/pyecharts/images/7)](https://sourcerer.io/fame/chenjiandongx/pyecharts/pyecharts/links/7)

## License
pyecharts is released under the MIT License. See LICENSE for more information.
