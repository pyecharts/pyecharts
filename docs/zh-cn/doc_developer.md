## 如何在 pyecharts 中安装更多的 Javascript 库

现在 pyecharts 所有的 js 库均已托管在 [submodule](https://git-scm.com/docs/git-submodule) [jupyter-echarts](https://github.com/chfw/jupyter-echarts). 也就是说现在所有 js 库的更新都要经过 jupyter-echarts。  

jupyter-echarts 是一个前端项目，如果你对前端这方面还不太熟悉的话，建议找相关的教程学习一下。

## step 1：向 jupyter-echarts 中新增你的内容

克隆远程仓库

```
git clone https://github.com/chfw/jupyter-echarts.git
```

然后执行

```
npm install --save your_javascript_library
```

编辑 gulp.js 文件

```
...
FILES = [
    './node_modules/echarts/dist/echarts.min.js',
    './node_modules/echarts/map/js/china.js',
    './node_modules/your_library/dist/min_version.js' <---
```

最后运行

```
$ gulp
```

最重要的是提交更新内容，你需要将它同步至 jupyter-echarts，如果没有权限的话，那就提交一个 PR 吧。


## step 2：更新 pyecharts

一旦你的提交被 jupyter-echarts 所接受，你就可以更新 pyecharts 了。
```
$ git clone --recursive https://github.com/chenjiandongx/pyecharts.git
$ cd pyecharts/pyecharts/templates/js
$ git pull
remote: Counting objects: 7, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 7 (delta 4), reused 7 (delta 4), pack-reused 0
Unpacking objects: 100% (7/7), done.
From https://github.com/chfw/jupyter-echarts
   af7184b..bb87949  master     -> origin/master
Updating af7184b..bb87949
Fast-forward
 echarts/main.js | 2 +-
 gulpfile.js     | 2 +-
 src/main.ts     | 2 +-
 3 files changed, 3 insertions(+), 3 deletions(-)
$ cd ../../../
$ git commit -am "pull latest changes from jupyter-echarts
```

最后将你的更新推送至 pyecharts


## 前端编程与 Python

在前端编程领域，没有人会去手动下载和更新 js/css 文件。[npm](https://docs.npmjs.com/getting-started/what-is-npm) 是一个 node.js 的包管理助手，用于帮助前端编程人员去自动化管理 js/css 模块。

当然，还有其他优秀的类似的工具 如 [bower](https://bower.io), [jspm](https://jspm.io) 等等。[gulp](https://gulpjs.com) 是 node.js 中的  `make` 命令，gulpfile.js 是 gulp 的 `Makefile`，你将会使用 js 来编写这些命令。这些优秀的工具可以帮助你自动化管理 js/css 模块，就像 Python 世界的 `pip` 工具。

那现在的前端编程主要在码些什么呢？答案就是 [pug file](https://pugjs.org/api/getting-started.html)/[HAML file](http://haml.info), [sass file](http://sass-lang.com) 和 [coffeescript](http://coffeescript.org)/[typescript](http://www.typescriptlang.org) ，编写这些文件经编译后就会成为 html/css/js 文件了，现在编写网页变成是一个软件工程师干的活了。而面向对象编程，代码复用以及设计 css 属性接口这些事才是前端编程人员的日常工作。

以上是对前端编程的一个简介，node.js 世界有很多很棒的项目，工具以及开发者。期待你去挖掘和发现更多精彩的东西！