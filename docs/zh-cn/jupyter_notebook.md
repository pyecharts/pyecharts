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
$ pip install jupyter-echarts-pypkg
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

## 导出 html 功能

可以使用 Notebook 默认的 "download as" 导出其他形式的文件，比如 ipynb 或者图片。

**重要** ：由于导出后的文件脱离了原有 Jupyter Notebook 环境，为了能够完整的显示图表，应当使用远程 jshost 库。

```python
from pyecharts import online

online()
```


如果导出的 HTML 文件需要在没有网路的情况下显示图片，请考虑后面的介绍。

## 导出 PDF 功能

一直以来 PDF 输出的问题困恼着 pyecharts 用户。目前的解决方案是结合 pyecharts-snapshot 来生成静态图片，然后输出。用户需要做两件事情：

第一就是装 [pyecharts-snapshot 0.1.4+ 和 phanomjs-prebuilt](https://github.com/pyecharts/pyecharts-snapshot#installation)

第二就是在 notebook 的最开始添上一下语句。这样就可以输出图片成 PDF 了。

```python
from pyecharts import configure

configure(output_image='png')
```

请看这个例子: [test.pdf](https://github.com/pyecharts/pyecharts/files/1813293/test.6.pdf)

## 导出的 HTML 文件， 在没有互联网，怎么样打开图片

这个时候， 你也需要装 pyecharts-snapshot 0.1.4+ 。你需要用 `renderer` 参数让 pyecharts 0.4.2+ 生成 svg 图片并且加上下面的语句。

```python
from pyecharts import configure

configure(output_image='svg')
```

同时，请注意，这个配置也是可以输出 PDF 的。可就是输出的图片不仅需要 Inkscape，输出图片效果很不好。所以不推荐用 `output_image='svg'`。

## 示例

参见 [pyecharts示例](https://github.com/pyecharts/pyecharts-users-cases) 。

## jupyterlab

[jupyterlab](https://github.com/jupyterlab/jupyterlab) 是下一代 Jupyter Notebook ，目前尚处于发展的雏形之中。我们将进一步关注项目发展，尽可能第一时间实现 pyecharts 的适配，敬请期待。

