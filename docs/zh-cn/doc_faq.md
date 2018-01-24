> FAQ 篇：本文档主要介绍一些常见问题及解决方案

**Q:jupyter绘画大量图后，图表无法显示，并提示 temporarily stop sending output ？**

A:jupyter-notebook console output 具体提示信息如下：

```
IOPub data rate exceeded.
    The notebook server will temporarily stop sending output
    to the client in order to avoid crashing it.
    To change this limit, set the config variable
    `--NotebookApp.iopub_data_rate_limit`.
```

根据以上的提示，需要修改找到配置文件（通常为jupyter_notebook_config.py），并修改 iopub_data_rate_limit 为更大的数值。

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

**Q:克隆项目到本地后 template/js 文件夹为空，没有 js 文件？**

A: pyecharts 项目使用了 submodule 特性，template/js 引用了另一个仓库的代码。

这时应当使用下面的命令更新 submodule 模块内容。

```
git submodule update
```

或者删除原有代码后，使用 `git clone --recursive https://github.com/pyecharts/pyecharts.git` 重新克隆代码。

**Q:pyecharts 是否支持  jupyterlab?**

A: 暂不支持。 jupyterlab应该是下一代 jupyter notebook 的雏形。欢迎大家提交相关 PR。

**Q:怎么设置 echarts 主题？**

A: 主题功能暂时不支持。

**Q:如何设置 tooltip 的 formatter 选项为回调函数？**

A: 目前暂时无法支持。因为暂无法将 python 函数通过 json 转换对应的 js 函数。

**Q:为什么安装后还是无法 import Bar,Line 等图形**

A:请检查是否将测试文件命名为 pyecharts.py，如若是请重命名该文件。

**Q:使用pyinstaller的单文件模式打包后无法加载js等静态文件？**

A:目前 pyecharts 暂时未开放这部分的API，没有考虑到打包后的资源文件路径的兼容问题。建议使用文件夹/多文件模式。

如果确实需要使用单文件模式，可参考 [《Python打包工具》](https://kinegratii.github.io/2016/04/23/python-package/) 这篇文章了解相关原理后进行源码修改。