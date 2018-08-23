> 开发者篇：本文档介绍了关于 pyecharts 开发的一些情况。

## 准备工作

请用下面命令部署好环境
```bash
$ git clone https://github.com/pyecharts/pyecharts.git
$ pip install -r requirements.txt
$ python setup.py install
```

## 代码格式化 (python 3.6+)

```bash
$ pip install -r requirements-dev.txt
$ ./format_code.sh  # windows: format_code.bat
```

## pyecharts 0.3.2+ 的扩展包

现在 pyecharts 所有的 js 库均由 lml 管理，由 pip 组装。 Jupyter notebook 用户不用担心，javascript 库装机的时候，会被 pyecharts-jupyter-installer 一齐装上。

![map-extension-architecture-diagram](https://github.com/chenjiandongx/pyecharts/blob/master/images/map-extension-architecture.png)

如果有更多需求，比如世界各国地图，请关注本项目。

## pyecharts 0.4.2+ 的 Environment 扩展

pyecharts-snapshot 能把 pyecharts 的 html 输出转换成图片，自然地，把它变成 pyecharts 的 Environment 扩展之后，就可以用同样的语句直接生成图片了。下面是个例子：

```python
#coding=utf-8
from pyecharts import Map

value = [1, 100]
attr = ['Gujarat', 'Tamil Nadu']
map = Map('India', width=800, height=600)
map.add('', attr, value, maptype='印度', is_visualmap=True, visual_text_color="#000")
map.render(path='map.png')  # <--- 直接生成图片
```

下面简单介绍一下架构：

在 pyecharts 里，图标类和 EchartsEnvironment 之间引入了 EnvironmentManager 类。EchartsEnvironment 成了 EnvironmentManager 的下属的同时，EnvironmentManager 通过 lml 可以拥有其他的下属。这个时候，如果用户装了 pyecharts-snapshot 0.1.4，EnvironmentManager 通过 lml 可以得到 SnapshotEnvironment，换句话说 pyecharts 可以得到直接产生图片的功能扩展。

![map-extension-architecture-diagram](https://github.com/chenjiandongx/pyecharts/blob/master/images/environment-extension-architecture.png)

### 局限性

Page 类不能享受直接生成图片的功能。原因是 pyecharts-snapshot 还不能[抓多个图片](https://github.com/pyecharts/pyecharts-snapshot/issues/10)

| 环境         | pyecharts-snapshot 启动方式 |文件格式                       |
| ----------- | ---------------------------|------------------------------|
| jupyter     | output_image               | svg, png, jpeg, html         |
| pure python | 文件后缀                    |svg, png, jpeg, gif, pdf, html|

## pyecharts 0.3.2+ 的扩展包启动顺序

[lml](http://lml.readthedocs.io/en/latest/index.html) 是支持松散包管理的 python 包。它的特点是支持扩展包搭积木式的架构：装了某包，就增加功能；不装，不影响主体库的运转。主体包启动的时候，lml 提供扩展包搜索程序，实现扩展包的动态合体。

![map-extension-architecture-diagram](https://github.com/chenjiandongx/pyecharts/blob/master/images/loading_sequence.png)

需要更多信息，请看[教学实例](http://lml.readthedocs.io/en/latest/api_tutorial.html)。

jupyter-echarts 是一个前端项目，如果你对前端这方面还不太熟悉的话，建议找相关的教程学习一下。

### 向 jupyter-echarts 中新增你的内容

克隆远程仓库

```bash
$ git clone https://github.com/chfw/jupyter-echarts.git
```

然后执行

```bash
$ npm install --save your_javascript_library
```

编辑 gulp.js 文件

```
FILES = [
    './node_modules/echarts/dist/echarts.min.js',
    './node_modules/echarts/map/js/china.js',
    './node_modules/your_library/dist/min_version.js' <---
```

最后运行

```bash
$ gulp
```

最重要的是提交更新内容，你需要将它同步至 jupyter-echarts，如果没有权限的话，那就提交一个 PR 吧。

## 前端编程与 Python

在前端编程领域，没有人会去手动下载和更新 js/css 文件。[npm](https://docs.npmjs.com/getting-started/what-is-npm) 是一个 node.js 的包管理助手，用于帮助前端编程人员去自动化管理 js/css 模块。

当然，还有其他优秀的类似的工具 如 [bower](https://bower.io), [jspm](https://jspm.io) 等等。[gulp](https://gulpjs.com) 是 node.js 中的  `make` 命令，gulpfile.js 是 gulp 的 `Makefile`，你将会使用 js 来编写这些命令。这些优秀的工具可以帮助你自动化管理 js/css 模块，就像 Python 世界的 `pip` 工具。

那现在的前端编程主要在码些什么呢？答案就是 [pug file](https://pugjs.org/api/getting-started.html)/[HAML file](http://haml.info), [sass file](http://sass-lang.com) 和 [coffeescript](http://coffeescript.org)/[typescript](http://www.typescriptlang.org) ，编写这些文件经编译后就会成为 html/css/js 文件了，现在编写网页变成是一个软件工程师干的活了。而面向对象编程，代码复用以及设计 css 属性接口这些事才是前端编程人员的日常工作。

以上是对前端编程的一个简介，node.js 世界有很多很棒的项目，工具以及开发者。期待你去挖掘和发现更多精彩的东西！
