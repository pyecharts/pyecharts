# 关于作者想说的
作为 pyecharts 的作者，很高兴看到 pyecharts 最近这么受欢迎，一度冲上了 Python daily trending 和 weekly trending 前三名。大家对这个项目的反馈也都不错，在这里我真诚的感谢大家对这个项目的支持。  
随着使用项目的人越来越多，已经收到了不少希望推出一份英文文档的请求，但是大家提新需求的速度已经远远快于我的开发速度......我还要测试以及解决提出的 issue，实在是没什么时间（加上我英语水平不高这点我是不会告诉你的）。
### 所以，划重点！！！
在这里，我诚恳地向各位对这个项目感兴趣，想参与到项目中来的开发者发出邀请，希望你们可以参与到英文文档的编写中来，成为这个项目的贡献者，一起推动这个项目的发展。英文文档在这里 [doc_en_US.md](https://github.com/chenjiandongx/pyecharts/blob/master/document/doc_en_US.md) ，我已经写了一些，但是还差挺多的。别犹豫了，来吧！
### 接着，划重点！！！
想参与到英文文档开发中来的开发者，请联系我邮箱，chenjiandongx@qq.com，或者加入下面这个微信群，我们可以来具体讨论。不然直接 fork 一份，编写后提交 PR 也行，我看到了会及时 merge 的。

![wechat](https://github.com/chenjiandongx/pyecharts/blob/master/images/wechat.png)
### 最后，划重点！！！
接下来我就暂时不更新版本了，因为作者要出去玩耍几天了，不然感觉这样下去的话我这个暑假就没了！

# pyecharts 文档
pyecharts 是一个用于生成 Echarts 图表的类库。实际上就是 Echarts 与 Python 的对接。  

[![Build Status](https://travis-ci.org/chenjiandongx/pyecharts.svg?branch=master)](https://travis-ci.org/chenjiandongx/pyecharts)  


* [开始使用](https://github.com/chenjiandongx/pyecharts/blob/master/README.md#开始使用)
* [通用配置项](https://github.com/chenjiandongx/pyecharts/blob/master/README.md#通用配置项)
    * xyAxis：直角坐标系中的 x、y 轴(Line、Bar、Scatter、EffectScatter、Kline)
    * dataZoom：dataZoom 组件 用于区域缩放，从而能自由关注细节的数据信息，或者概览数据整体，或者去除离群点的影响。(Line、Bar、Scatter、EffectScatter、Kline)
    * legend：图例组件。图例组件展现了不同系列的标记(symbol)，颜色和名字。可以通过点击图例控制哪些系列不显示。
    * label：图形上的文本标签，可用于说明图形的一些数据信息，比如值，名称等。
    * lineStyle：带线图形的线的风格选项(Line、Polar、Radar、Graph、Parallel)
    * grid3D：3D笛卡尔坐标系组配置项，适用于 3D 图形。（Bar3D, Line3D, Scatter3D)
    * visualMap：是视觉映射组件，用于进行『视觉编码』，也就是将数据映射到视觉元素（视觉通道）

* [图表详细](https://github.com/chenjiandongx/pyecharts/blob/master/README.md#图表详细)
    * Bar（柱状图/条形图）
    * Bar3D（3D 柱状图）
    * EffectScatter（带有涟漪特效动画的散点图）
    * Funnel（漏斗图）
    * Gauge（仪表盘）
    * Geo（地理坐标系）
    * Graph（关系图）
    * HeatMap（热力图）
    * Kline（K线图）
    * Line（折线/面积图）
    * Line3D（3D 折线图）
    * Liquid（水球图）
    * Map（地图）
    * Parallel（平行坐标系）
    * Pie（饼图）
    * Polar（极坐标系）
    * Radar（雷达图）
    * Scatter（散点图）
    * Scatter3D（3D 散点图）
    * WordCloud（词云图）
* [用户自定义](https://github.com/chenjiandongx/pyecharts/blob/master/README.md#用户自定义)
* [更多示例](https://github.com/chenjiandongx/pyecharts/blob/master/README.md#更多示例)
* [关于项目](https://github.com/chenjiandongx/pyecharts/blob/master/README.md#关于项目)


# 开始使用
### 确认你已安装了最新版本的 pyecharts
首先开始来绘制你的第一个图表
```python
from pyecharts import Bar

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar.show_config()
bar.render()
```
![guide-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/guide-0.png)

**Tip：** 可以按右边的下载按钮将图片下载到本地  

* ```add()```  
    主要方法，用于添加图表的数据和设置各种配置项  
* ```show_config()```  
    打印输出图表的所有配置项
* ```render()```  
    默认将会在根目录下生成一个 render.html 的文件，支持 path 参数，设置文件保存位置，如 render(r"e:\my_first_chart.html")，文件用浏览器打开。  

### Python2 编码问题
默认的编码类型为 UTF-8，在 Python3 中是没什么问题的，Python3 对中文的支持好很多。但是在 Python2 中，请应用下面的语句，保证没有编码问题:
```
#!/usr/bin/python
#coding=utf-8
from __future__ import unicode_literals
```
前两句告知你的编辑器你用 UTF-8 ([PEP-0263](https://www.python.org/dev/peps/pep-0263/)). 最后一句告知 Python 所有字符是 UTF-8 ([unicode literals](http://python-future.org/unicode_literals.html))

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

如果使用的是 Numpy 或者 Pandas，直接将数据放入 ```add()``` 方法也可能会出现问题，因为 ```add()``` 方法接受的是两个 list 列表。最后所有的配置项都是要经过 JSON 序列化的，像 int64 这种类型的数据在这个过程是会报错的。  
在这里提供了 ```pdcast(pddata)``` 和 ``` npcast(npdata)``` 两个方法，用于这两个库数据类型的处理。

pdcast()，接受的参数可以为 Series 或者 DataFrame 类型。
```python
@staticmethod
pdcast(pddata)
``` 用于处理 Pandas 中的 Series 和 DataFrame 类型，返回 value_lst, index_list 两个列表 ```
```
1. 传入的类型为 Series 的话，pdcast() 会返回两个确保类型正确的列表（整个列表的数据类型为 float 或者 str，会先尝试转换为数值类型的 float，出现异常再尝试转换为 str 类型），value_lst 和 index_lst，分别为 Series.values 和 Series.index 列表。
2. 传入的类型为 DataFrame 的话，pdcast() 会返回一个确保类型正确的列表（整个列表的数据类型为 float 或者 str，会先尝试转换为数值类型的 float，出现异常再尝试转换为 str 类型），为 DataFrame.values 列表。多个维度时返回一个嵌套列表。比较适合像 Radar, Parallel, HeatMap 这些需要传入嵌套列表（[[ ], [ ]]）数据的图表。

npcast()，接受的参数为 Numpy.array 类型。
```python
@staticmethod
npcast(npdata)
``` 用于处理 Numpy 中的 ndarray 类型，返回一个确保类型正确的列表。如果多个维度的话返回嵌套列表。```
```

**当然你也可以采用更加酷炫的方式，使用 Jupyter Notebook 来展示图表，matplotlib 有的，pyecharts 也会有的**  

比如这样  

![jupyter-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/jupyter-0.gif)

还有这样

![jupyter-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/jupyter-1.gif)

![jupyter-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/jupyter-2.gif)


这里只是举几个例子。如需使用 Jupyter Notebook 来展示图表，只需要调用 ```render_notebook()``` 即可，同时兼容 Python2 和 Python3 的 Jupyter Notebook 环境。所有图表均可正常显示（除了 3D 图），与浏览器一致的交互体验，这下展示报告连 PPT 都省了！！  
> 在这里要特别感谢 [@ygw365](https://github.com/ygw365) 提供这部分的代码模板 和 [@muxuezi](https://github.com/muxuezi) 协助对代码进行改进，特此感谢！

图表类初始化所接受的参数（所有类型的图表都一样）。

* title -> str   
    主标题文本，支持 \n 换行，默认为 ""
* subtitle -> str  
    副标题文本，支持 \n 换行，默认为 ""
* width -> int  
    画布宽度，默认为 800（px）
* height -> int  
    画布高度，默认为 400（px）
* title_pos -> str/int  
    标题距离左侧距离，默认为'left'，有'auto', 'left', 'right', 'center'可选，也可为百分比或整数
* title_top -> str/int  
    标题距离顶部距离，默认为'top'，有'top', 'middle', 'bottom'可选，也可为百分比或整数
* title_color -> str  
    主标题文本颜色，默认为 '#000'
* subtitle_color -> str  
    副标题文本颜色，默认为 '#aaa'
* title_text_size -> int  
    主标题文本字体大小，默认为 18
* subtitle_text_size -> int  
    副标题文本字体大小，默认为 12
* background_color -> str  
    画布背景颜色，默认为 '#fff'
* is_grid -> bool  
    是否使用 grid 组件，grid 组件用于并行显示图表。具体实现参见 [用户自定义](https://github.com/chenjiandongx/pyecharts/blob/master/README.md#用户自定义)
    
# 通用配置项
**通用配置项均在 ```add()``` 中设置**

xyAxis：直角坐标系中的 x、y 轴(Line、Bar、Scatter、EffectScatter、Kline)

* is_convert -> bool  
    是否交换 x 轴与 y 轴
* xy_text_size -> int  
    x 轴和 y 轴字体大小
* namegap -> int  
    坐标轴名称与轴线之间的距离
* x_axis -> list  
    x 轴数据项
* xaxis_name -> str  
    x 轴名称
* xaxis_name_pos -> str  
    x 轴名称位置，有'start'，'middle'，'end'可选
* xaxis_rotate -> int  
    刻度标签旋转的角度，在类目轴的类目标签显示不下的时候可以通过旋转防止标签之间重叠。默认为 0，即不旋转。旋转的角度从 -90 度到 90 度。
* y_axis -> list  
    y 坐标轴数据
* yaxis_formatter -> str  
    y 轴标签格式器，如 '天'，则 y 轴的标签为数据加'天'(3 天，4 天),默认为 ""
* yaxis_name -> str  
    y 轴名称
* yaxis_name_pos -> str  
    y 轴名称位置，有'start', 'middle'，'end'可选
* yaxis_rotate -> int  
    刻度标签旋转的角度，在类目轴的类目标签显示不下的时候可以通过旋转防止标签之间重叠。默认为 0，即不旋转。旋转的角度从 -90 度到 90 度。
* interval -> int  
    坐标轴刻度标签的显示间隔，在类目轴中有效。默认会采用标签不重叠的策略间隔显示标签  
    设置成 0 强制显示所有标签。设置为 1，表示『隔一个标签显示一个标签』，如果值为 2，表示隔两个标签显示一个标签，以此类推


dataZoom：dataZoom 组件 用于区域缩放，从而能自由关注细节的数据信息，或者概览数据整体，或者去除离群点的影响。(Line、Bar、Scatter、EffectScatter、Kline)

* is_datazoom_show -> bool  
    是否使用区域缩放组件，默认为 False
* datazoom_type -> str    
    区域缩放组件类型，默认为'slider'，有'slider', 'inside'可选
* datazoom_range -> list    
    区域缩放的范围，默认为[50, 100]
* datazoom_orient -> str  
    datazomm 组件在直角坐标系中的方向，默认为 'horizontal'，效果显示在 x 轴。如若设置为 'vertical' 的话效果显示在 y 轴。


legend：图例组件。图例组件展现了不同系列的标记(symbol)，颜色和名字。可以通过点击图例控制哪些系列不显示。

* is_legend_show -> bool  
    是否显示顶端图例，默认为 True
* legend_orient -> str  
    图例列表的布局朝向，默认为'horizontal'，有'horizontal', 'vertical'可选
* legend_pos -> str  
    图例组件离容器左侧的距离，默认为'center'，有'left', 'center', 'right'可选
* legend_top -> str  
    图例组件离容器上侧的距离，默认为'top'，有'top', 'center', 'bottom'可选
* legend_selectedmode -> str/bool  
    图例选择的模式，控制是否可以通过点击图例改变系列的显示状态。默认为'multiple'，可以设成 'single' 或者 'multiple' 使用单选或者多选模式。也可以设置为 False 关闭显示状态。
    

label：图形上的文本标签，可用于说明图形的一些数据信息，比如值，名称等。

* is_label_show -> bool  
    是否正常显示标签，默认不显示。标签即各点的数据项信息  
* is_emphasis -> bool  
    是否高亮显示标签，默认显示。高亮标签即选中数据时显示的信息项。
* label_pos -> str  
    标签的位置，Bar 图默认为'top'。有'top', 'left', 'right', 'bottom', 'inside','outside'可选
* label_text_color -> str  
    标签字体颜色，默认为 "#000"
* label_text_size -> int  
    标签字体大小，默认为 12
* is_random -> bool  
    是否随机排列颜色列表，默认为 False
* label_color -> list  
    自定义标签颜色。全局颜色列表，所有图表的图例颜色均在这里修改。如 Bar 的柱状颜色，Line 的线条颜色等等。
* formatter -> list  
    标签内容格式器，有'series', 'name', 'value', 'percent'可选。如 ["name", "value"]
    * series：图例名称
    * name：数据项名称
    * value：数据项值
    * percent：数据的百分比（主要用于饼图）

**Tip：** is_random 可随机打乱图例颜色列表，算是切换风格？建议试一试！


lineStyle：带线图形的线的风格选项(Line、Polar、Radar、Graph、Parallel)

* line_width -> int    
    线的宽度，默认为 1
* line_opacity -> float    
    线的透明度，0 为完全透明，1 为完全不透明。默认为 1
* line_curve -> float    
    线的弯曲程度，0 为完全不弯曲，1 为最弯曲。默认为 0
* line_type -> str  
    线的类型，有'solid', 'dashed', 'dotted'可选。默认为'solid'

grid3D：3D笛卡尔坐标系组配置项，适用于 3D 图形。（Bar3D, Line3D, Scatter3D)

* grid3D_width -> int  
    三维笛卡尔坐标系组件在三维场景中的高度。默认为 100
* grid3D_height -> int  
    三维笛卡尔坐标系组件在三维场景中的高度。默认为 100
* grid3D_depth -> int  
    三维笛卡尔坐标系组件在三维场景中的高度。默认为 100
* is_grid3D_rotate -> bool  
    是否开启视角绕物体的自动旋转查看。默认为 False
* grid3D_rotate_speed -> int  
    物体自传的速度。单位为角度 / 秒，默认为 10 ，也就是 36 秒转一圈。
* grid3D_rotate_sensitivity -> int  
    旋转操作的灵敏度，值越大越灵敏。默认为 1, 设置为 0 后无法旋转。

visualMap：是视觉映射组件，用于进行『视觉编码』，也就是将数据映射到视觉元素（视觉通道）

* is_visualmap -> bool  
    是否使用视觉映射组件
* visual_type -> str  
    制定组件映射方式，默认为'color‘，即通过颜色来映射数值。有'color', 'size'可选。'szie'通过数值点的大小，也就是图形点的大小来映射数值。
* visual_range -> list  
    指定组件的允许的最小值与最大值。默认为 [0, 100]
* visual_text_color -> list  
    两端文本颜色。
* visual_range_text -> list  
    两端文本。默认为 ['low', 'hight']
* visual_range_color -> list  
    过渡颜色。默认为 ['#50a3ba', '#eac763', '#d94e5d']
* visual_range_size -> list  
    数值映射的范围，也就是图形点大小的范围。默认为 [20, 50]
* visual_orient -> str  
    visualMap 组件条的方向，默认为'vertical'，有'vertical', 'horizontal'可选。
* visual_pos -> str/int  
    visualmap 组件条距离左侧的位置，默认为'left'。有'right', 'center', 'right'可选，也可为百分数或整数。
* visual_top -> str/int  
    visualmap 组件条距离顶部的位置，默认为'top'。有'top', 'center', 'bottom'可选，也可为百分数或整数。
* is_calculable -> bool  
    是否显示拖拽用的手柄（手柄能拖拽调整选中范围）。默认为 True


# 图表详细  

## Bar（柱状图/条形图）
> 柱状/条形图，通过柱形的高度/条形的宽度来表现数据的大小。

Bar.add() 方法签名
```python
add(name, x_axis, y_axis, is_stack=False, **kwargs)
```
* name -> str  
    图例名称
* x_axis -> list  
    x 坐标轴数据
* y_axis -> list  
    y 坐标轴数据  
* is_stack -> bool  
    数据堆叠，同个类目轴上系列配置相同的 stack 值可以堆叠放置  

```python
from pyecharts import Bar

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图数据堆叠示例")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True)
bar.render()
```
![bar-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/bar-0.gif)  
**Tip：** 全局配置项要在最后一个 ```add()``` 上设置，否侧设置会被冲刷掉。

```python
from pyecharts import Bar

bar = Bar("标记线和标记点示例")
bar.add("商家A", attr, v1, mark_point=["average"])
bar.add("商家B", attr, v2, mark_line=["min", "max"])
bar.render()
```
![bar-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/bar-1.gif)

* mark_point  -> list  
    标记点，有'min', 'max', 'average'可选
* mark_line  -> list  
    标记线，有'min', 'max', 'average'可选
* mark_point_symbol -> str  
    标记点图形，，默认为'pin'，有'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'可选
* mark_point_symbolsize -> int  
    标记点图形大小，默认为 50
* mark_point_textcolor -> str  
    标记点字体颜色，默认为'#fff'

```python
from pyecharts import Bar

bar = Bar("x 轴和 y 轴交换")
bar.add("商家A", attr, v1)
bar.add("商家B", attr, v2, is_convert=True)
bar.render()
```
![bar-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/bar-2.png)

dataZoom 效果，'slider' 类型
```python
import random

attr = ["{}天".format(i) for i in range(30)]
v1 = [random.randint(1, 30) for _ in range(30)]
bar = Bar("Bar - datazoom - slider 示例")
bar.add("", attr, v1, is_label_show=True, is_datazoom_show=True)
bar.show_config()
bar.render()
```
![bar-4](https://github.com/chenjiandongx/pyecharts/blob/master/images/bar-4.gif)

'inside' 类型
```python
attr = ["{}天".format(i) for i in range(30)]
v1 = [random.randint(1, 30) for _ in range(30)]
bar = Bar("Bar - datazoom - inside 示例")
bar.add("", attr, v1, is_datazoom_show=True, datazoom_type='inside', datazoom_range=[10, 25])
bar.show_config()
bar.render()
```
![bar-5](https://github.com/chenjiandongx/pyecharts/blob/master/images/bar-5.gif)  

**Tip：** datazoom 适合所有平面直角坐标系图形，也就是(Line、Bar、Scatter、EffectScatter、Kline)  
**Tip：** 可以通过 label_color 来设置柱状的颜色，如 ['#eee', '#000']，所有的图表类型的图例颜色都可通过 label_color 来修改。


## Bar3D（3D 柱状图）

Bar3D.add() 方法签名
```python
add(name, x_axis, y_axis, data, grid3D_opacity=1, grid3D_shading='color', **kwargs)
```
* name -> str  
    图例名称
* x_axis -> str  
    x 坐标轴数据。需为类目轴，也就是不能是数值。
* y_axis -> str  
    y 坐标轴数据。需为类目轴，也就是不能是数值。
* data -> [list],包含列表的列表  
    数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』
* grid3D_opacity -> int  
    3D 笛卡尔坐标系组的透明度（柱状的透明度），默认为 1，完全不透明。
* grid3D_shading -> str  
    三维柱状图中三维图形的着色效果。
    * color：只显示颜色，不受光照等其它因素的影响。
    * lambert：通过经典的 lambert 着色表现光照带来的明暗。
    * realistic：真实感渲染，配合 light.ambientCubemap 和 postEffect 使用可以让展示的画面效果和质感有质的提升。ECharts GL 中使用了基于物理的渲染（PBR) 来表现真实感材质。

```python
from pyecharts import Bar3D

bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
x_axis = ["12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
          "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"]
y_aixs = ["Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"]
data = [[0, 0, 5], [0, 1, 1], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0], [0, 6, 0], [0, 7, 0],
        [0, 8, 0],[0, 9, 0], [0, 10, 0], [0, 11, 2], [0, 12, 4], [0, 13, 1], [0, 14, 1], [0, 15, 3],
        [0, 16, 4], [0, 17, 6], [0, 18, 4], [0, 19, 4], [0, 20, 3], [0, 21, 3], [0, 22, 2], [0, 23, 5],
        [1, 0, 7], [1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0], [1, 6, 0], [1, 7, 0], [1, 8, 0],
        [1, 9, 0], [1, 10, 5], [1, 11, 2], [1, 12, 2], [1, 13, 6], [1, 14, 9], [1, 15, 11], [1, 16, 6], [1, 17, 7],
        [1, 18, 8], [1, 19, 12], [1, 20, 5], [1, 21, 5], [1, 22, 7], [1, 23, 2], [2, 0, 1], [2, 1, 1],
        [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0], [2, 6, 0], [2, 7, 0], [2, 8, 0], [2, 9, 0], [2, 10, 3],
        [2, 11, 2], [2, 12, 1], [2, 13, 9], [2, 14, 8], [2, 15, 10], [2, 16, 6], [2, 17, 5], [2, 18, 5],
        [2, 19, 5], [2, 20, 7], [2, 21, 4], [2, 22, 2], [2, 23, 4], [3, 0, 7], [3, 1, 3], [3, 2, 0], [3, 3, 0],
        [3, 4, 0], [3, 5, 0], [3, 6, 0], [3, 7, 0], [3, 8, 1], [3, 9, 0], [3, 10, 5], [3, 11, 4], [3, 12, 7],
        [3, 13, 14], [3, 14, 13], [3, 15, 12], [3, 16, 9], [3, 17, 5], [3, 18, 5], [3, 19, 10], [3, 20, 6],
        [3, 21, 4], [3, 22, 4], [3, 23, 1], [4, 0, 1], [4, 1, 3], [4, 2, 0], [4, 3, 0], [4, 4, 0], [4, 5, 1],
        [4, 6, 0], [4, 7, 0], [4, 8, 0], [4, 9, 2], [4, 10, 4], [4, 11, 4], [4, 12, 2], [4, 13, 4], [4, 14, 4],
        [4, 15, 14], [4, 16, 12], [4, 17, 1], [4, 18, 8], [4, 19, 5], [4, 20, 3], [4, 21, 7], [4, 22, 3],
        [4, 23, 0], [5, 0, 2], [5, 1, 1], [5, 2, 0], [5, 3, 3], [5, 4, 0], [5, 5, 0], [5, 6, 0], [5, 7, 0],
        [5, 8, 2], [5, 9, 0], [5, 10, 4], [5, 11, 1], [5, 12, 5], [5, 13, 10], [5, 14, 5], [5, 15, 7], [5, 16, 11],
        [5, 17, 6], [5, 18, 0], [5, 19, 5], [5, 20, 3], [5, 21, 4], [5, 22, 2], [5, 23, 0], [6, 0, 1], [6, 1, 0],
        [6, 2, 0], [6, 3, 0], [6, 4, 0], [6, 5, 0], [6, 6, 0], [6, 7, 0], [6, 8, 0], [6, 9, 0], [6, 10, 1],
        [6, 11, 0], [6, 12, 2], [6, 13, 1], [6, 14, 3], [6, 15, 4], [6, 16, 0], [6, 17, 0], [6, 18, 0], [6, 19, 0],
        [6, 20, 1], [6, 21, 2], [6, 22, 2], [6, 23, 6]]
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
bar3d.add("", x_axis, y_aixs, [[d[1], d[0], d[2]] for d in data], is_visualmap=True,
          visual_range=[0, 20], visual_range_color=range_color, grid3D_width=200, grid3D_depth=80)
bar3d.show_config()
bar3d.render()
```
![bar3D-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/bar3D-0.gif)

设置 ``` grid3D_shading``` 可以让柱状更真实  
```python
bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
bar3d.add("", x_axis, y_aixs, [[d[1], d[0], d[2]] for d in data], is_visualmap=True,
          visual_range=[0, 20], visual_range_color=range_color, grid3D_width=200, grid3D_depth=80,
          grid3D_shading='lambert')
bar3d.show_config()
bar3d.render()
```
![bar3D-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/bar3D-1.gif)

设置 ```is_grid3D_rotate``` 启动自动旋转功能
```python
bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
bar3d.add("", x_axis, y_aixs, [[d[1], d[0], d[2]] for d in data], is_visualmap=True,
          visual_range=[0, 20], visual_range_color=range_color, grid3D_width=200, grid3D_depth=80,
          is_grid3D_rotate=True)
bar3d.show_config()
bar3d.render()
```
![bar3D-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/bar3D-2.gif)

设置 ``` grid3D_rotate_speed``` 调节旋转速度
```python
bar3d = Bar3D("3D 柱状图示例", width=1200, height=600)
bar3d.add("", x_axis, y_aixs, [[d[1], d[0], d[2]] for d in data], is_visualmap=True,
          visual_range=[0, 20], visual_range_color=range_color, grid3D_width=200, grid3D_depth=80,
          is_grid3D_rotate=True, grid3D_rotate_speed=180)
bar3d.show_config()
bar3d.render()
```
![bar3D-3](https://github.com/chenjiandongx/pyecharts/blob/master/images/bar3D-3.gif)

**Tip：** 关于 gird3D 部分的设置，请参照通用配置项中的介绍 [通用配置项](https://github.com/chenjiandongx/pyecharts/blob/master/README.md#通用配置项)  


## EffectScatter（带有涟漪特效动画的散点图）
> 利用动画特效可以将某些想要突出的数据进行视觉突出。

EffectScatter.add() 方法签名
```python
add(name, x_value, y_value, symbol_size=10, **kwargs)
```
* name -> str  
    图例名称
* x_axis -> list  
    x 坐标轴数据
* y_axis -> list  
    y 坐标轴数据
* symbol_size -> int  
    标记图形大小，默认为 10
    
```python
from pyecharts import EffectScatter

v1 = [10, 20, 30, 40, 50, 60]
v2 = [25, 20, 15, 10, 60, 33]
es = EffectScatter("动态散点图示例")
es.add("effectScatter", v1, v2)
es.render()
```
![effectscatter-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/effectscatter-0.gif)

```python
es = EffectScatter("动态散点图各种图形示例")
es.add("", [10], [10], symbol_size=20, effect_scale=3.5, effect_period=3, symbol="pin")
es.add("", [20], [20], symbol_size=12, effect_scale=4.5, effect_period=4,symbol="rect")
es.add("", [30], [30], symbol_size=30, effect_scale=5.5, effect_period=5,symbol="roundRect")
es.add("", [40], [40], symbol_size=10, effect_scale=6.5, effect_brushtype='fill',symbol="diamond")
es.add("", [50], [50], symbol_size=16, effect_scale=5.5, effect_period=3,symbol="arrow")
es.add("", [60], [60], symbol_size=6, effect_scale=2.5, effect_period=3,symbol="triangle")
es.render()
```
![effectscatter-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/effectscatter-1.gif)

* symbol -> str  
    标记图形，有'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'可选
* effect_brushtype -> str  
    波纹绘制方式，有'stroke', 'fill'可选。默认为'stroke'
* effect_scale -> float  
    动画中波纹的最大缩放比例。默认为 2.5
* effect_period -> float  
    动画持续的时间。默认为 4（s）


## Funnel（漏斗图）
Funnel.add() 方法签名
```python
add(self, name, attr, value, **kwargs)
```
* name -> str  
    图例名称
* attr -> list  
    属性名称
* value -> list  
    属性所对应的值

```python
from pyecharts import Funnel

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
value = [20, 40, 60, 80, 100, 120]
funnel = Funnel("漏斗图示例")
funnel.add("商品", attr, value, is_label_show=True, label_pos="inside", label_text_color="#fff")
funnel.render()
```
![funnel-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/funnel-0.gif)

```python
funnel = Funnel("漏斗图示例", width=600, height=400, title_pos='center')
funnel.add("商品", attr, value, is_label_show=True, label_pos="outside", legend_orient='vertical',
           legend_pos='left')
funnel.show_config()
funnel.render()
```
![funnel-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/funnel-1.png)


## Gauge（仪表盘）
Gauge.add() 方法签名
```python
add(name, attr, value, scale_range=None, angle_range=None, **kwargs)
```
* name -> str  
    图例名称
* attr -> list  
    属性名称
* value -> list
    属性所对应的值
* scale_range -> list  
    仪表盘数据范围。默认为 [0, 100]
* angle_range -> list  
    仪表盘角度范围。默认为 [225, -45]
    
```python
from pyecharts import Gauge

gauge = Gauge("仪表盘示例")
gauge.add("业务指标", "完成率", 66.66)
gauge.show_config()
gauge.render()
```
![gauge-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/gauge-0.png)

```python
gauge = Gauge("仪表盘示例")
gauge.add("业务指标", "完成率", 166.66, angle_range=[180, 0], scale_range=[0, 200], is_legend_show=False)
gauge.show_config()
gauge.render()
```
![gauge-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/gauge-1.png)


## Geo（地理坐标系）
> 地理坐标系组件用于地图的绘制，支持在地理坐标系上绘制散点图，线集。

Geo.add() 方法签名
```python
add(name, attr, value, type="scatter", maptype='china', symbol_size=12, border_color="#111",
    geo_normal_color="#323c48", geo_emphasis_color="#2a333d", **kwargs)
```
* name -> str  
    图例名称
* attr -> list  
    属性名称
* value -> list   
    属性所对应的值
* type -> str  
    图例类型，有'scatter', 'effectscatter', 'heatmap'可选。默认为 'scatter'
* maptype -> str  
    地图类型。目前只支持'china'。
* symbol_size -> int  
    标记图形大小。默认为 12
* border_color -> str  
    地图边界颜色。默认为 '#111'
* geo_normal_color -> str  
    正常状态下地图区域的颜色。默认为 '#323c48'
* geo_emphasis_color -> str  
    高亮状态下地图区域的颜色。默认为 '#2a333d'

Scatter 类型
```python
from pyecharts import Geo

data = [
    ("海门", 9),("鄂尔多斯", 12),("招远", 12),("舟山", 12),("齐齐哈尔", 14),("盐城", 15),
    ("赤峰", 16),("青岛", 18),("乳山", 18),("金昌", 19),("泉州", 21),("莱西", 21),
    ("日照", 21),("胶南", 22),("南通", 23),("拉萨", 24),("云浮", 24),("梅州", 25),
    ("文登", 25),("上海", 25),("攀枝花", 25),("威海", 25),("承德", 25),("厦门", 26),
    ("汕尾", 26),("潮州", 26),("丹东", 27),("太仓", 27),("曲靖", 27),("烟台", 28),
    ("福州", 29),("瓦房店", 30),("即墨", 30),("抚顺", 31),("玉溪", 31),("张家口", 31),
    ("阳泉", 31),("莱州", 32),("湖州", 32),("汕头", 32),("昆山", 33),("宁波", 33),
    ("湛江", 33),("揭阳", 34),("荣成", 34),("连云港", 35),("葫芦岛", 35),("常熟", 36),
    ("东莞", 36),("河源", 36),("淮安", 36),("泰州", 36),("南宁", 37),("营口", 37),
    ("惠州", 37),("江阴", 37),("蓬莱", 37),("韶关", 38),("嘉峪关", 38),("广州", 38),
    ("延安", 38),("太原", 39),("清远", 39),("中山", 39),("昆明", 39),("寿光", 40),
    ("盘锦", 40),("长治", 41),("深圳", 41),("珠海", 42),("宿迁", 43),("咸阳", 43),
    ("铜川", 44),("平度", 44),("佛山", 44),("海口", 44),("江门", 45),("章丘", 45),
    ("肇庆", 46),("大连", 47),("临汾", 47),("吴江", 47),("石嘴山", 49),("沈阳", 50),
    ("苏州", 50),("茂名", 50),("嘉兴", 51),("长春", 51),("胶州", 52),("银川", 52),
    ("张家港", 52),("三门峡", 53),("锦州", 54),("南昌", 54),("柳州", 54),("三亚", 54),
    ("自贡", 56),("吉林", 56),("阳江", 57),("泸州", 57),("西宁", 57),("宜宾", 58),
    ("呼和浩特", 58),("成都", 58),("大同", 58),("镇江", 59),("桂林", 59),("张家界", 59),
    ("宜兴", 59),("北海", 60),("西安", 61),("金坛", 62),("东营", 62),("牡丹江", 63),
    ("遵义", 63),("绍兴", 63),("扬州", 64),("常州", 64),("潍坊", 65),("重庆", 66),
    ("台州", 67),("南京", 67),("滨州", 70),("贵阳", 71),("无锡", 71),("本溪", 71),
    ("克拉玛依", 72),("渭南", 72),("马鞍山", 72),("宝鸡", 72),("焦作", 75),("句容", 75),
    ("北京", 79),("徐州", 79),("衡水", 80),("包头", 80),("绵阳", 80),("乌鲁木齐", 84),
    ("枣庄", 84),("杭州", 84),("淄博", 85),("鞍山", 86),("溧阳", 86),("库尔勒", 86),
    ("安阳", 90),("开封", 90),("济南", 92),("德阳", 93),("温州", 95),("九江", 96),
    ("邯郸", 98),("临安", 99),("兰州", 99),("沧州", 100),("临沂", 103),("南充", 104),
    ("天津", 105),("富阳", 106),("泰安", 112),("诸暨", 112),("郑州", 113),("哈尔滨", 114),
    ("聊城", 116),("芜湖", 117),("唐山", 119),("平顶山", 119),("邢台", 119),("德州", 120),
    ("济宁", 120),("荆州", 127),("宜昌", 130),("义乌", 132),("丽水", 133),("洛阳", 134),
    ("秦皇岛", 136),("株洲", 143),("石家庄", 147),("莱芜", 148),("常德", 152),("保定", 153),
    ("湘潭", 154),("金华", 157),("岳阳", 169),("长沙", 175),("衢州", 177),("廊坊", 193),
    ("菏泽", 194),("合肥", 229),("武汉", 273),("大庆", 279)]

geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center",
width=1200, height=600, background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, visual_range=[0, 200], visual_text_color="#fff", symbol_size=15, is_visualmap=True)
geo.show_config()
geo.render()
```
![geo-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/geo-0.gif)

**Tip：** 请配合 [通用配置项](https://github.com/chenjiandongx/pyecharts/blob/master/README.md#通用配置项) 中的 Visualmap 使用

HeatMap 类型
```python
geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center", width=1200, height=600,
          background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, type="heatmap", is_visualmap=True, visual_range=[0, 300], visual_text_color='#fff')
geo.show_config()
geo.render()
```
![geo-0-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/geo-0-1.gif)

EffectScatter 类型
```python
from pyecharts import Geo

data = [("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15)]
geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center",
          width=1200, height=600, background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, type="effectScatter", is_random=True, effect_scale=5)
geo.show_config()
geo.render()
```
![geo-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/geo-1.gif)


## Graph（关系图）
> 用于展现节点以及节点之间的关系数据。

Graph.add() 方法签名
```python
add(name, nodes, links, categories=None, is_focusnode=True, is_roam=True, is_rotatelabel=False,
    layout="force", edge_length=50, gravity=0.2, repulsion=50, **kwargs)
```
* name -> str  
    图例名称
* nodes -> dict  
    关系图结点，包含的数据项有  
    * name：结点名称（必须有！）
    * x：节点的初始 x 值
    * y：节点的初始 y 值
    * value：结点数值 
    * category：结点类目
    * symbol：标记图形
    * symbolSize：标记图形大小
* links -> dict  
    结点间的关系数据，包含的数据项有  
    * source：边的源节点名称的字符串，也支持使用数字表示源节点的索引（必须有！）
    * target：边的目标节点名称的字符串，也支持使用数字表示源节点的索引（必须有！）
    * vaule：边的数值，可以在力引导布局中用于映射到边的长度
* categories -> list  
    结点分类的类目，结点可以指定分类，也可以不指定。  
    如果节点有分类的话可以通过 nodes[i].category 指定每个节点的类目，类目的样式会被应用到节点样式上
* is_focusnode -> bool  
    是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。默认为 True
* is_roam -> bool/str  
    是否开启鼠标缩放和平移漫游。默认为 True  
    如果只想要开启缩放或者平移，可以设置成'scale'或者'move'。设置成 True 为都开启
* is_rotatelabel -> bool  
    是否旋转标签，默认为 False
* layout -> str  
    关系图布局，默认为 'force'
    * none：不采用任何布局，使用节点中必须提供的 x， y 作为节点的位置。
    * circular：采用环形布局
    * force：采用力引导布局
* edge_length -> int  
    力布局下边的两个节点之间的距离，这个距离也会受 repulsion 影响。默认为 50  
    支持设置成数组表达边长的范围，此时不同大小的值会线性映射到不同的长度。值越小则长度越长
* gravity -> int  
    节点受到的向中心的引力因子。该值越大节点越往中心点靠拢。默认为 0.2
* repulsion -> int  
    节点之间的斥力因子。默认为 50  
    支持设置成数组表达斥力的范围，此时不同大小的值会线性映射到不同的斥力。值越大则斥力越大

```python
from pyecharts import Graph

nodes = [{"name": "结点1", "symbolSize": 10},
         {"name": "结点2", "symbolSize": 20},
         {"name": "结点3", "symbolSize": 30},
         {"name": "结点4", "symbolSize": 40},
         {"name": "结点5", "symbolSize": 50},
         {"name": "结点6", "symbolSize": 40},
         {"name": "结点7", "symbolSize": 30},
         {"name": "结点8", "symbolSize": 20}]
links = []
for i in nodes:
    for j in nodes:
        links.append({"source": i.get('name'), "target": j.get('name')})
graph = Graph("关系图-力引导布局示例")
graph.add("", nodes, links, repulsion=8000)
graph.show_config()
graph.render()

```
![graph-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/graph-0.png)

```python
graph = Graph("关系图-环形布局示例")
graph.add("", nodes, links, is_label_show=True, repulsion=8000, layout='circular', label_text_color=None)
graph.show_config()
graph.render()
```
![graph-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/graph-1.png)

```python
from pyecharts import Graph

import json
with open("..\json\weibo.json", "r", encoding="utf-8") as f:
    j = json.load(f)
    nodes, links, categories, cont, mid, userl = j
graph = Graph("微博转发关系图", width=1200, height=600)
graph.add("", nodes, links, categories, label_pos="right", repulsion=50, is_legend_show=False,
          line_curve=0.2, label_text_color=None)
graph.show_config()
graph.render()
```
![graph-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/graph-2.gif)

**Tip：** 可配置 **lineStyle** 参数


# HeatMap（热力图）
> 热力图主要通过颜色去表现数值的大小，必须要配合 visualMap 组件使用。直角坐标系上必须要使用两个类目轴。

HeatMap.add() 方法签名
```python
add(name, x_axis, y_axis, data, **kwargs)
```
* name -> str  
    图例名称
* x_axis -> str  
    x 坐标轴数据。需为类目轴，也就是不能是数值。
* y_axis -> str  
    y 坐标轴数据。需为类目轴，也就是不能是数值。
* data -> [list],包含列表的列表    
    数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』
```python
import random
from pyecharts import HeatMap

x_axis = ["12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
          "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"]
y_aixs = ["Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"]
data = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
heatmap = HeatMap()
heatmap.add("热力图直角坐标系", x_axis, y_aixs, data, is_visualmap=True,
            visual_text_color="#000", visual_orient='horizontal')
heatmap.show_config()
heatmap.render()
```
![heatmap-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/heatmap-0.gif)

**Tip：** 热力图必须配合 [通用配置项](https://github.com/chenjiandongx/pyecharts/blob/master/README.md#通用配置项) 中的 VisualMap 使用才有效果。


## Kline（K线图）
> 红涨蓝跌

Kline.add() 方法签名
```python
add(name, x_axis, y_axis, **kwargs)
```
* name -> str  
    图例名称
* x_axis -> list  
    x 坐标轴数据
* y_axis -> [list],包含列表的列表   
    y 坐标轴数据。数据中，每一行是一个『数据项』，每一列属于一个『维度』。
    数据项具体为 [open, close, lowest, highest] （即：[开盘值, 收盘值, 最低值, 最高值]）
```python
from pyecharts import Kline

v1 = [[2320.26, 2320.26, 2287.3, 2362.94], [2300, 2291.3, 2288.26, 2308.38],
      [2295.35, 2346.5, 2295.35, 2345.92], [2347.22, 2358.98, 2337.35, 2363.8],
      [2360.75, 2382.48, 2347.89, 2383.76], [2383.43, 2385.42, 2371.23, 2391.82],
      [2377.41, 2419.02, 2369.57, 2421.15], [2425.92, 2428.15, 2417.58, 2440.38],
      [2411, 2433.13, 2403.3, 2437.42], [2432.68, 2334.48, 2427.7, 2441.73],
      [2430.69, 2418.53, 2394.22, 2433.89], [2416.62, 2432.4, 2414.4, 2443.03],
      [2441.91, 2421.56, 2418.43, 2444.8], [2420.26, 2382.91, 2373.53, 2427.07],
      [2383.49, 2397.18, 2370.61, 2397.94], [2378.82, 2325.95, 2309.17, 2378.82],
      [2322.94, 2314.16, 2308.76, 2330.88], [2320.62, 2325.82, 2315.01, 2338.78],
      [2313.74, 2293.34, 2289.89, 2340.71], [2297.77, 2313.22, 2292.03, 2324.63],
      [2322.32, 2365.59, 2308.92, 2366.16], [2364.54, 2359.51, 2330.86, 2369.65],
      [2332.08, 2273.4, 2259.25, 2333.54], [2274.81, 2326.31, 2270.1, 2328.14],
      [2333.61, 2347.18, 2321.6, 2351.44], [2340.44, 2324.29, 2304.27, 2352.02],
      [2326.42, 2318.61, 2314.59, 2333.67], [2314.68, 2310.59, 2296.58, 2320.96],
      [2309.16, 2286.6, 2264.83, 2333.29], [2282.17, 2263.97, 2253.25, 2286.33],
      [2255.77, 2270.28, 2253.31, 2276.22]]
kline = Kline("K 线图示例")
kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1)
kline.show_config()
kline.render()
```
![kline-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/kline-0.png)

Kline + dataZoom
```python
kline = Kline("K 线图示例")
kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1, mark_point=["max"], is_datazoom_show=True)
kline.show_config()
kline.render()
```
![kline-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/kline-1.gif)

dataZoom 效果加在纵坐标轴上
```python
kline = Kline("K 线图示例")
kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1, mark_point=["max"],
          is_datazoom_show=True, datazoom_orient='vertical')
kline.show_config()
kline.render()
```
![kline-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/kline-2.gif)


## Line（折线/面积图）
> 折线图是用折线将各个数据点标志连接起来的图表，用于展现数据的变化趋势。

Line.add() 方法签名
```python
add(name, x_axis, y_axis, is_symbol_show=True, is_smooth=False, is_stack=False,
    is_step=False, is_fill=False, **kwargs)
```
* name -> str  
    图例名称
* x_axis -> list  
    x 坐标轴数据
* y_axis -> list  
    y 坐标轴数据
* is_symbol_show -> bool  
    是否显示标记图形，默认为 True
* is_smooth -> bool  
    是否平滑曲线显示，默认为 False
* is_stack -> bool  
    数据堆叠，同个类目轴上系列配置相同的 stack 值可以堆叠放置。默认为 False
* is_step -> bool/str  
    是否是阶梯线图。可以设置为 True 显示成阶梯线图。默认为 False  
    也支持设置成'start', 'middle', 'end'分别配置在当前点，当前点与下个点的中间下个点拐弯。
* is_fill -> bool  
    是否填充曲线所绘制面积，默认为 False

```python
from pyecharts import Line

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 10, 100]
v2 = [55, 60, 16, 20, 15, 80]
line = Line("折线图示例")
line.add("商家A", attr, v1, mark_point=["average"])
line.add("商家B", attr, v2, is_smooth=True, mark_line=["max", "average"])
line.show_config()
line.render()
```
![line-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/line-0.gif)

* mark_point  -> list  
    标记点，有'min', 'max', 'average'可选
* mark_line  -> list  
    标记线，有'min', 'max', 'average'可选
* mark_point_symbol -> str  
    标记点图形，，默认为'pin'，有'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'可选
* mark_point_symbolsize -> int  
    标记点图形大小，默认为 50
* mark_point_textcolor -> str  
    标记点字体颜色，默认为'#fff'

标记点其他配置
```python
line = Line("折线图示例")
line.add("商家A", attr, v1, mark_point=["average", "max", "min"],
         mark_point_symbol='diamond', mark_point_textcolor='#40ff27')
line.add("商家B", attr, v2, mark_point=["average", "max", "min"],
         mark_point_symbol='arrow', mark_point_symbolsize=40)
line.show_config()
line.render()
```
![line-0-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/line-0-1.png)

```python
line = Line("折线图-数据堆叠示例")
line.add("商家A", attr, v1, is_stack=True, is_label_show=True)
line.add("商家B", attr, v2, is_stack=True, is_label_show=True)
line.show_config()
line.render()
```
![line-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/line-1.gif)

```python
line = Line("折线图-阶梯图示例")
line.add("商家A", attr, v1, is_step=True, is_label_show=True)
line.show_config()
line.render()
```
![line-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/line-2.png)

```python
line = Line("折线图-面积图示例")
line.add("商家A", attr, v1, is_fill=True, line_opacity=0.2, area_opacity=0.4, symbol=None)
line.add("商家B", attr, v2, is_fill=True, area_color='#000', area_opacity=0.3, is_smooth=True)
line.show_config()
line.render()
```
![line-3](https://github.com/chenjiandongx/pyecharts/blob/master/images/line-3.png)

* area_opacity -> float  
    填充区域透明度
* area_color -> str  
    填充区域颜色

**Tip：** 可配置 **lineStyle** 参数
**Tip：** 可以通过 label_color 来设置线条颜色，如 ['#eee', '#000']，所有的图表类型的图例颜色都可通过 label_color 来修改。


## Line3D（3D 折线图）

Line3D.add() 方法签名
```python
add(name, data, grid3D_opacity=1, **kwargs)
```
* name -> str  
    图例名称
* data -> [list],包含列表的列表  
    数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』
* grid3D_opacity -> int  
    3D 笛卡尔坐标系组的透明度（线的透明度），默认为 1，完全不透明。

画个弹簧
```python
from pyecharts import Line3D

import math
_data = []
for t in range(0, 25000):
    _t = t / 1000
    x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
    y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
    z = _t + 2.0 * math.sin(75 * _t)
    _data.append([x, y, z])
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
line3d = Line3D("3D 折线图示例", width=1200, height=600)
line3d.add("", _data, is_visualmap=True, visual_range_color=range_color, visual_range=[0, 30],
           grid3D_rotate_sensitivity=5)
line3d.render()
```
![line3D-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/line3D-0.gif)

旋转弹簧
```python
from pyecharts import Line3D

import math
_data = []
for t in range(0, 25000):
    _t = t / 1000
    x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
    y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
    z = _t + 2.0 * math.sin(75 * _t)
    _data.append([x, y, z])
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
line3d = Line3D("3D 折线图示例", width=1200, height=600)
line3d.add("", _data, is_visualmap=True, visual_range_color=range_color, visual_range=[0, 30],
           is_grid3D_rotate=True, grid3D_rotate_speed=180)
line3d.render()
```
![line3D-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/line3D-1.gif)

**Tip：** 关于 gird3D 部分的设置，请参照通用配置项中的介绍 [通用配置项](https://github.com/chenjiandongx/pyecharts/blob/master/README.md#通用配置项)  


## Liquid（水球图）
> 主要用来突出数据的百分比。

Liquid.add() 方法签名
```python
add(name, data, shape='circle', liquid_color=None, is_liquid_animation=True,
    is_liquid_outline_show=True, **kwargs)
```
* name -> str  
    图例名称
* data -> list  
    数据项
* shape -> str  
    水球外形，有'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'可选。默认'circle'
* liquid_color -> list  
    波浪颜色，默认的颜色列表为['#294D99', '#156ACF', '#1598ED', '#45BDFF']。
* is_liquid_animation -> bool  
    是否显示波浪动画，默认为 True。
* is_liquid_outline_show -> bool  
    是否显示边框，默认为 True。

```python
from pyecharts import Liquid

liquid = Liquid("水球图示例")
liquid.add("Liquid", [0.6])
liquid.show_config()
liquid.render()
```
![liquid-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/liquid-0.gif)

```python
from pyecharts import Liquid

liquid = Liquid("水球图示例")
liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
liquid.show_config()
liquid.render()
```
![liquid-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/liquid-1.gif)

```python
from pyecharts import Liquid

liquid = Liquid("水球图示例")
liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_animation=False, shape='diamond')
liquid.show_config()
liquid.render()
```
![liquid-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/liquid-2.png)

## Map（地图）
> 地图主要用于地理区域数据的可视化。

Map.add() 方法签名
```python
add(name, attr, value, is_roam=True, maptype='china', **kwargs)
```
* name -> str  
    图例名称
* attr -> list  
   属性名称
* value -> list  
   属性所对应的值
* is_roam -> bool/str
   是否开启鼠标缩放和平移漫游。默认为 True  
   如果只想要开启缩放或者平移，可以设置成'scale'或者'move'。设置成 True 为都开启
* maptype -> str  
   地图类型。
   支持 china、world、安徽、澳门、北京、重庆、福建、福建、甘肃、广东，广西、广州、海南、河北、黑龙江、河南、湖北、湖南、江苏、江西、吉林、辽宁、内蒙古、宁夏、青海、山东、上海、陕西、四川、台湾、天津、香港、新疆、西藏、云南、浙江

```python
from pyecharts import Map

value = [155, 10, 66, 78]
attr = ["福建", "山东", "北京", "上海"]
map = Map("全国地图示例", width=1200, height=600)
map.add("", attr, value, maptype='china')
map.show_config()
map.render()
```
![map-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/map-0.gif)

```python
from pyecharts import Map

value = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
attr = ["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]
map = Map("Map 结合 VisualMap 示例", width=1200, height=600)
map.add("", attr, value, maptype='china', is_visualmap=True, visual_text_color='#000')
map.show_config()
map.render()
```
![map-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/map-1.gif)

**Tip：** 请配合 [通用配置项](https://github.com/chenjiandongx/pyecharts/blob/master/README.md#通用配置项) 中的 Visualmap 使用

```python
from pyecharts import Map

value = [20, 190, 253, 77, 65]
attr = ['汕头市', '汕尾市', '揭阳市', '阳江市', '肇庆市']
map = Map("广东地图示例", width=1200, height=600)
map.add("", attr, value, maptype='广东', is_visualmap=True, visual_text_color='#000')
map.show_config()
map.render()
```
![map-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/map-2.gif)

### 关于自定义地图
因为地图涉及范围太广，项目不可能涵盖所有的地图，不过不用担心。Echarts 官方提供了自己定制地图的功能 [echart-map](http://echarts.baidu.com/download-map.html)，根据自己所需制定相应的地图，下载成 JS 文件格式。

打开安装目录下的 pyecharts/temple.py 文件，在 _temple 变量下对应的增加类似一行  
 ```<script type="text/javascript " src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/china.js"></script>```  
而对应的 Jupyter Notebook 下的就在 _mapindex 变量下新增类似一行  
```"北京": "beijing: '//oog4yfyu0.bkt.clouddn.com/beijing'"```   
然后就可以在项目中使用自定义的地图了！Js 的引入方式由自己决定，能被项目所找到就行！


## Parallel（平行坐标系）
> 平行坐标系是一种常用的可视化高维数据的图表。

Parallel.add() 方法签名
```python
add(name, data, **kwargs)
```
* name -> str
    图例名称
* data -> [list],包含列表的列表  
    数据项。数据中，每一行是一个『数据项』，每一列属于一个『维度』

Parallel.config() 方法签名
```python
config(schema=None, c_schema=None)
```
* schema  
    默认平行坐标系的坐标轴信息，如 ["dim_name1", "dim_name2", "dim_name3"]。
* c_schema  
    用户自定义平行坐标系的坐标轴信息。
    * dim -> int   
        维度索引
    * name > str  
        维度名称
    * type -> str   
        维度类型，有'value', 'category'可选  
        value：数值轴，适用于连续数据。  
        category： 类目轴，适用于离散的类目数据。
    * min -> int  
        坐标轴刻度最小值。
    * max -> int  
        坐标轴刻度最大值。
    * inverse - bool  
        是否是反向坐标轴。默认为 False
    * nameLocation -> str  
        坐标轴名称显示位置。有'start', 'middle', 'end'可选

```python
from pyecharts import Parallel

schema = ["data", "AQI", "PM2.5", "PM10", "CO", "NO2"]
data = [
        [1, 91, 45, 125, 0.82, 34],
        [2, 65, 27, 78, 0.86, 45,],
        [3, 83, 60, 84, 1.09, 73],
        [4, 109, 81, 121, 1.28, 68],
        [5, 106, 77, 114, 1.07, 55],
        [6, 109, 81, 121, 1.28, 68],
        [7, 106, 77, 114, 1.07, 55],
        [8, 89, 65, 78, 0.86, 51, 26],
        [9, 53, 33, 47, 0.64, 50, 17],
        [10, 80, 55, 80, 1.01, 75, 24],
        [11, 117, 81, 124, 1.03, 45]
]
parallel = Parallel("平行坐标系-默认指示器")
parallel.config(schema) 
parallel.add("parallel", data, is_random=True)
parallel.show_config()
parallel.render()
```
![parallel-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/parallel-0.png)

```python
from pyecharts import Parallel

c_schema = [
    {"dim": 0, "name": "data"},
    {"dim": 1, "name": "AQI"},
    {"dim": 2, "name": "PM2.5"},
    {"dim": 3, "name": "PM10"},
    {"dim": 4, "name": "CO"},
    {"dim": 5, "name": "NO2"},
    {"dim": 6, "name": "CO2"},
    {"dim": 7, "name": "等级",
    "type": "category", "data": ['优', '良', '轻度污染', '中度污染', '重度污染', '严重污染']}
]
data = [
    [1, 91, 45, 125, 0.82, 34, 23, "良"],
    [2, 65, 27, 78, 0.86, 45, 29, "良"],
    [3, 83, 60, 84, 1.09, 73, 27, "良"],
    [4, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
    [5, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
    [6, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
    [7, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
    [8, 89, 65, 78, 0.86, 51, 26, "良"],
    [9, 53, 33, 47, 0.64, 50, 17, "良"],
    [10, 80, 55, 80, 1.01, 75, 24, "良"],
    [11, 117, 81, 124, 1.03, 45, 24, "轻度污染"],
    [12, 99, 71, 142, 1.1, 62, 42, "良"],
    [13, 95, 69, 130, 1.28, 74, 50, "良"],
    [14, 116, 87, 131, 1.47, 84, 40, "轻度污染"]
]
parallel = Parallel("平行坐标系-用户自定义指示器")
parallel.config(c_schema=c_schema)
parallel.add("parallel", data)
parallel.show_config()
parallel.render()
```
![parallel-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/parallel-1.png)

**Tip：** 可配置 **lineStyle** 参数


## Pie（饼图）
> 饼图主要用于表现不同类目的数据在总和中的占比。每个的弧度表示数据数量的比例。

Pie.add() 方法签名
```python
add(name, attr, value, radius=None, center=None, rosetype=None, **kwargs)
```
* name -> str   
    图例名称
* attr -> list  
    属性名称
* value -> list  
    属性所对应的值
* radius -> list  
    饼图的半径，数组的第一项是内半径，第二项是外半径，默认为 [0, 75]  
    默认设置成百分比，相对于容器高宽中较小的一项的一半
* center -> list  
    饼图的中心（圆心）坐标，数组的第一项是横坐标，第二项是纵坐标，默认为 [50, 50]  
    默认设置成百分比，设置成百分比时第一项是相对于容器宽度，第二项是相对于容器高度
* rosetype -> str  
    是否展示成南丁格尔图，通过半径区分数据大小，有'radius'和'area'两种模式。默认为'radius'
    * radius：扇区圆心角展现数据的百分比，半径展现数据的大小
    * area：所有扇区圆心角相同，仅通过半径展现数据大小

```python
from pyecharts import Pie

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图示例")
pie.add("", attr, v1, is_label_show=True)
pie.show_config()
pie.render()
```
![pie-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/pie-0.gif)

```python
from pyecharts import Pie

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图-圆环图示例", title_pos='center')
pie.add("", attr, v1, radius=[40, 75], label_text_color=None, is_label_show=True,
        legend_orient='vertical', legend_pos='left')
pie.show_config()
pie.render()
```
![pie-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/pie-1.png)

```python
from pyecharts import Pie

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
v2 = [19, 21, 32, 20, 20, 33]
pie = Pie("饼图-玫瑰图示例", title_pos='center', width=900)
pie.add("商品A", attr, v1, center=[25, 50], is_random=True, radius=[30, 75], rosetype='radius')
pie.add("商品B", attr, v2, center=[75, 50], is_random=True, radius=[30, 75], rosetype='area',
        is_legend_show=False, is_label_show=True)
pie.show_config() 
pie.render()
```
![pie-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/pie-2.png)


## Polar（极坐标系）
> 可以用于散点图和折线图。

Polar.add() 方法签名
```python
add(name, data, angle_data=None, radius_data=None, type='line', symbol_size=4, start_angle=90,
    rotate_step=0, boundary_gap=True, clockwise=True, **kwargs)
```
* name -> str  
    图例名称
* data -> [list],包含列表的列表  
    数据项 [极径，极角 [数据值]]
* angle_data -> list  
    角度类目数据
* radius_data -> list  
    半径类目数据
* type -> str  
    图例类型，有'line', 'scatter', 'effectScatter', 'barAngle', 'barRadius'可选。默认为 'line'
* symbol_size -> int  
    标记图形大小，默认为 4。
* start_angle -> int  
    起始刻度的角度，默认为 90 度，即圆心的正上方。0 度为圆心的正右方
* rotate_step -> int  
    刻度标签旋转的角度，在类目轴的类目标签显示不下的时候可以通过旋转防止标签之间重叠  
    旋转的角度从 -90 度到 90 度。默认为 0
* boundary_gap -> bool  
    坐标轴两边留白策略  
    默认为 True，这时候刻度只是作为分隔线，标签和数据点都会在两个刻度之间的带(band)中间
* clockwise -> bool  
    刻度增长是否按顺时针，默认 True
* is_stack -> bool  
    数据堆叠，同个类目轴上系列配置相同的 stack 值可以堆叠放置
* axis_range -> list  
    坐标轴刻度范围。默认值为 [None, None]。
* is_angleaxis_show -> bool  
    是否显示极坐标系的角度轴，默认为 True
* is_radiusaxis_show -> bool  
    是否显示极坐标系的径向轴，默认为 True

```python
from pyecharts import Polar

import random
data = [(i, random.randint(1, 100)) for i in range(101)]
polar = Polar("极坐标系-散点图示例")
polar.add("", data, boundary_gap=False, type='scatter', is_splitline_show=False,
          area_color=None, is_axisline_show=True)
polar.show_config()
polar.render()
```
![polar-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/polar-0.png)

* is_splitline_show  -> bool  
    是否显示分割线，默认为 True
* is_axisline_show -> bool  
    是否显示坐标轴线，默认为 True
* area_opacity -> float  
    填充区域透明度
* area_color -> str  
    填充区域颜色

**Tip：** 可配置 **lineStyle** 参数

```python
from pyecharts import Polar

import random
data_1 = [(10, random.randint(1, 100)) for i in range(300)]
data_2 = [(11, random.randint(1, 100)) for i in range(300)]
polar = Polar("极坐标系-散点图示例", width=1200, height=600)
polar.add("", data_1, type='scatter')
polar.add("", data_2, type='scatter')
polar.show_config()
polar.render()
```
![polar-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/polar-1.png)

```python
from pyecharts import Polar

import random
data = [(i, random.randint(1, 100)) for i in range(10)]
polar = Polar("极坐标系-动态散点图示例", width=1200, height=600)
polar.add("", data, type='effectScatter', effect_scale=10, effect_period=5)
polar.show_config()
polar.render()
```
![polar-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/polar-2.gif)

```python
from pyecharts import Polar

radius = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
polar = Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
polar.add("A", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, type='barRadius', is_stack=True)
polar.add("B", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, type='barRadius', is_stack=True)
polar.add("C", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, type='barRadius', is_stack=True)
polar.show_config()
polar.render()
```
![polar-3](https://github.com/chenjiandongx/pyecharts/blob/master/images/polar-3.gif)

```python
from pyecharts import Polar

radius = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
polar = Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
polar.add("", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, type='barAngle', is_stack=True)
polar.add("", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, type='barAngle', is_stack=True)
polar.add("", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, type='barAngle', is_stack=True)
polar.show_config()
polar.render()
```
![polar-4](https://github.com/chenjiandongx/pyecharts/blob/master/images/polar-4.png)


## Radar（雷达图）
> 雷达图主要用于表现多变量的数据。

Radar.add() 方法签名
```python
add(name, value, item_color=None, **kwargs)
```
* name -> list  
    图例名称
* value -> [list],包含列表的列表 
    数据项。数据中，每一行是一个『数据项』，每一列属于一个『维度』
* item_color -> str  
    指定单图例颜色

Radar.config() 方法签名
```python
config(schema=None, c_schema=None, shape="", rader_text_color="#000", **kwargs):
```
* schema -> list  
    默认雷达图的指示器，用来指定雷达图中的多个维度，会对数据处理成 {name:xx, value:xx} 的字典
* c_schema -> dict  
    用户自定义雷达图的指示器，用来指定雷达图中的多个维度
    * name: 指示器名称
    * min: 指示器最小值
    * max: 指示器最大值
* shape -> str  
    雷达图绘制类型，有'polygon'（多边形）和'circle'可选
* rader_text_color -> str  
    雷达图数据项字体颜色，默认为'#000'

```python
from pyecharts import Radar

schema = [ 
    ("销售", 6500), ("管理", 16000), ("信息技术", 30000), ("客服", 38000), ("研发", 52000), ("市场", 25000)]
v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
radar = Radar()
radar.config(schema)
radar.add("预算分配", v1, is_splitline=True, is_axisline_show=True)
radar.add("实际开销", v2, label_color=["#4e79a7"], is_area_show=False, legend_selectedmode='signle')
radar.show_config()
radar.render()
```
![radar-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/radar-0.gif)

* is_area_show -> bool  
    是否显示填充区域
* area_opacity -> float  
    填充区域透明度
* area_color -> str  
    填充区域颜色
* is_splitline_show  -> bool  
    是否显示分割线，默认为 True
* is_axisline_show -> bool  
    是否显示坐标轴线，默认为 True

**Tip：** 可配置 **lineStyle** 参数

```python
value_bj = [
    [55, 9, 56, 0.46, 18, 6, 1], [25, 11, 21, 0.65, 34, 9, 2],
    [56, 7, 63, 0.3, 14, 5, 3], [33, 7, 29, 0.33, 16, 6, 4],
    [42, 24, 44, 0.76, 40, 16, 5], [82, 58, 90, 1.77, 68, 33, 6],
    [74, 49, 77, 1.46, 48, 27, 7], [78, 55, 80, 1.29, 59, 29, 8],
    [267, 216, 280, 4.8, 108, 64, 9], [185, 127, 216, 2.52, 61, 27, 10],
    [39, 19, 38, 0.57, 31, 15, 11], [41, 11, 40, 0.43, 21, 7, 12],
    [64, 38, 74, 1.04, 46, 22, 13], [108, 79, 120, 1.7, 75, 41, 14],
    [108, 63, 116, 1.48, 44, 26, 15], [33, 6, 29, 0.34, 13, 5, 16],
    [94, 66, 110, 1.54, 62, 31, 17], [186, 142, 192, 3.88, 93, 79, 18],
    [57, 31, 54, 0.96, 32, 14, 19], [22, 8, 17, 0.48, 23, 10, 20],
    [39, 15, 36, 0.61, 29, 13, 21], [94, 69, 114, 2.08, 73, 39, 22],
    [99, 73, 110, 2.43, 76, 48, 23], [31, 12, 30, 0.5, 32, 16, 24],
    [42, 27, 43, 1, 53, 22, 25], [154, 117, 157, 3.05, 92, 58, 26],
    [234, 185, 230, 4.09, 123, 69, 27],[160, 120, 186, 2.77, 91, 50, 28],
    [134, 96, 165, 2.76, 83, 41, 29], [52, 24, 60, 1.03, 50, 21, 30],
]
value_sh = [
    [91, 45, 125, 0.82, 34, 23, 1], [65, 27, 78, 0.86, 45, 29, 2],
    [83, 60, 84, 1.09, 73, 27, 3], [109, 81, 121, 1.28, 68, 51, 4],
    [106, 77, 114, 1.07, 55, 51, 5], [109, 81, 121, 1.28, 68, 51, 6],
    [106, 77, 114, 1.07, 55, 51, 7], [89, 65, 78, 0.86, 51, 26, 8],
    [53, 33, 47, 0.64, 50, 17, 9], [80, 55, 80, 1.01, 75, 24, 10],
    [117, 81, 124, 1.03, 45, 24, 11], [99, 71, 142, 1.1, 62, 42, 12],
    [95, 69, 130, 1.28, 74, 50, 13], [116, 87, 131, 1.47, 84, 40, 14],
    [108, 80, 121, 1.3, 85, 37, 15], [134, 83, 167, 1.16, 57, 43, 16],
    [79, 43, 107, 1.05, 59, 37, 17], [71, 46, 89, 0.86, 64, 25, 18],
    [97, 71, 113, 1.17, 88, 31, 19], [84, 57, 91, 0.85, 55, 31, 20],
    [87, 63, 101, 0.9, 56, 41, 21], [104, 77, 119, 1.09, 73, 48, 22],
    [87, 62, 100, 1, 72, 28, 23], [168, 128, 172, 1.49, 97, 56, 24],
    [65, 45, 51, 0.74, 39, 17, 25], [39, 24, 38, 0.61, 47, 17, 26],
    [39, 24, 39, 0.59, 50, 19, 27], [93, 68, 96, 1.05, 79, 29, 28],
    [188, 143, 197, 1.66, 99, 51, 29], [174, 131, 174, 1.55, 108, 50, 30],
]
c_schema= [{"name": "AQI", "max": 300, "min": 5},
           {"name": "PM2.5", "max": 250, "min": 20},
           {"name": "PM10", "max": 300, "min": 5},
           {"name": "CO", "max": 5},
           {"name": "NO2", "max": 200},
           {"name": "SO2", "max": 100}]
radar = Radar()
radar.config(c_schema=c_schema, shape='circle')
radar.add("北京", value_bj, item_color="#f9713c", symbol=None)
radar.add("上海", value_sh, item_color="#b3e4a1", symbol=None, legend_selectedmode='signle')
radar.show_config()
radar.render()
```
![radar-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/radar-1.gif)

**Tip：** symblo=None 可隐藏标记图形（小圆圈）

图例多例模式。
```python
radar = Radar()
radar.config(c_schema=c_schema, shape='circle')
radar.add("北京", value_bj, item_color="#f9713c", symbol=None)
radar.add("上海", value_sh, item_color="#b3e4a1", symbol=None)
radar.show_config()
radar.render()
```
![radar-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/radar-2.gif)


## Scatter（散点图）
> 直角坐标系上的散点图可以用来展现数据的 x，y 之间的关系，如果数据项有多个维度，可以用颜色来表现，利用 geo 组件。

Scatter.add() 方法签名
```python
add(name, x_value, y_value, symbol_size=10, **kwargs)
```
* name -> str  
    图例名称
* x_axis -> list  
    x 坐标轴数据
* y_axis -> list  
    y 坐标轴数据
* symbol_size -> int  
    标记图形大小，默认为 10

```python
from pyecharts import Scatter

v1 = [10, 20, 30, 40, 50, 60]
v2 = [10, 20, 30, 40, 50, 60]
scatter = Scatter("散点图示例")
scatter.add("A", v1, v2)
scatter.add("B", v1[::-1], v2)
scatter.show_config()
scatter.render()
```
![scatter-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/scatter-0.png)

利用 Visualmap 组件，通过颜色映射数值。
```python
scatter = Scatter("散点图示例")
scatter.add("A", v1, v2)
scatter.add("B", v1[::-1], v2, is_visualmap=True)
scatter.show_config()
scatter.render()
```
![scatter-0-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/scatter-0-1.gif)

利用 Visualmap 组件，通过图形点大小映射数值。
```python
scatter = Scatter("散点图示例")
scatter.add("A", v1, v2)
scatter.add("B", v1[::-1], v2, is_visualmap=True, visual_type='size', visual_range_size=[20, 80])
scatter.show_config()
scatter.render()
```
![scatter-0-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/scatter-0-2.gif)

**Tip：** 请配合 [通用配置项](https://github.com/chenjiandongx/pyecharts/blob/master/README.md#通用配置项) 中的 Visualmap 使用

Scatter 还内置了画画方法
```python
draw(path, color=None)
''' 
将图片上的像素点转换为数组，如 color 为（255,255,255）时只保留非白色像素点的坐标信息  
返回两个 k_lst, v_lst 两个列表刚好作为散点图的数据项
'''
```
* path -> str  
    转换图片的地址
* color -> str  
    所要排除的颜色

首先你需要准备一张图片，如

![pyecharts-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/pyecharts-0.png)

```python
from pyecharts import Scatter

scatter = Scatter("散点图示例")
v1, v2 = scatter.draw("../images/pyecharts-0.png")
scatter.add("pyecharts", v1, v2, is_random=True)
scatter.show_config()
scatter.render()
```
![pyecharts-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/pyecharts-1.png)


## Scatter3D（3D 散点图）

Scatter3D.add() 方法签名
```python
add(name, data, grid3D_opacity=1, **kwargs)
```
* name -> str  
    图例名称
* data -> [list],包含列表的列表  
    数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』
* grid3D_opacity -> int  
    3D 笛卡尔坐标系组的透明度（点的透明度），默认为 1，完全不透明。

```python
from pyecharts import Scatter3D

import random
data = [[random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)] for _ in range(80)]
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
scatter3D = Scatter3D("3D 散点图示例", width=1200, height=600)
scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
scatter3D.render()
```
![scatter3D-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/scatter3D-0.gif)

**Tip：** 关于 gird3D 部分的设置，请参照通用配置项中的介绍 [通用配置项](https://github.com/chenjiandongx/pyecharts/blob/master/README.md#通用配置项)  


## WordCloud（词云图）
WordCloud.add() 方法签名
```python
add(name, attr, value, shape="circle", word_gap=20, word_size_range=None, rotate_step=45)
```
* name -> str  
    图例名称
* attr -> list  
   属性名称
* value -> list  
   属性所对应的值
* shape -> list  
   词云图轮廓，有'circle', 'cardioid', 'diamond', 'triangle-forward', 'triangle', 'pentagon', 'star'可选
* word_gap -> int  
   单词间隔，默认为 20。
* word_size_range -> list  
   单词字体大小范围，默认为 [12, 60]。
* rotate_step -> int  
   旋转单词角度，默认为 45

```python
from pyecharts import WordCloud

name = ['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications',
        'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp',
        'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham',
        'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
value = [10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555,
         550, 462, 366, 360, 282, 273, 265]
wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[20, 100])
wordcloud.show_config()
wordcloud.render()
```
![wordcloud-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/wordcloud-0.png)

```python
wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[30, 100], shape='diamond')
wordcloud.show_config()
wordcloud.render()
```
![wordcloud-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/wordcloud-1.png)

**Tip：** 当且仅当 shape 为默认的'circle'时 rotate_step 参数才生效


# 用户自定义

## 结合不同类型图表画在一张图上
用户可以自定义结合 Line/Bar/Kline, Scatter/EffectScatter 图表，将不同类型图表画在一张图上。利用第一个图表为基础，往后的数据都将会画在第一个图表上。   
需使用 ```get_series()``` 和 ```custom()``` 方法  

```python
get_series()
""" 获取图表的 series 数据 """
```
```python
custom(series)
''' 追加自定义图表类型 '''
```
* series -> dict  
    追加图表类型的 series 数据

先用 ```get_series()``` 获取数据，再使用 ```custom()``` 将图表结合在一起  

Line + Bar
```python
from pyecharts import Bar, Line

attr = ['A', 'B', 'C', 'D', 'E', 'F']
v1 = [10, 20, 30, 40, 50, 60]
v2 = [15, 25, 35, 45, 55, 65]
v3 = [38, 28, 58, 48, 78, 68]
bar = Bar("Line - Bar 示例")
bar.add("bar", attr, v1)
line = Line()
line.add("line", v2, v3)
bar.custom(line.get_series())
bar.show_config()
bar.render()
```
![custom-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/custom-0.gif)

具体流程如下：
1. 初始化图表，正常添加配置项。
2. 调用第一个图表的 custom(type.get_series()) 方法逐个添加。
3. 调用第一个图表的 render() 方法。

**Tip：** ```bar.custom(line.get_series())``` 这个一定要注意，利用第一个图表为基础。切记不要写成 ```bar.custom(bar.get_series())``` 不然会进入无限地自我调用的状态中，无限递归，最后可能导致死机。

Scatter + EffectScatter
```python
from pyecharts import Scatter, EffectScatter

v1 = [10, 20, 30, 40, 50, 60]
v2 = [30, 30, 30, 30, 30, 30]
v3 = [50, 50, 50, 50, 50, 50]
v4 = [10, 10, 10, 10, 10, 10]
es = EffectScatter("Scatter - EffectScatter 示例")
es.add("es", v1, v2)
scatter = Scatter()
scatter.add("scatter", v1, v3)
es.custom(scatter.get_series())
es_1 = EffectScatter()
es_1.add("es_1", v1, v4, symbol='pin', effect_scale=5)
es.custom(es_1.get_series())
es.show_config()
es.render()
```
![custom-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/custom-1.gif)

Kline + Line
```python
import random
from pyecharts import Line, Kline

v1 = [[2320.26, 2320.26, 2287.3, 2362.94], [2300, 2291.3, 2288.26, 2308.38],
      [2295.35, 2346.5, 2295.35, 2345.92], [2347.22, 2358.98, 2337.35, 2363.8],
      [2360.75, 2382.48, 2347.89, 2383.76], [2383.43, 2385.42, 2371.23, 2391.82],
      [2377.41, 2419.02, 2369.57, 2421.15], [2425.92, 2428.15, 2417.58, 2440.38],
      [2411, 2433.13, 2403.3, 2437.42], [2432.68, 2334.48, 2427.7, 2441.73],
      [2430.69, 2418.53, 2394.22, 2433.89], [2416.62, 2432.4, 2414.4, 2443.03],
      [2441.91, 2421.56, 2418.43, 2444.8], [2420.26, 2382.91, 2373.53, 2427.07],
      [2383.49, 2397.18, 2370.61, 2397.94], [2378.82, 2325.95, 2309.17, 2378.82],
      [2322.94, 2314.16, 2308.76, 2330.88], [2320.62, 2325.82, 2315.01, 2338.78],
      [2313.74, 2293.34, 2289.89, 2340.71], [2297.77, 2313.22, 2292.03, 2324.63],
      [2322.32, 2365.59, 2308.92, 2366.16], [2364.54, 2359.51, 2330.86, 2369.65],
      [2332.08, 2273.4, 2259.25, 2333.54], [2274.81, 2326.31, 2270.1, 2328.14],
      [2333.61, 2347.18, 2321.6, 2351.44], [2340.44, 2324.29, 2304.27, 2352.02],
      [2326.42, 2318.61, 2314.59, 2333.67], [2314.68, 2310.59, 2296.58, 2320.96],
      [2309.16, 2286.6, 2264.83, 2333.29], [2282.17, 2263.97, 2253.25, 2286.33],
      [2255.77, 2270.28, 2253.31, 2276.22]]
attr = ["2017/7/{}".format(i + 1) for i in range(31)]
kline = Kline("Kline - Line 示例")
kline.add("日K", attr, v1)
line_1 = Line()
line_1.add("line-1", attr, [random.randint(2400, 2500) for _ in range(31)])
line_2 = Line()
line_2.add("line-2", attr, [random.randint(2400, 2500) for _ in range(31)])
kline.custom(line_1.get_series())
kline.custom(line_2.get_series())
kline.show_config()
kline.render()
```
![custom-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/custom-2.png)

## 结合不同类型图表画在多张图上，并行显示图表
用户可以自定义结合 Line/Bar/Kline/Scatter/EffectScatter/Pie/HeatMap 图表，将不同类型图表画在多张图上。同样也是要以某一张图表为基础。     
需使用 ```get_series()``` 和 ```grid()``` 方法  

```python
get_series()
""" 获取图表的 series 数据 """
```
```python
grid(series，grid_width, grid_height, grid_top, grid_bottom, grid_left, grid_right)
''' 并行显示图表 '''
```
* series -> dict  
    追加图表类型的 series 数据
* grid_width -> str/int  
    grid 组件的宽度。默认自适应。
* grid_height -> str/int  
    grid 组件的高度。默认自适应。
* grid_top -> str/int  
    grid 组件离容器顶部的距离。默认为 None, 有'top', 'center', 'middle'可选，也可以为百分数或者整数
* grid_bottom -> str/int  
    grid 组件离容器底部的距离。默认为 None, 有'top', 'center', 'middle'可选，也可以为百分数或者整数
* grid_left -> str/int  
    grid 组件离容器左侧的距离。默认为 None, 有'left', 'center', 'right'可选，也可以为百分数或者整数
* grid_right -> str/int  
    grid 组件离容器右侧的距离。默认为 None, 有'left', 'center', 'right'可选，也可以为百分数或者整数

先用 ```get_series()``` 获取数据，再使用 ```grid()``` 将图表结合在一起  

上下类型，Bar + Line  
```python
from pyecharts import Bar, Line

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图示例", height=720, is_grid=True)
bar.add("商家A", attr, v1, is_stack=True, grid_bottom="60%")
bar.add("商家B", attr, v2, is_stack=True, grid_bottom="60%")
line = Line("折线图示例", title_top="50%")
attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10], mark_point=["max", "min"], mark_line=["average"])
line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0], mark_point=["max", "min"],
         mark_line=["average"], legend_top="50%")
bar.grid(line.get_series(), grid_top="60%")
bar.show_config()
bar.render()
```
![grid-0](https://github.com/chenjiandongx/pyecharts/blob/master/images/grid-0.gif)

**再次Tip：** ```bar.grid(line.get_series(), grid_top="60%")``` 不要写成 ```bar.grid(bar.get_series())``` 不然会陷入无限递归中  

具体流程如下：
1. 在第一个图表初始化的时候制定 is_grid=True，说明要使用 grid 组件。
2. 第一个表格的 add() 方法中要制定 grid_* 参数，必须制定，因为 grid_* 默认值都是为 None，不会添加到配置项中。最少指定一个。
3. 初始化其他类型（同类型也可以），不用指定 grid_* 参数。
4. 调用第一个图表的 grid() 方法逐个添加，并且设置 grid_* 参数，必须指定，至少一个。
5. 调用第一个图表的 render() 方法。

左右类型，Scatter + EffectScatter  
```python
from pyecharts import Scatter, EffectScatter

v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
scatter = Scatter(width=1200, is_grid=True)
scatter.add("散点图示例", v1, v2, grid_left="60%", legend_pos="70%")
es = EffectScatter()
es.add("动态散点图示例", [11, 11, 15, 13, 12, 13, 10], [1, -2, 2, 5, 3, 2, 0],
       effect_scale=6, legend_pos="20%")
scatter.grid(es.get_series(), grid_right="60%")
scatter.show_config()
scatter.render()
```
![grid-1](https://github.com/chenjiandongx/pyecharts/blob/master/images/grid-1.gif)

上下左右类型，Bar + Line + Scatter + EffectScatter  
```python
from pyecharts import Bar, Line, Scatter, EffectScatter  

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图示例", height=720, width=1200, title_pos="65%", is_grid=True)
bar.add("商家A", attr, v1, is_stack=True, grid_bottom="60%", grid_left="60%")
bar.add("商家B", attr, v2, is_stack=True, grid_bottom="60%", grid_left="60%", legend_pos="80%")
line = Line("折线图示例")
attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10], mark_point=["max", "min"], mark_line=["average"])
line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0], mark_point=["max", "min"],
         mark_line=["average"], legend_pos="20%")
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
scatter = Scatter("散点图示例", title_top="50%", title_pos="65%")
scatter.add("scatter", v1, v2, legend_top="50%", legend_pos="80%")
es = EffectScatter("动态散点图示例", title_top="50%")
es.add("es", [11, 11, 15, 13, 12, 13, 10], [1, -2, 2, 5, 3, 2, 0], effect_scale=6,
       legend_top="50%", legend_pos="20%")
bar.grid(line.get_series(), grid_bottom="60%", grid_right="60%")
bar.grid(scatter.get_series(), grid_top="60%", grid_left="60%")
bar.grid(es.get_series(), grid_top="60%", grid_right="60%")
bar.show_config()
bar.render()
```
![grid-2](https://github.com/chenjiandongx/pyecharts/blob/master/images/grid-2.gif)

Line +  Pie  
```python
from pyecharts import Line, Pie

line = Line("折线图示例", width=1200, is_grid=True)
attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10], mark_point=["max", "min"],
         mark_line=["average"], grid_right="65%")
line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0], mark_point=["max", "min"],
         mark_line=["average"], legend_pos="20%")
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图示例", title_pos="45%")
pie.add("", attr, v1, radius=[30, 55], legend_pos="65%", legend_orient='vertical')
line.grid(pie.get_series(), grid_left="60%")
line.show_config()
line.render()
```
![grid-3](https://github.com/chenjiandongx/pyecharts/blob/master/images/grid-3.png)

**Tip：** 可以通过设置 center 参数改变 Pie 图的位置，如 [v1, v2]， 要求 v1 > v2。

Line + Kline
```python
from pyecharts import Line, Kline

line = Line("折线图示例", width=1200, is_grid=True)
attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10], mark_point=["max", "min"],
         mark_line=["average"], grid_right="60%")
line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0], mark_point=["max", "min"],
         mark_line=["average"], legend_pos="20%", grid_right="60%")
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
value = [20, 40, 60, 80, 100, 120]
v1 = [[2320.26, 2320.26, 2287.3, 2362.94], [2300, 2291.3, 2288.26, 2308.38],
      [2295.35, 2346.5, 2295.35, 2345.92], [2347.22, 2358.98, 2337.35, 2363.8],
      [2360.75, 2382.48, 2347.89, 2383.76], [2383.43, 2385.42, 2371.23, 2391.82],
      [2377.41, 2419.02, 2369.57, 2421.15], [2425.92, 2428.15, 2417.58, 2440.38],
      [2411, 2433.13, 2403.3, 2437.42], [2432.68, 2334.48, 2427.7, 2441.73],
      [2430.69, 2418.53, 2394.22, 2433.89], [2416.62, 2432.4, 2414.4, 2443.03],
      [2441.91, 2421.56, 2418.43, 2444.8], [2420.26, 2382.91, 2373.53, 2427.07],
      [2383.49, 2397.18, 2370.61, 2397.94], [2378.82, 2325.95, 2309.17, 2378.82],
      [2322.94, 2314.16, 2308.76, 2330.88], [2320.62, 2325.82, 2315.01, 2338.78],
      [2313.74, 2293.34, 2289.89, 2340.71], [2297.77, 2313.22, 2292.03, 2324.63],
      [2322.32, 2365.59, 2308.92, 2366.16], [2364.54, 2359.51, 2330.86, 2369.65],
      [2332.08, 2273.4, 2259.25, 2333.54], [2274.81, 2326.31, 2270.1, 2328.14],
      [2333.61, 2347.18, 2321.6, 2351.44], [2340.44, 2324.29, 2304.27, 2352.02],
      [2326.42, 2318.61, 2314.59, 2333.67], [2314.68, 2310.59, 2296.58, 2320.96],
      [2309.16, 2286.6, 2264.83, 2333.29], [2282.17, 2263.97, 2253.25, 2286.33],
      [2255.77, 2270.28, 2253.31, 2276.22]]
kline = Kline("K 线图示例", title_pos="60%")
kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1, legend_pos="80%")
line.grid(kline.get_series(), grid_left="55%")
line.show_config()
line.render()
```
![grid-4](https://github.com/chenjiandongx/pyecharts/blob/master/images/grid-4.png)

HeatMap + Bar  
```python
import random

from pyecharts import HeatMap, Bar  

x_axis = ["12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
          "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"]
y_aixs = ["Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"]
data = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
heatmap = HeatMap("热力图示例", height=700, is_grid=True)
heatmap.add("热力图直角坐标系", x_axis, y_aixs, data, is_visualmap=True, visual_top="45%",
            visual_text_color="#000", visual_orient='horizontal', grid_bottom="60%")
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图示例", title_top="52%")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True, legend_top="50%")
heatmap.grid(bar.get_series(), grid_top="60%")
heatmap.show_config()
heatmap.render()
```
![grid-5](https://github.com/chenjiandongx/pyecharts/blob/master/images/grid-5.gif)  
Bar 会受 HeatMap 影响，很有趣。

# 更多示例

* 更多示例请参考 [example.md](https://github.com/chenjiandongx/pyecharts/blob/master/example.md)
* 欢迎大家补充示例

# 关于项目

* 欢迎大家使用 pyecharts
* 有什么建议或者想法可以开个 issue 讨论，有什么小错误的也可以直接提交 PR。
* 如有想单独讨论的话可以使用邮箱 -> chenjiandongx@qq.com
* 关注 [changelog.md](https://github.com/chenjiandongx/pyecharts/blob/master/changelog.md)