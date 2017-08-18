# Version Log

## 项目期待

* 最大的期待就是大家提需求的时候悠着点...


## 版本信息

* version 0.1.9.6（下一版本）
    * Page 类现在也支持在 jupyter-notebook 中显示了，直接调用 Page() 实例即可。
    * 更改通用配置项中的 label 的参数 formatter 为 label_formatter
    * 更改 clockwise 参数为 is_clockwise
    * 更改 Graph 图中的 repulsion, gravity, edge_length, layout 参数为 graph_repulsion, graph_gravity, graph_edge_length, graph_layout，并新增 graph_edge_symbol, graph_edge_symbolsize 参数
    * 通用配置项中新增 tooltip 模块
    * Overlap 中新增 xaxis_index, is_add_xaxis, yaxis_index, is_add_yaxis 参数，现支持多 Y 轴或多 X 轴

* version 0.1.9.5（当前版本）
    * jupyter notebook 现在也为离线模式，从本地加载项目所需 js 文件。至此 pyecharts 彻底实现本地化运行。速度更快，不再受网速影响。
    * 删除冗余 js 文件，压缩项目体积。
    * 新增 Timeline 功能，支持轮播多张图表
    * 修改自定义模块的接口，现自定义模块有以下 4 个类，具体用法参见文档
        * Grid 类：并行显示多张图
        * Overlap 类：结合不同类型图表叠加画在同张图上
        * Page 类：同一网页按顺序展示多图
        * Timeline 类：提供时间线轮播多张图
    * 为 3D 图新增参数用于配置坐标轴选项（参见通用配置项中的 axis3D）
    * 废弃 xAxis，yAxis 中的 `interval`, `xy_font_size`, `namegap` 参数。新增以下参数
        * xaxis_interval（取代 `interval` 参数）
        * yaxis_interval（取代 `interval` 参数）
        * xaxis_name_gap（取代 `namegap` 参数）
        * yaxis_name_gap（取代 `namegap` 参数）
        * xaxis_name_size（取代 `xy_font_size` 参数）
        * yaxis_name_size（取代 `xy_font_size` 参数）
        * xaxis_margin（x 轴与标签的距离）
        * yaxis_margin（y 轴与标签的距离）
        * is_xaxislabel_align（x 轴标签是否与刻度对齐）
        * is_yaxislabel_align（y 轴标签是否与刻度对齐）

* version 0.1.9.4
    * 删除 Image 依赖模块，改为 pillow 模块
    * 新增 Page 类，现能同时在一个 html 页面内按顺序展示多个图形。（参见用户自定义）

* version 0.1.9.3
    * 新增 `xaxis_type`, `yaxis_type` 参数，可通过设置该参数指定直角坐标系数轴类型。（参见 Line，Scattre 图）
    * 废弃 `npcast()`, `pdcast()` 方法，新版本已经在内部封装了处理逻辑，直接在 `add()` 中传入 `numpy`, `pandas` 的 `index`，`values` 属性即可
    * 集成 Flask + Django

* version 0.1.9.2
    * 新增 `xaxis_rotate`, `yaxis_rotate` 参数，可通过设置该参数解决强制显示所有坐标轴标签时因过于密集重叠的问题。参见（Bar 图）
    * 新增 `xaxis_min`, `xaxis_max`. `yaxis_min`, `yaxis_max` 参数，可设置坐标轴上的最大最小值，针对数值轴有效。
    * 解决 3D 图形不能在 jupyter notebook 上正常显示的问题。
    * `render()` 方法现在为离线模式，实现本地生成 .html 文件，加载速度更快。
    * 废弃 `render_notebook()` 方法，现可直接调用图形实例显示在 jupyter notebook 上。

* version 0.1.9.1
    * 加入 Travis-CI 自动化测试。感谢 [@chfw](https://github.com/chfw) 提供的代码。  
    * legend 增加 `legend_selectedmode` 参数，图例可以设置为单例或者多例。（参见 Radar 图）
    * visualmap 组件增加 `visual_map` 和 `visual_range_size` 参数。现在支持映射到颜色和图形大小两种方式。（参见 Scatter 图）

* version 0.1.9
    * 解决在 macos 下安装出错的问题。感谢 [@chfw](https://github.com/chfw) 提供的解决方案。
    * datazoom 中增加了将组件效果显示在 y 坐标轴中的功能。（参见 KLine 图）
    * 新增对 Pandas 和 Numpy 数据的简单处理。解决直接传入 Pandas 和 Numpy 数据类型出错的问题。（参见开始使用）
    * 新增 Bar3D, Line3D, Scatter3D 三种 3D 立体图表。

* version 0.1.8  
    * 新增在 Jupyter Notebook 中展示图表功能。感谢 [@ygw365](https://github.com/ygw365) 提供这部分的代码模板 和 [@muxuezi](https://github.com/muxuezi) 协助对代码进行改进!
    * 新增对自定义地图的使用说明  

* version 0.1.7  
    * 增加并行显示图表功能

* version 0.1.6  
    * 新增了热力图

* version 0.1.5  
    * 新增了 K 线图

* version 0.1.4  
    * 第一个稳定版本
    