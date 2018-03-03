# pyecharts Document - Jupyter Notebook

## Overview

You can show charts and export to some file formats in the Jupyter Notebook.

## Installation

When install the *pyecharts* package using the following command, a jupyter nbextension named *echarts/main* will be installed if jupyter exists.Or the nbextension installation will be skipped.

```shell
pip install pyecharts
```

In the development, you can also use the command to install manually jupyter nbextension.

```shell
$ pip install jupyter-echarts-pypkg
```

You can check the jupyter nbextension using the *list* command.

```shell
$ jupyter nbextension list
Known nbextensions:
  config dir: /Users/jaska/.jupyter/nbconfig
    notebook section
      echarts/main  enabled 
      - Validating: OK
```



## Show Charts

In the Notebook cell ,you can simply call the instance itself to diplay the chart.

All chart classes in pyecharts implement the `_repr_html_` interface about [IPython Rich Display](http://ipython.readthedocs.io/en/stable/config/integrating.html#rich-display) .

![pandas_numpy](https://github.com/pyecharts/pyecharts/blob/master/images/pandas-numpy.png)

## Export Images and Pdf

You can also download as some file formats (ipynb/py/html/pdf) and run without jupyter notebook enviromnment.

**Important** ：You must be use remote jshost mode to enable this feature.

```python
from pyecharts import online

online(host='https://my-site.com')
```

## Demo

see more detail for [pyecharts-users-cases](https://github.com/pyecharts/pyecharts-users-cases) 。

## jupyterlab

[jupyterlab](https://github.com/jupyterlab/jupyterlab) is the next generation for Jupyter Notebook,and this is a very early preview, and is not suitable for general usage yet. We will pay Continuous attention to the development and make adapter with pyecharts.

