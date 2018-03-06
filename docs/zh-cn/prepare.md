[TOC]

### 第一个示例

**Note：** 推荐使用 pyecharts 的最新版本！！

首先开始来绘制你的第一个图表
```python
from pyecharts import Bar

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar.print_echarts_options()
bar.render()
```
![guide-0](https://user-images.githubusercontent.com/19553554/35103909-3ee41ba2-fca2-11e7-87be-1a3585b9e0fa.png)


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
![guide-1](https://user-images.githubusercontent.com/19553554/35104150-f31e1b7c-fca2-11e7-81cf-a12bf1629e02.png)

### 使用 pyecharts-snapshot 插件
如果想直接将图片保存为 png, pdf, gif 格式的文件，可以使用 [pyecharts-snapshot](https://github.com/pyecharts/pyecharts-snapshot)。使用该插件请确保你的系统上已经安装了 node.js 环境，如果没有，请到这里下载 [https://nodejs.org/en/download/](https://nodejs.org/en/download/)

1. 安装 phantomjs  
    `npm install -g phantomjs-prebuilt`
2. 安装 pyecharts-snapshot  
    `pip install pyecharts-snapshot`
3. 引入 pyecharts-snapshot  
    `from pyecharts_snapshot.main import make_a_snapshot`
4. 调用方法  
    `make_a_snapshot('render.html', 'snapshot.png')`  
    make_a_snapshot() 第一个参数为生成的 .html 文件，第二个参数为要保存的文件，可以为 png/pdf/gif

更多内容请移步至 [pyecharts-snapshot](https://github.com/pyecharts/pyecharts-snapshot)  


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
转换数据序列，将带字典和元组类型的序列转换为 k_lst,v_lst 两个列表 
```
1. 元组列表  
    [(A1, B1), (A2, B2), (A3, B3), (A4, B4)] --> k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]
2. 字典列表  
    [{A1: B1}, {A2: B2}, {A3: B3}, {A4: B4}] --> k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]
3. 字典  
    {A1: B1, A2: B2, A3: B3, A4: B4} -- > k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]

### 多次显示图表

> v0.4.0 更新

在 pyecharts 可以连续使用 `chart.render` 在同一个脚本中显示多个图表。

```python
from pyecharts import Bar, Line

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar.render(path='bar.html')

line = Line("我的第一个图表", "这里是副标题")
line.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
line.render(path='line.html')
```

从 v0.4.0 开始，pyecharts 重构了渲染的内部逻辑，改善效率。推荐使用以下方式显示多个图表。

```python
from pyecharts import Bar, Line
from pyecharts.engine import create_default_environment

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])

line = Line("我的第一个图表", "这里是副标题")
line.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])

env = create_default_environment()

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


### 如果在没有互联网的情况下安装 pyecharts 0.3.2 +

首先，您需要通过有互联网的计算机得到这三个包：pyecharts, pyecharts-jupyter-installer, 和 jupyter-echarts-pypkg. 

然后，按照这个顺序组装：

```
pip install pyecharts-jupyter-installer.tar.gz
pip install jupyter-echarts-pypkg.tar.gz
pip install pyecharts.tar.gz
```
