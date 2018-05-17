# Jupyter Notebook

> pyecharts 支持在 Jupyter Notebook 环境中显示渲染图表以及导出其他形式的文件。

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

在 Cell 中，可以直接调用实例本身来显示图表，目前所有的类已经实现了 [IPython Rich Display](http://ipython.readthedocs.io/en/stable/config/integrating.html#rich-display) 的 `_repr_html_` 方法。

![pandas-numpy](https://user-images.githubusercontent.com/19553554/35104252-3e36cee2-fca3-11e7-8e43-09bbe8dbbd1e.png)

## 导出 html 功能

可以使用 Notebook 默认的 "download as" 导出其他形式的文件，比如 ipynb 或者图片。

**NOTE:** 由于导出后的文件脱离了原有 Jupyter Notebook 环境，为了能够完整的显示图表，应当使用远程 jshost 库。

```python
from pyecharts import online

online() # 使用远程 jshost
```

如果导出的 HTML 文件需要在没有网路的情况下显示图片，请考虑后面的介绍。

## 导出 PDF 功能

用户可以结合 pyecharts-snapshot 来生成静态图片，然后输出。需要执行一下两个步骤。

1. 安装 [pyecharts-snapshot 0.1.4+ 和 phanomjs-prebuilt](https://github.com/pyecharts/pyecharts-snapshot#installation)
2. 在 notebook 的最开始添上一下语句。这样就可以输出图片成 PDF 了。

```python
from pyecharts import Bar, configure

configure(output_image='pdf')

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar # 将在 jupyter 中显示为 pdf 文件，并不保存为本地 pdf 文件。
```

请看这个例子: [test.pdf](https://github.com/pyecharts/pyecharts/files/1813293/test.6.pdf)

## 离线显示 HTML 中的图片

用户需要装 pyecharts-snapshot 0.1.4+，并使用 `renderer` 参数让 pyecharts 0.4.2+ 生成 svg 图片。

```python
from pyecharts import configure

configure(output_image='svg')
```

**NOTE:** `svg` 下也是可以输出 PDF 的。可就是输出的图片不仅需要 Inkscape 且图片效果很不好。所以不推荐用 `output_image='svg'` 输出为 PDF。

## 示例

参见 [pyecharts示例](https://github.com/pyecharts/pyecharts-users-cases) 。

## 主题

自 pyecharts 0.5.2+ 之后，用户通过图表的 `use_theme` 函数配置单个图形的主题。如果想配置运行环境内所有图表的主题，可以在 notebook 的最开始添上以下语句：

```python
from pyecharts import configure

configure(global_theme='dark')
```

然后在重新运行，就可以看到主题已经被更换。

## nteract

从 pyecharts 0.5.5+ 开始，[nteract](https://nteract.io) 也可以使用 pyecharts 了。目前来说，nteract 用户必需在最开始的时候声明 `enable_nteract()` 才能顺利进行绘图。而且，仅仅是在需要产生 html(js) 输出是需要调用 `enable_nteract()`。

![nteract-demo](https://user-images.githubusercontent.com/4280312/40146181-75652024-595c-11e8-9a63-44fcfb8959c2.png)

但是，如果你需要输出图片，具体做法和上面提到的 jupyter notebook 的做法是一样的。

![nteract-image-output](https://user-images.githubusercontent.com/4280312/40167928-305385bc-59ba-11e8-9a23-56b5970f1a41.png)

## jupyterlab

[jupyterlab](https://github.com/jupyterlab/jupyterlab) 是下一代 Jupyter Notebook ，目前尚处于发展的雏形之中。我们将进一步关注项目发展，尽可能第一时间实现 pyecharts 的适配，敬请期待。
