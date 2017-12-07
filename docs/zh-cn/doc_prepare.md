> pyecharts 是一个用于生成 Echarts 图表的类库。实际上就是 Echarts 与 Python 的对接。

[![Build Status](https://travis-ci.org/chenjiandongx/pyecharts.svg?branch=master)](https://travis-ci.org/chenjiandongx/pyecharts) [![codecov](https://codecov.io/gh/chenjiandongx/pyecharts/branch/master/graph/badge.svg)](https://codecov.io/gh/chenjiandongx/pyecharts) [![PyPI version](https://badge.fury.io/py/pyecharts.svg)](https://badge.fury.io/py/pyecharts) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### 确认你已安装了最新版本的 pyecharts
> `pyecharts.__version__` 可查看当前 pyecharts 版本，更多版本信息请查看 [changelog.md](https://github.com/chenjiandongx/pyecharts/blob/master/changelog.md) **强烈推荐阅读**！

**Note：** 推荐使用 pyecharts 的最新版本！！

首先开始来绘制你的第一个图表
```python
from pyecharts import Bar

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar.show_config()
bar.render()
```
![guide-0](https://raw.githubusercontent.com/chenjiandongx/pyecharts/master/images/guide-0.png)


* ```add()```  
    主要方法，用于添加图表的数据和设置各种配置项  
* ```show_config()```  
    打印输出图表的所有配置项
* ```render()```  
    默认将会在根目录下生成一个 render.html 的文件，支持 path 参数，设置文件保存位置，如 render(r"e:\my_first_chart.html")，文件用浏览器打开。  

**Note：** 可以按右边的下载按钮将图片下载到本地，如果想要提供更多实用工具按钮，请在 `add()` 中设置 `is_more_utils` 为 True  

```python
from pyecharts import Bar

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90],
        is_more_utils=True)
bar.render()
```
![guide-1](https://raw.githubusercontent.com/chenjiandongx/pyecharts/master/images/guide-1.png)

### 使用 pyecharts-snapshot 插件
如果想直接将图片保存为 png, pdf, gif 格式的文件，可以使用 [pyecharts-snapshot](https://github.com/chfw/pyecharts-snapshot)。使用该插件请确保你的系统上已经安装了 node.js 环境，如果没有，请到这里下载 [https://nodejs.org/en/download/](https://nodejs.org/en/download/)

1. 安装 phantomjs  
    `npm install -g phantomjs-prebuilt`
2. 安装 pyecharts-snapshot  
    `pip install pyecharts-snapshot`
3. 引入 pyecharts-snapshot  
    `from pyecharts_snapshot.main import make_a_snapshot`
4. 调用方法  
    `make_a_snapshot('render.html', 'snapshot.png')`  
    make_a_snapshot() 第一个参数为生成的 .html 文件，第二个参数为要保存的文件，可以为 png/pdf/gif

更多内容请移步至 [pyecharts-snapshot](https://github.com/chfw/pyecharts-snapshot)  


### Jupyter notebook 小贴士
对本库的现有用户来说，v0.1.9.5 版本的离线模式要求：  
1）老版本已完全卸载   
2）您现有的 notebook 文档需要刷新并重新运行。

离线模式工作原理：pyecharts 自动把 echarts 脚本文件装在了 jupyter nbextensions 文件夹下面。以下代码可以告诉你 pyecharts 网页脚本是否装到了 Jupyter 里面：


```shell
$ jupyter nbextension list
Known nbextensions:
  config dir: /Users/jaska/.jupyter/nbconfig
    notebook section
      echarts/main  enabled 
      - Validating: OK
```

在特殊的情况下，如果你想要 pyecharts 更新所有的脚本文件的话，你可以运行下面的命令：

```shell
$ git clone https://github.com/chfw/jupyter-echarts.git
$ cd jupyter-echarts
$ jupyter nbextension install echarts --user
```
在下一个画图动作的时候，您的脚本文件会被更新。

下面这个删除命令估计只有参与 pyecharts 开发者才会用到

```shell
$ jupyter nbextension uninstall echarts --user
```

#### jupyter-notebook 输出问题
自 v0.1.9.7 起，pyecharts 已经进入全部离线模式，也就是没有网络，也能画图。jupyter notebook 输出后，你的 notebook 离开了本地 jupyter 环境，图片就不能显示了。
为了解决这个问题，再画图之前，你可以多加两个语句：

```python
...
from pyecharts import online

online()
...
```

这样，所有的脚本会从 http://chfw.github.io/jupyter-echarts/echarts 下载。如果你连不上 Github, 你可以先把 https://github.com/chfw/jupyter-echarts 克隆一下。然后在你自己的服务器上，把整个 echarts 挂上去。  

下面我简单示范一下  

```
$ cd jupyter-echarts/echarts
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


### Python2 编码问题
默认的编码类型为 UTF-8，在 Python3 中是没什么问题的，Python3 对中文的支持好很多。但是在 Python2 中，请应用下面的语句，保证没有编码问题:
```
#!/usr/bin/python
#coding=utf-8
from __future__ import unicode_literals
```
前两句告知你的编辑器你用 UTF-8 ([PEP-0263](https://www.python.org/dev/peps/pep-0263/)). 最后一句告知 Python 所有字符是 UTF-8 ([unicode literals](http://python-future.org/unicode_literals.html))


### 图形绘制过程
基本上所有的图表类型都是这样绘制的：
1. ```chart_name = Type()``` 初始化具体类型图表。
2. ```add()``` 添加数据及配置项。
3. ```render()``` 生成 .html 文件。  

```add()``` 数据一般为两个列表（长度一致）。  
如果你的数据是字典或者是带元组的字典。可利用 ```cast()``` 方法转换。

```python
@staticmethod
cast(seq)
``` 转换数据序列，将带字典和元组类型的序列转换为 k_lst,v_lst 两个列表 ``` 
```
1. 元组列表  
    [(A1, B1), (A2, B2), (A3, B3), (A4, B4)] --> k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]
2. 字典列表  
    [{A1: B1}, {A2: B2}, {A3: B3}, {A4: B4}] --> k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]
3. 字典  
    {A1: B1, A2: B2, A3: B3, A4: B4} -- > k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]


### Pandas&Numpy 简单示例
如果使用的是 Numpy 或者 Pandas，可以参考这个示例

![pandas-numpy](https://raw.githubusercontent.com/chenjiandongx/pyecharts/master/images/pandas-numpy.png)

**Note：** 使用 Pandas&Numpy 时，整数类型请确保为 int，而不是 numpy.int32

**当然你也可以采用更加酷炫的方式，使用 Jupyter Notebook 来展示图表，matplotlib 有的，pyecharts 也会有的**  
**Note：** 从 v0.1.9.2 版本开始，废弃 ```render_notebook()``` 方法，现已采用更加 pythonic 的做法。直接调用本身实例就可以了。  

比如这样  

![notebook-0](https://raw.githubusercontent.com/chenjiandongx/pyecharts/master/images/notebook-0.gif)

还有这样

![notebook-1](https://raw.githubusercontent.com/chenjiandongx/pyecharts/master/images/notebook-1.gif)

如果使用的是自定义类，直接调用自定义类示例即可

![notebook-2](https://raw.githubusercontent.com/chenjiandongx/pyecharts/master/images/notebook-2.gif)

更多 Jupyter notebook 的例子请参考 [notebook-use-cases](https://github.com/chenjiandongx/pyecharts/blob/master/docs/notebook-use-cases.zip)。可下载后运行看看。

如需使用 Jupyter Notebook 来展示图表，只需要调用自身实例即可，同时兼容 Python2 和 Python3 的 Jupyter Notebook 环境。所有图表均可正常显示，与浏览器一致的交互体验，这下展示报告连 PPT 都省了！！  
