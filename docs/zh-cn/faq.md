> FAQ 篇：本文档主要介绍一些常见问题及解决方案

**Q:jupyter 绘画大量图后，图表无法显示，并提示 temporarily stop sending output ？**

A:jupyter-notebook console output 具体提示信息如下：

```
IOPub data rate exceeded.
    The notebook server will temporarily stop sending output
    to the client in order to avoid crashing it.
    To change this limit, set the config variable
    `--NotebookApp.iopub_data_rate_limit`.
```

根据以上的提示，需要修改找到配置文件（通常为 jupyter_notebook_config.py），并修改 iopub_data_rate_limit 为更大的数值。

```
## (bytes/sec) Maximum rate at which messages can be sent on iopub before they
#  are limited.
c.NotebookApp.iopub_data_rate_limit = 10000000
```

**Q:在 Jupyter Notebook 使用 download-as 导出 ipynb/png/pdf 等文件后，图表无法显示？**

A:由于使用 download-as 后，便脱离了 Jupyter Notebook 的环境，无法引用其内的相关 js 文件，因此应当使用在线模式，引用来自 [jupyter-echarts](https://github.com/pyecharts/jupyter-echarts) 或其他有效的远程 js 库。

```python
from pyecharts import online

online()
```

**Q:jupyter-notebook 输出问题**

jupyter notebook 输出后，你的 notebook 离开了本地 jupyter 环境，图片就不能显示了。
为了解决这个问题，再画图之前，你可以多加两个语句：

```python
...
from pyecharts import online

online()
...
```

这样，所有的脚本会从 github 下载。如果你连不上 Github, 你可以先把 https://github.com/pyecharts/assets 克隆一下。然后在你自己的服务器上，把整个 js 文件夹挂上去。

下面我简单示范一下  

```
$ git clone https://github.com/pyecharts/assets
$ cd js
$ python -m http.server # for python 2, use python -m SimpleHTTPServer
Serving HTTP on 0.0.0.0 port 8000 ...
```

然后，再把本地服务器加进前面的语句：

```python
...
from pyecharts import online

online(host="http://localhost:8000)
...
```
**Q:Python2 编码问题**
默认的编码类型为 UTF-8，在 Python3 中是没什么问题的，Python3 对中文的支持好很多。但是在 Python2 中，请应用下面的语句，保证没有编码问题:
```
#!/usr/bin/python
#coding=utf-8
from __future__ import unicode_literals
```
前两句告知你的编辑器你用 UTF-8 ([PEP-0263](https://www.python.org/dev/peps/pep-0263/)). 最后一句告知 Python 所有字符是 UTF-8 ([unicode literals](http://python-future.org/unicode_literals.html))

**Q:pyecharts 是否支持  jupyterlab?**

A: 暂不支持。 jupyterlab 应该是下一代 jupyter notebook 的雏形。欢迎大家提交相关 PR。

**Q:怎么设置 echarts 主题？**

A: 主题功能暂时不支持。

**Q:如何设置 tooltip 的 formatter 选项为回调函数？**

A: 目前暂时无法支持。因为暂无法将 python 函数通过 json 转换对应的 js 函数。

**Q:为什么安装后还是无法 import Bar,Line 等图形**

A:请检查是否将测试文件命名为 pyecharts.py，如若是请重命名该文件。

**Q:使用 pyinstaller 的单文件模式打包后无法加载 js 等静态文件？**

A:目前 pyecharts 暂时未开放这部分的API，没有考虑到打包后的资源文件路径的兼容问题。建议使用文件夹/多文件模式。
如果确实需要使用单文件模式，可参考 [《Python打包工具》](https://kinegratii.github.io/2016/04/23/python-package/) 这篇文章了解相关原理后进行源码修改。