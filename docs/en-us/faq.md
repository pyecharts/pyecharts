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

A: Because china.js did not load successfully. Please check if echarts-countries-pypkg is installed. Install solutions [README](https://github.com/pyecharts/pyecharts/blob/master/README.md). If in jupyter environment, please check if it can be accessed correctly. http://localhost:8888/nbextensions/echarts-countries-js/china.js

If you have already installed all maps, jupyter's javascript console will have this content when you open a new notebook:

![](https://user-images.githubusercontent.com/4280312/37921785-a472a2b8-3122-11e8-8ee3-cc80a3901d9d.png)


**Q: Why is the jupyter notebook chart empty?**

Please check it in this order：

1）Check if you can access echarts.min.js? http://localhost:8888/nbextensions/echarts/echarts.min.js

If not, please check if jupyter-echarts-pypkg is installed? After confirming that jupyter is installed, you can uninstall jupyter-echarts-pypkg and install it again. (`pip install --no-cache-dir jupyter-echarts-pypkg`).   
And then run jupyter notebook, check `1）if you can access echarts.min.js`?

If so, right click on the developer tool and take a screenshot of the <script>...</script> area.

Example:  

![](https://user-images.githubusercontent.com/4280312/29354092-4c4eecee-8264-11e7-98bb-06ec1b4c06b6.png)


**Q: Why are some echarts-xxx-pypkg not successfully installed?**

First, check if there is a jupyter in the current python environment. If you have it, first uninstall the previously installed echarts-xxx-pypkg (`pip uninstall echarts-xxx-pypkg`) and install it again with `pip install --no-cache-dir echarts-xxx-pypkg`.


**Q: pip install pyecharts meet error: Microsoft Visual C++ 14.0 is required**

"error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools ". This problem occurs when installing with `pip install pyecharts`.  

You need to go to the Microsoft website to download Build Tools for Visual Studio 2017. For more information, please visit https://www.scivision.co/python-windows-visual-c++-14-required/


**Q: How to install pyecharts offline?**

The requirements for offline mode have changed since v0.5.0. If you are using python 3.5+, the following instructions will be enough. If you are using python 2.7 / 3.4, please read the supplementary tips.

First, you need to download [requirements.txt](https://github.com/pyecharts/pyecharts/blob/master/requirements.txt) packages on a computer that can be connected to the Internet.
``` shell
$ mkdir pyecharts_requirements
$ cd pyecharts_requirements
$ # copy requirement.txt to this directory
$ pip download -r requirements.txt
$ pip download pyecharts
```
Then you can see all required dependencies have been installed under the pyecharts_requirements folder, including pyecharts.
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
Copy this folder to the computer that needs to be installed offline, and then switches to the path in terminal.

``` shell
$ pip install --no-index -f ./ -r requirements.txt
$ pip install ./pyecharts
```

python 2.7, 3.4 user tips：

For offline usage, you have two options:

1）Switch to python 3.5+  
2）Run [pyecharts-javascripthon-api-service](https://github.com/pyecharts/pyecharts-javascripthon-api-service) on your machine. This service also needs python 3.5+, so if you are a personal user, you can stop here and install pyecharts v0.5.0 directly with pip3.