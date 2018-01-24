# pyecharts 文档 - Jupyter Notebook

## 概述

pyecharts 支持在 Jupyter Notebook 环境中显示渲染图表以及导出其他形式的文件。

## 安装

在使用以下的命令安装 pyecharts ，如果系统检查有 Jupyter Notebook 环境，将默认的 echarts.min 等文件自动安装到  Jupyter notebook 插件/扩展；否则将跳过这一步骤。

```shell
pip install pyecharts
```

在之后的开发中也可以使用下列的命令自行安装。

```shell
$ git clone https://github.com/pyecharts/jupyter-echarts.git
$ cd jupyter-echarts
$ jupyter nbextension install echarts --user
```

无论使用何种方式，均可通过以下的命令测试是否安装成功。

```shell
$ jupyter nbextension list
Known nbextensions:
  config dir: /Users/jaska/.jupyter/nbconfig
    notebook section
      echarts/main  enabled 
      - Validating: OK
```



## 显示图表

在 Cell 中，可以直接调用实例本身实例来显示图表，目前所有的类已经实现了  [IPython Rich Display](http://ipython.readthedocs.io/en/stable/config/integrating.html#rich-display) 的 `_repr_html_` 方法。

![pandas-numpy](https://user-images.githubusercontent.com/19553554/35104252-3e36cee2-fca3-11e7-8e43-09bbe8dbbd1e.png)

## 导出功能

可以使用 Notebook 默认的 "download as" 导出其他形式的文件，比如 ipynb或者图片。

**重要** ：由于导出后的文件脱离了原有 Jupyter Notebook 环境，为了能够完整的显示图表，应当使用远程 jshost 库。

```python
from pyecharts import online

online(host='https://my-site.com')
```

## 示例

参见 [pyecharts示例](https://github.com/pyecharts/pyecharts-users-cases) 。

## jupyterlab

[jupyterlab](https://github.com/jupyterlab/jupyterlab) 是下一代 Jupyter Notebook ，目前尚处于发展的雏形之中。我们将进一步关注项目发展，尽可能第一时间实现 pyecharts 的适配，敬请期待。

