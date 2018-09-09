> 基本用法篇：本文档描述了 pyecharts 库的基本使用用法。

### 安装 pyecharts

#### 兼容性

pyecharts 支持 Python2.7+ 和 Ptyhon3.5+。如果你使用的是 Python2.7，请在代码顶部声明字符编码，否则会出现中文乱码问题。
```python
#coding=utf-8
from __future__ import unicode_literals
```

#### pyecharts

pip 安装
```shell
$ pip install pyecharts
```

源码安装
```shell
$ git clone https://github.com/pyecharts/pyecharts.git
$ cd pyecharts
$ pip install -r requirements.txt
$ python setup.py install
```

#### 地图插件

自从 v0.3.2 开始，为了缩减项目本身的体积以及维持 pyecharts 项目的轻量化运行，pyecharts 将不再自带地图 js 文件。想使用地图的开发者**必须**自己手动安装地图插件。具体参考 [自定义地图篇](zh-cn/customize_map)。


### 快速开始

首先开始来绘制你的第一个图表
```python
from pyecharts import Bar

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
# bar.print_echarts_options() # 该行只为了打印配置项，方便调试时使用
bar.render()    # 生成本地 HTML 文件
```
![guide-0](https://user-images.githubusercontent.com/19553554/35103909-3ee41ba2-fca2-11e7-87be-1a3585b9e0fa.png)


* ```add()```  
    主要方法，用于添加图表的数据和设置各种配置项
* ```print_echarts_options()```  
    打印输出图表的所有配置项
* ```render()```  
    默认将会在根目录下生成一个 render.html 的文件，支持 path 参数，设置文件保存位置，如 render(r"e:\my_first_chart.html")，文件用浏览器打开。

**Note：** 可以按右边的下载按钮将图片下载到本地，如果想要提供更多实用工具按钮，请在 `add()` 中设置 `is_more_utils` 为 True

```python
from pyecharts import Bar

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", 
        ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90],
        is_more_utils=True)
bar.render()
```
![guide-1](https://user-images.githubusercontent.com/19553554/35104150-f31e1b7c-fca2-11e7-81cf-a12bf1629e02.png)


### 使用主题

自 0.5.2+ 起，pyecharts 支持更换主体色系。下面是跟换为 'dark' 的例子：

```python
from pyecharts import Bar

bar = Bar("我的第一个图表", "这里是副标题")
bar.use_theme('dark')
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar.render()
```
![guide-2](https://user-images.githubusercontent.com/4280312/39617664-79789878-4f78-11e8-9f0e-c3a2c371b6cb.png)

pyecharts 支持另外 5 个主体色系，[请移步到主题色系获取更多配置信息](zh-cn/themes)。


### 使用 pyecharts-snapshot 插件

如果想直接将图片保存为 png, pdf, gif 格式的文件，可以使用 [pyecharts-snapshot](https://github.com/pyecharts/pyecharts-snapshot)。使用该插件请确保你的系统上已经安装了 [Nodejs](https://nodejs.org/en/download/) 环境。

1. 安装 phantomjs
    `$ npm install -g phantomjs-prebuilt`
2. 安装 pyecharts-snapshot
    `$ pip install pyecharts-snapshot`
3. 调用 `render` 方法
    `bar.render(path='snapshot.png')`
    文件结尾可以为 svg/jpeg/png/pdf/gif。请注意，svg 文件需要你在初始化 bar 的时候设置 renderer='svg'。

更多内容请移步至 [pyecharts-snapshot](https://github.com/pyecharts/pyecharts-snapshot)


### 图形绘制过程

图表类提供了若干了构建和渲染的方法，在使用的过程中，建议按照以下的顺序分别调用：

| 步骤 | 描述 | 代码示例 | 备注 |
| ------ | ------ | ------ | ------ |
| 1 | 实例一个具体类型图表的对象 |  `chart = FooChart()`| |
| 2  | 为图表添加通用的配置，如主题 |  `chart.use_theme()` | |
| 3  | 为图表添加特定的配置 | `geo.add_coordinate()` | |
| 4  | 添加数据及配置项| `chart.add()` | 参考 [数据解析与导入篇](zh-cn/data_import) |
| 5  | 生成本地文件（html/svg/jpeg/png/pdf/gif）| `chart.render()` | |

从 v0.5.9 开始，以上涉及的方法均支持链式调用。例如：

```python
from pyecharts import Bar

CLOTHES = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
clothes_v1 = [5, 20, 36, 10, 75, 90]
clothes_v2 = [10, 25, 8, 60, 20, 80]

(Bar("柱状图数据堆叠示例")
    .add("商家A", CLOTHES, clothes_v1, is_stack=True)
    .add("商家B", CLOTHES, clothes_v2, is_stack=True)
    .render())
```

### 多次显示图表

从 v0.4.0+ 开始，pyecharts 重构了渲染的内部逻辑，改善效率。推荐使用以下方式显示多个图表。

```python
from pyecharts import Bar, Line
from pyecharts.engine import create_default_environment

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])

line = Line("我的第一个图表", "这里是副标题")
line.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])

env = create_default_environment("html")
# 为渲染创建一个默认配置环境
# create_default_environment(filet_ype)
# file_type: 'html', 'svg', 'png', 'jpeg', 'gif' or 'pdf'

env.render_chart_to_file(bar, path='bar.html')
env.render_chart_to_file(line, path='line.html')
```

相比第一个例子，该代码只是使用同一个引擎对象，减少了部分重复操作，速度有所提高。

### Pandas&Numpy 简单示例

如果使用的是 Numpy 或者 Pandas，可以参考这个示例

![pandas-numpy](https://user-images.githubusercontent.com/19553554/35104252-3e36cee2-fca3-11e7-8e43-09bbe8dbbd1e.png)

**Note：** 使用 Pandas&Numpy 时，整数类型请确保为 int，而不是 numpy.int32

**当然你也可以采用更加酷炫的方式，使用 Jupyter Notebook 来展示图表，matplotlib 有的，pyecharts 也会有的**

**Note：** 从 v0.1.9.2 版本开始，废弃 ```render_notebook()``` 方法，现已采用更加 pythonic 的做法。直接调用本身实例就可以了。

比如这样

![notebook-0](https://user-images.githubusercontent.com/19553554/35104153-f6256212-fca2-11e7-854c-bacc61eabf6f.gif)

还有这样

![notebook-1](https://user-images.githubusercontent.com/19553554/35104157-fa39e170-fca2-11e7-9738-1547e22914a6.gif)

如果使用的是自定义类，直接调用自定义类示例即可

![notebook-2](https://user-images.githubusercontent.com/19553554/35104165-fe9765da-fca2-11e7-8126-920158616b99.gif)

更多 Jupyter notebook 的例子请参考 [notebook-use-cases](https://github.com/pyecharts/pyecharts-users-cases)。可下载后运行看看。

如需使用 Jupyter Notebook 来展示图表，只需要调用自身实例即可，同时兼容 Python2 和 Python3 的 Jupyter Notebook 环境。所有图表均可正常显示，与浏览器一致的交互体验，这下展示报告连 PPT 都省了！！
