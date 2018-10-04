# Jupyter Notebook

> pyecharts support show charts and export to some file formats in the Jupyter Notebook.

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

![pandas_numpy](https://user-images.githubusercontent.com/19553554/35104252-3e36cee2-fca3-11e7-8e43-09bbe8dbbd1e.png)

## Export html function

You can use Notebook's default "download as" to export other forms of files, such as ipynb or images.

**NOTE:** Since the exported file is out of the original Jupyter Notebook environment, in order to be able to display the chart completely, you should use the remote jshost library.

```python
from pyecharts import online

online(host='https://my-site.com') # use remote jshost
```

If the exported HTML file needs to display the image without a network, consider the introduction below.

## Export PDF function

Users can use pyecharts-snapshot to generate static images and then output them. There are two steps that need to be performed.

1. Install [pyecharts-snapshot 0.1.4+ 和 phanomjs-prebuilt](https://github.com/pyecharts/pyecharts-snapshot#installation)
2. Add a statement at the beginning of the notebook. This will output the image as a PDF.

```python
from pyecharts import Bar, configure

configure(output_image='pdf')

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar # Display as a pdf file in jupyter and not as a local pdf file.
```

Please see this example: [test.pdf](https://github.com/pyecharts/pyecharts/files/1813293/test.6.pdf)

## Show charts in HTML offline

Users need to install pyecharts-snapshot 0.1.4+ and use the `renderer` parameter to generate svg images by pyecharts 0.4.2+.

```python
from pyecharts import configure

configure(output_image='svg')
```

**NOTE:** `svg` is also possible to output a PDF. But the output image not only requires Inkscape but the image is not very good. Therefore, it is not recommended to use `output_image='svg'` to output as PDF.

## Example

Refer to [pyecharts示例](https://github.com/pyecharts/pyecharts-users-cases).

## Theme

Since pyecharts 0.5.2+, users configure the theme of a single chart through the `use_theme` function. If you want to configure the theme of all the charts in your environment, you can add the following statement at the very beginning of the notebook:

```python
from pyecharts import configure

configure(global_theme='dark')
```

Then re-run, you can see that the theme has been replaced.

## nteract

From pyecharts 0.5.5+, [nteract](https://nteract.io) can also use pyecharts. For now, nteract users must declare `enable_nteract()` at the very beginning. Otherwise, just call `enable_nteract()` when you need to generate html(js) output.

![nteract-demo](https://user-images.githubusercontent.com/4280312/40146181-75652024-595c-11e8-9a63-44fcfb8959c2.png)

However, if you need to output an image, the method is the same as the jupyter notebook mentioned above.

![nteract-image-output](https://user-images.githubusercontent.com/4280312/40167928-305385bc-59ba-11e8-9a23-56b5970f1a41.png)

## jupyterlab

[jupyterlab](https://github.com/jupyterlab/jupyterlab) is the next generation for Jupyter Notebook,and this is a very early preview, and is not suitable for general usage yet. We will pay Continuous attention to the development and make adapter with pyecharts.

