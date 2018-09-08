> Frequently asked questions and its solutions

**Q: After jupyter draws a large number of charts, the chart cannot be displayed and prompts temporarily stop sending output ？**

A: jupyter-notebook console output detailed tips are as follows：

```
IOPub data rate exceeded.
    The notebook server will temporarily stop sending output
    to the client in order to avoid crashing it.
    To change this limit, set the config variable
    `--NotebookApp.iopub_data_rate_limit`.
```

According to the above tips, you need to modify the configuration file (usually jupyter_notebook_config.py) and modify iopub_data_rate_limit to a larger value.

```
## (bytes/sec) Maximum rate at which messages can be sent on iopub before they
#  are limited.
c.NotebookApp.iopub_data_rate_limit = 10000000
```


**Q: In Jupyter Notebook, export files such as ipynb/png/pdf etc using download-as, the chart cannot be displayed?**

A: Since download-as is used, it is out of Jupyter Notebook's environment and cannot refer related js files within it. So you should use online mode, quote from [jupyter-echarts](https://github.com/pyecharts/jupyter- Echarts) or other valid remote js library.

```python
from pyecharts import online

online()
```


**Q: jupyter-notebook export problem**

A: Since 0.1.9.7, pyecharts has gone into offline mode, drawing without internet connection. Now, the charts in exported notebook cannot be display as they have been put outside
jupyter environment.

So the solution is to add the following statement:

```python
...
from pyecharts import online

online()
...
```
Above code will take javascripts from github.
you cannot connect to github, you could clone https://github.com/pyecharts/assets. Then, you put `js` folder onto your own server. Here is a simple command to achieve it:

```
$ git clone https://github.com/pyecharts/assets
$ cd js
$ python -m http.server # for python 2, use python -m SimpleHTTPServer
Serving HTTP on 0.0.0.0 port 8000 ...
```

Then, add localhost into previous python code:

```python
...
from pyecharts import online

online(host="http://localhost:8000)
...
```

**Q: Python2 Coding Problem**

A: Default code type is UTF-8, there's no problem in Python3, because Python3 have a good support in chinese. But in Python2, please use the following sentence to ensure avoiding wrong coding problem:
```
#!/usr/bin/python
#coding=utf-8
from __future__ import unicode_literals
```
The first two sentences are telling your editor that it should use UTF-8 ([PEP-0263](https://www.python.org/dev/peps/pep-0263/)). And the last sentence is telling Python all the characters are UTF-8 ([unicode literals](http://python-future.org/unicode_literals.html))


**Q: Does pyecharts support jupyterlab?**

A: Not supported yet. jupyterlab should be the prototype of next generation jupyter notebook. Welcome to submit the relevant PR.


**Q: How to set the formatter of tooltip option to callback function?**

A: The *option callback function* was introduced in v0.5.0 and can be found in the related documentation.


**Q: Why cannot import charts such as Bar, Line, etc. after installation?**

A: Please check if the test file is named by `pyecharts.py`. If so, please rename the file.


**Q: Cannot load static files like js after packaging in pyinstaller's single file mode?**

A: Currently, pyecharts does not open this part of the API, and does not consider the compatibility problem of the packaged resource file path. It is recommended to use the folder/multi-file mode.
If you really need to use the single file mode, please refer to [Python Packaging Tools](https://kinegratii.github.io/2016/04/23/python-package/). This article gives the relevant principles. After read that, you make some changes on the source code.


**Q: Why are there only pictures of the South China Sea in China?**

![](https://user-images.githubusercontent.com/4280312/37690316-08ef46e0-2ca2-11e8-9f2c-78c41a84bf57.png)

A: 因为 china.js 没有加载成功。请检查 echarts-countries-pypkg 是不是已经装了，安装方法参考 [README](https://github.com/pyecharts/pyecharts/blob/master/README.md)。如果是 jupyter 的环境的话， 请检查能否正确访问 http://localhost:8888/nbextensions/echarts-countries-js/china.js

如果你把地图全部装了的画，在你开新的 notebook 的时候， jupyter 的 javascript console 会有这个显示：

![](https://user-images.githubusercontent.com/4280312/37921785-a472a2b8-3122-11e8-8ee3-cc80a3901d9d.png)


**Q:为什么 jupyter notebook 图是空的？**

请按这个顺序排查问题：

1）检查能否访问 echarts.min.js？ http://localhost:8888/nbextensions/echarts/echarts.min.js

如果不能，请检查 jupyter-echarts-pypkg 是否装好？在确认你已经装了 jupyter 的情况下，可以卸载 jupyter-echarts-pypkg 然后再装一遍（`pip install --no-cache-dir jupyter-echarts-pypkg`）。然后运行 jupyter notebook，再次查看 1）能否正确访问 echarts.min.js？

如果能，请右键打开开发者工具，截下 <script>...</script> 区域的截图.

例子：

![](https://user-images.githubusercontent.com/4280312/29354092-4c4eecee-8264-11e7-98bb-06ec1b4c06b6.png)


**Q: 为什么部分 echarts-xxx-pypkg 不能成功安装？**

首先，请检查当前 python 环境有没有 jupyter。有的话，先卸载先前装的 echarts-xxx-pypkg (`pip uninstall echarts-xxx-pypkg`) ，下一步再用 `pip install --no-cache-dir echarts-xxx-pypkg` 装一遍。


**Q: pip install pyecharts meet error: Microsoft Visual C++ 14.0 is required**

使用 `pip install pyecharts` 安装时出现该问题，“error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools”。

你需要到微软网站下载 Build Tools for Visual Studio 2017。具体信息请访问 https://www.scivision.co/python-windows-visual-c++-14-required/


**Q:如何离线安装 pyecharts？**

自 v0.5.0 后，离线模式的要求改变了一下。如果你用的是 python 3.5+, 以下的指导就足够了。要是你用的是 python 2.7, 3.4, 请读补充提示。

首先需要在一台可以联网的电脑上下载 [requirements.txt](https://github.com/pyecharts/pyecharts/blob/master/requirements.txt) 的依赖包，然后执行
``` shell
$ mkdir pyecharts_requirements
$ cd pyecharts_requirements
$ # 将下载好的 requirement.txt 复制到本目录下
$ pip download -r requirements.txt
$ pip download pyecharts
```
然后就可以看到 pyecharts_requirements 文件夹下已经安装了所有需要的依赖包，包括 pyecharts
``` shell
$ ls
Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        2018/4/19     19:58         824484 future-0.16.0.tar.gz
-a----        2018/4/19     19:58         126381 Jinja2-2.10-py2.py3-none-any.whl
-a----        2018/4/19     19:58         514596 jupyter-echarts-pypkg-0.1.0.tar.gz
-a----        2018/4/19     19:58          10659 lml-0.0.2-py2.py3-none-any.whl
-a----        2018/4/19     19:59          14356 MarkupSafe-1.0.tar.gz
-a----        2018/4/19     19:58        1571935 Pillow-5.1.0-cp36-cp36m-win_amd64.whl
-a----        2018/4/19     20:05         107681 pyecharts-0.4.1.tar.gz
-a----        2018/4/19     19:59           4725 pyecharts_jupyter_installer-0.0.3-py2.py3-none-any.whl
-a----         2018/3/9     23:12             71 requirements.txt
```
复制本文件夹到需要离线安装的电脑上，终端切换到该路径下

``` shell
$ pip install --no-index -f ./ -r requirements.txt
$ pip install ./pyecharts
```

python 2.7, 3.4 用户提示：

离线用法呢，你们有两个选择：

1）拥抱 python 3.5+, 你们就不需要再做别的了  
2）在自己的机器上运行 [pyecharts-javascripthon-api-service](https://github.com/pyecharts/pyecharts-javascripthon-api-service). 这个服务呢，也是需要 python 3.5+ 的，所以如果你是个人用户的，可以就此打住，直接用 pip3 装 pyecharts v0.5.0 好了。