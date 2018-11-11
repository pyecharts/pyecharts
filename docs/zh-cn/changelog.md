# 版本日志

* ### version 0.6.0（dev）

    #### Updated
    * 将 pyecharts-javascripthon 合并入主仓库，并对该部分代码进行了重构。导入路径由 `from pyecharts_javascripthon import *` 转变为 `from pyecharts.javascripthon import *`
    * Grid / Overlap / Timeline 等更名为复合图表，并移入 `pyecharts.charts.composite` 包。
    
    ### Removed
    * 类 `Style` 废弃，推荐使用原生 `dict` 写法。
    * [issue#762](https://github.com/pyecharts/pyecharts/issues/762) 移除 `is_fill` 配置项，使用 `area_opacity` 指定区域透明度。

* ### version 0.5.11 - 2018.9.9（current）
    
    #### Added
    * [issue#731](https://github.com/pyecharts/pyecharts/issues/731) 新增 `mark_point_raw`, `mark_line_raw` 配置项用于个性化展示标记。
    
    #### Fixed
    * [issue#738](https://github.com/pyecharts/pyecharts/issues/738) 支持设置 Grid, Overlay 和 Timeline 某选项为空 (null)

    #### Removed
    * 移除 pillow 作为默认依赖，需要用到 Scatter.draw 方法的开发者请先自行安装 pillow。
    

* ### version 0.5.10 - 2018.9.4

    #### Added
    * [issue#699](https://github.com/pyecharts/pyecharts/issues/699) 为漏斗图新增 `funnel_sort` 和 `funnel_gap` 分别用于控制漏斗图的排序方式和数据图形间隔。
    * [issue#703](https://github.com/pyecharts/pyecharts/issues/703) 支持设置 Echarts 某选项为空 (null)
    * [issue#720](https://github.com/pyecharts/pyecharts/issues/720) 新增 3D 曲面图图形种类。

    #### Fixed
    * [issue#715](https://github.com/pyecharts/pyecharts/issues/715) 修复 online() 方法不生效的 bug

    #### Updated
    * [issue#702](https://github.com/pyecharts/pyecharts/issues/702) Toobox 选项标签文本更改为更通用的英语。

    #### Removed
    * 停止对 Python3.4 版本的支持和维护。


* ### version 0.5.9 - 2018.8.26

    #### Added
    * [pr#685](https://github.com/pyecharts/pyecharts/pull/685) 图表方法(`use_theme`/`config`/`add`)支持链式调用
    * [pr#690](https://github.com/pyecharts/pyecharts/pull/690) Radar 新增 `set_radar_component` 方法，废弃 `config` 方法；Parallel 图新增 `set_schema` 方法，废弃 `confg` 方法
    * [issue#687](https://github.com/pyecharts/pyecharts/issues/687) 新增 `add_coordinate_json` 方法用于支持导入 Geo/Geolines 坐标数据
    * [issue#691](https://github.com/pyecharts/pyecharts/issues/691) 为每种图形新增 `is_animation` 初始化参数，用于控制是否显示动画。
    * 新增 [geo-region-coords](https://github.com/pyecharts/geo-region-coords) 辅助项目，提供中国地区坐标查询。

    #### Updated
    * [issue#678](https://github.com/pyecharts/pyecharts/issues/678) 将 `extra_html_text_label` 默认位置移动到图形顶部。
    * [pr#677](https://github.com/pyecharts/pyecharts/pull/677) 重构 Polar，更正错误参数。


* ### version 0.5.8 - 2018.8.13

    #### Added
    * [issue#655](https://github.com/pyecharts/pyecharts/issues/655) 新增多个自定义主题：westeros, wonderland, chalk, halloween, essos，walden, romantic and purple-passion
    * [issue#669](https://github.com/pyecharts/pyecharts/issues/669) 新增 Tree 图形种类。
    * Polar 图新增 `angleaxis_label_interval` 参数，用于控制坐标轴刻度标签的显示间隔，在类目轴中有效。


* ### version 0.5.7 - 2018.8.11

    #### Added
    * [issue#651](https://github.com/pyecharts/pyecharts/issues/651) Scatter 图新增 `extra_name` 参数，额外的数据项的名称，可以为每个数据点指定一个名称。
    * [issue#657](https://github.com/pyecharts/pyecharts/issues/657) 基本图形新增 `extra_html_text_label` 参数用于显示额外的文本标签，仅限于在单图形或者 Page 时使用。
    * [issue#660](https://github.com/pyecharts/pyecharts/issues/660) 为 X/Y 坐标轴新增 `xaxis_line_color`, `xaxis_line_width`, `yaxis_line_color`, `yaxis_line_width` 四个参数，用于控制其坐标轴线线的颜色以及宽度。
    * [pr#663](https://github.com/pyecharts/pyecharts/pull/663) 新增 `coordinate_region` 参数用于指定国家/地区检索坐标且提供了 echarts-cities-pypkg 为可选的地理数据扩展。引入来自 [geonames.org](http://geonames.org/) 的 138,398 个城市坐标。


* ### version 0.5.6 - 2018.7.28

    #### Fixed
    * [issue#452](https://github.com/pyecharts/pyecharts/issues/452) 修复 K 线图不能显示 tooltip【open, close, lowest, highest】的 bug
    * [issue#639](https://github.com/pyecharts/pyecharts/issues/639) 修复 Line 图当 X 轴的类型设置为 'value' 的时候，X、Y 轴均显示 Y 轴数据的 bug
    * [issue#636](https://github.com/pyecharts/pyecharts/issues/636) 修复 Geo/Geoline 图坐标地点名替换 Legend 的 bug

    #### Updated
    * 修正参数拼写，将 `tooltip_tragger`, `tooltip_tragger_on` 修正为 `tooltip_trigger`, `tooltip_trigger_on`
    * 更新 echarts 及附属 js 文件版本 echarts 4.0.4 -> 4.1.0，echarts-gl 1.1.0 -> 1.1.1，echarts-liquidfill 2.0.0 -> 2.0.1
    * [issue#634](https://github.com/pyecharts/pyecharts/issues/634) 新增 `is_datazoom_extra_show`, `datazoom_extra_type`, `datazoom_extra_range`, `datazoom_extra_orient`, `datazoom_extra_xaxis_index`, `datazoom_extra_yaxis_index` 参数用于设置额外的 dataZoom 控制条，可将效果同时作用于 X、Y 轴


* ### version 0.5.5 - 2018.05.17

    #### Added
    * [issue#565](https://github.com/pyecharts/pyecharts/issues/565) Geolines 图数据项可以新增数值维度
    * [issue#573](https://github.com/pyecharts/pyecharts/issues/573) 新增对 jupyter notebook 家族的新成员 [nteract](https://nteract.io/) 的支持

    #### Fixed
    * [issue#572](https://github.com/pyecharts/pyecharts/issues/572) 修复 HeatMap 图纵坐标显示索引值，而非 data 值的 bug

* ### version 0.5.4 - 2018.05.15

    #### Updated
    * 重构 `Page` 类，新增图表命名名称引用。

    #### Fixed
    * [issue#555](https://github.com/pyecharts/pyecharts/issues/555) 修复 v0.5.3 Polar 图不能显示的 bug
    * [issue#541](https://github.com/pyecharts/pyecharts/issues/541) 修复 v0.5.3 Django + pyecharts 不能正常导入的 bug

* ### version 0.5.3 - 2018.05.10

    #### Fixed
    * [issue#544](https://github.com/pyecharts/pyecharts/issues/544) 修复 v0.5.2 主题颜色默认颜色配置与前版本有差别太大的 bug

* ### version 0.5.2 - 2018.05.04

    #### Added
    * [issue#512](https://github.com/pyecharts/pyecharts/issues/512) 新增自定义主题功能

* ### version 0.5.1 - 2018.05.02

    #### Fixed
    * [issue#516](https://github.com/pyecharts/pyecharts/issues/516) 修复直角坐标系图 X 轴分隔符展示效果不一致的 bug

    #### Update
    * [issue#518](https://github.com/pyecharts/pyecharts/issues/518) 放弃 sdist 构建方式，使用 wheel 构建项目包，并在 PYPI 上为项目添加 description

* ### version 0.5.0 - 2018.04.28

    #### Added
    * [issue#311](https://github.com/pyecharts/pyecharts/issues/311) 提供 Jupyter Notebook 导出为 PDF 没有图片的解决方案
    * 新增对 JavaScript 回调函数配置项和事件绑定的支持。详细内容请移步至 [release-note/v050](zh-cn/release-note/v050)。

    #### Fixed
    * [issue#448](https://github.com/pyecharts/pyecharts/issues/448) 修复 Timeline 中 Overlap 图的 label_color 配置项不生效的 bug
    * [issue#504](https://github.com/pyecharts/pyecharts/issues/504) 修复 markpoint 标记点标注不显示的 bug

    #### Updated
    * 重构底层 `option.py` 配置项代码，使其更加具有`面向对象`特征，相关文件转移至新 package echarts。
    * 将地图数据及接口转移至 'pyecharts.datasets' 包，更多内容请参考 [地理地图数据](zh-cn/datasets)。
    * `pyecharts.Geo` 和 `pyecharts.GeoLines` 新增 `add_coordinate` 方法用于新增一个自定义城市地理位置的功能。

* ### version 0.4.1 - 2018.03.13

    #### Fixed
    * [issue#437](https://github.com/pyecharts/pyecharts/issues/437) 修复 Timeline 图累计多个 Bar 图会导致条形宽度压缩的 bug
    * [issue#437](https://github.com/pyecharts/pyecharts/issues/437) 修复 Timeline 图不能正常显示 Tooltip 组件的 bug

* ### version 0.4.0 - 2018.03.09

    #### Added
    * `EchartsEnvironment` 类性增 `render_chart_to_file`
    * [issue#425](https://github.com/pyecharts/pyecharts/issues/425) 新增 `pieces` 配置项，为 visualMap 组件提供自定义分段标签的功能
    * 新增 `tooltip_border_width`, `tooltip_border_color`, `tooltip_background_color` 三个参数用与提示框背景颜色及边框的配置
    * [issue#376](https://github.com/pyecharts/pyecharts/issues/376) 新增 `mark_line_coords` 配置项用于指定标记线的起点和终点
    * [issue#431](https://github.com/pyecharts/pyecharts/issues/431) pyecharts.Chart 图表类新增 renderer 参数，用于指定渲染方式，支持 canvas / svg 两种方式

    #### Updated
    * 更新 jupyter-echarts 至 1.4.0: echarts 3.6.2 -> 4.0.4, echarts-gl 1.0.0-b4 -> 1.1.0, echarts-liquidfill 1.0.5 -> 2.0.0, echarts-wordcloud 1.1.0 -> 1.1.2
    * 优化内部渲染逻辑，提高渲染效率。

    #### Fixed
    * 修正 width / height 在 Jupyter Notebook 渲染错误的 Bug
    * [issue#432](https://github.com/pyecharts/pyecharts/issues/432) 修复水球图和词云图不能指定 Toolbox 等选项的 Bug

* ### version 0.3.3 - 2018.03.01

    #### Added
    * 防止将来的依赖包影响 v0.3.2 的功能: lml==0.0.2, jupyter-echarts-pypkg==0.0.11
    * 新增 `name_map`， [允许用户采用自己地图名称](http://echarts.baidu.com/option.html#series-map.nameMap)。

    #### Changed
    * `Chart.render_embed` 返回 `jinja2.Markup` 实例
    * `Base.show_config` 重命名为 `Base.print_echarts_options`
    * 移除 `EchartsEnvironment.configure_pyecharts` 方法

* ### version 0.3.2 - 2018.02.26

    从此版本开始，将不再自带地图 js 文件。有需要的开发人员，请自选安装。

    #### Added
    * 新增 `chart_id` 配置项，可设置图形 id，对应为每个图在 html 中的 div#id
    * 新增 jupyter-echarts-pypkg, echarts-china-provinces-pypkg, echarts-china-cities-pypkg 和 echarts-countries-pypkg。第一个是自带安装，后三个是可选安装。
    * [issue#395](https://github.com/pyecharts/pyecharts/issues/395) 新增 `is_splitline_show` 配置项，用于控制是否显示网格线
    * 新增 AppVeyor CI，为 Windows OS 提供测试功能

    #### Fixed
    * [issue#322](https://github.com/pyecharts/pyecharts/issues/322) 修复在 timeline 中不能设置多个 legend 的 bug
    * [issue#357](https://github.com/pyecharts/pyecharts/issues/357) 修复 Line 图 symbol 大小不能调整的 bug
    * [issue#371](https://github.com/pyecharts/pyecharts/issues/371) 修复 Parallel 图 Line 样式失效的 bug
    * [issue#378](https://github.com/pyecharts/pyecharts/issues/378) 修复 Geo 图中当多次 render 时相同 value 值会被叠加的 bug
    * [issue#338](https://github.com/pyecharts/pyecharts/issues/338) 修复 timeline 中 map 的 visualmap 组件不能正常显示的 bug

    #### Updated
    * 地图更新：[台湾地图补了市，县，岛](https://github.com/pyecharts/pyecharts/pull/316), [重庆地图补了开州区](https://github.com/pyecharts/pyecharts/pull/317)
    * 优化图表 API，图表 js_dependencies 属性返回有序列表
    * 优化部分代码逻辑
    * [issue#377](https://github.com/pyecharts/pyecharts/issues/377) 为 Kline 提供 Candlestick 别名

    #### Changed
    * 示例移到新的代码仓库 [pyecharts-users-cases](https://github.com/pyecharts/pyecharts-users-cases)

    #### Removed
    * [PR#368](https://github.com/pyecharts/pyecharts/pull/368) `pyecharts/templates/js` 被删去了。`jupyter-echarts` 不再内嵌于 pyecharts 。
    * echarts-china-cities-js 和 echarts-countries-js 不再是必选，而是可选图库。

* ### version 0.3.1 - 2017.12.13

    #### Fixed
    * [issue#290](https://github.com/pyecharts/pyecharts/issues/290) 紧急修复 v0.3.0 版本不能正常显示图形的严重 bug
    * [issue#296](https://github.com/pyecharts/pyecharts/issues/296) 修复 Timeline 不能在 notebook 中显示的 bug

* ### version 0.3.0 - 2017.12.11

    #### Added
    * 图表 `render` 方法增加 `template_name` 、`object_name`、`extra_context` 等参数，全面支持自定义模板
    * 新增统一配置函数 `pyecharts.configure` ，支持设置模板目录，JS 文件仓库路径。
    * [issue#252](https://github.com/pyecharts/pyecharts/issues/252) 新增 `xaxis_label_textsize`, `xaxis_label_textcolor`, `yaxis_label_textsize`, `yaxis_label_textcolor` 四个参数修改坐标轴标签的字体和颜色
    * [issue#258](https://github.com/pyecharts/pyecharts/issues/258) 新增 `mark_point_valuedim` 参数，并将 `mark_line_valuedim` 和 `mark_point_valuedim` 参数类型修改为 list。
    * [issue#260](https://github.com/pyecharts/pyecharts/issues/260) 新增 `is_toolbox_show` 参数用于控制是否显示右侧实用工具箱。

    #### Updated
    * 重写底层逻辑，支持在模板文件中使用 `echarts_*` 系列模板函数
    * js 依赖文件支持外部链接方式引入。
    * `pyecharts.custom.Page` 类实现 `list` 协议，支持迭代、索引、添加、扩展等操作。
    * 图表 width 和 height 支持 '50%' 、'78px' 等其他 css 有效长度形式。
    * 更新 jupyter-echarts 至 1.3.3: [上海地图补了崇明区](https://github.com/pyecharts/jupyter-echarts/issues/9), [西藏地图补了山南市](https://github.com/pyecharts/jupyter-echarts/issues/7)

* ### version 0.2.7 - 2017.10.27

    #### Added
    * 新增 GeoLines（地理坐标系线图）
    * [issue#230](https://github.com/pyecharts/pyecharts/issues/230) 新增工具类 `Style`，用于简化代码编写和统一风格

    #### Changed
    * [issue#232](https://github.com/pyecharts/pyecharts/issues/232) Grid, Overlap, Timeline 类初始化参数的变动

    #### Fixed
    * 修复 Geo 系列名无法正常显示的问题
    * [issue#229](https://github.com/pyecharts/pyecharts/issues/229) 修复水球图不能自定义图形的问题

* ### version 0.2.6 - 2017.10.14

    #### Added
    * 为 [文档](https://github.com/pyecharts/pyecharts/blob/master/docs/zh-cn/documentation.md) 新增 [使用技巧](https://github.com/pyecharts/pyecharts/blob/master/docs/zh-cn/documentation.md#使用技巧) 介绍
    * [issue#194](https://github.com/pyecharts/pyecharts/issues/194) 新增 `is_map_symbol_show` 参数，用于控制 Map 图 [红点的显示](https://www.oschina.net/question/1416804_245423)
    * [issue#192](https://github.com/pyecharts/pyecharts/issues/192) 新增 `label_emphasis_pos`, `label_emphasis_textsize`, `label_emphasis_textcolor` 参数，用于解决 Geo 图 tooltip 不能只显示城市名和数值的问题
    * [issue#132](https://github.com/pyecharts/pyecharts/issues/132) 新增图形类型树图
    * [issue#181](https://github.com/pyecharts/pyecharts/issues/181) 为 Geo 图新增 `is_roam` 参数解决不能缩放和移动的问题
    * [issue#199](https://github.com/pyecharts/pyecharts/issues/199) 为 markLine 新增 `mark_line_symbolsize` 和 `mark_line_valuedim` 参数，解决不能指定维度以及标记大小不能调整的问题
    * [issue#200](https://github.com/pyecharts/pyecharts/issues/200) 为 xyAxis 通用配置项新增 `is_xaxis_show` 和 `is_yaxis_show` 参数，（控制是否显示 x 轴或 y 轴）解决设计可编辑文本的问题
    * [issue#201](https://github.com/pyecharts/pyecharts/issues/201) 为 Bar 图新增 `bar_category_gap` 参数，提供绘制直方图的方案
    * [issue#208](https://github.com/pyecharts/pyecharts/issues/208) 为 dataZoom 通用配置项 `datazoom_type` 新增类型 'both'（同时拥有 'slider' 以及 'inside')
    * [issue#208](https://github.com/pyecharts/pyecharts/issues/208) 为 HeatMap 图新增 **日历热力图**

    #### Changed
    * 将 label 通用配置项的 `is_emphasis` 参数更改为 `is_label_emphasis`
    * show_config() 修改用 JSON 显示

    #### Fixed
    * [issue#195](https://github.com/pyecharts/pyecharts/issues/195) 修复 HeatMap 图配置 x、y 轴属性无效的问题

* ### version 0.2.5 - 2017.9.28

    #### Added
    * [issue#173](https://github.com/pyecharts/pyecharts/issues/173) 为 xyAxis 通用配置项新增 `is_xaxis_boundarygap` 和 `is_yaxis_boundartgap` 参数
    * [issue#22](https://github.com/pyecharts/pyecharts/issues/22) 为散点图新增 `extra_data` 参数，可以为数据新增除 x y 轴外的其他维度
    * 为 markPoint 新增自定义标记点功能
    * 为 visualMap 新增 `visual_dimension` 参数，可以指定 visualmap 映射到哪个数据维度
    * 为 Map 图新增 [212个国家和地区](https://github.com/pyecharts/echarts-countries-js#featuring-citiesor-for-single-download)
    * 部分解决 Overlap 和 Grid 不能一起使用的问题（当 Overlap 为多 x 轴或多 y 轴的时候坐标轴索引仍会出现问题）

* ### version 0.2.4 - 2017.9.8

    #### Added
    * [issue#148](https://github.com/pyecharts/pyecharts/issues/148) 为 Radar.config() 新增 `legend_text_size` 参数
    * [issue#148](https://github.com/pyecharts/pyecharts/issues/148) 为 Legend 通用配置项新增 `legend_text_color` 和 `legend_text_font` 参数
    * [issue#156](https://github.com/pyecharts/pyecharts/issues/156) 为 xyAxis 通用配置项新增 `xaxis_force_interval` 和 `yaxis_force_interval` 参数
    * 为 Visualmap 通用配置项新增 `is_piecewise` 和 `visual_split_number` 参数
    * [issue#160](https://github.com/pyecharts/pyecharts/issues/160) 为 Base 类新增 `page_title` 参数，初始化类实例的时候可指定生成的 html 文件 `<title>` 标签的值。自定义类 Grid/Overlap/Timeline/Page 以第一个添加的实例的 `page_title` 参数为准。
    * [issue#165](https://github.com/pyecharts/pyecharts/issues/165) 为 Radar 图新增 `label` 通用配置项，现可以展示 `label` 文字标签，但是建议在数据量少的时候使用（比如数据量为 1 的时候）

    #### Changed
    * 压缩 js 文件体积，总体体积减少约 0.3MB

    #### Fixed
    * [issue#158](https://github.com/pyecharts/pyecharts/issues/158) 修复 Grid/Timeline/Overlap 在 Page 中不能正常使用的 bug

* ### version 0.2.3 - 2017.9.1

    #### Fixed
    * [issue#143](https://github.com/pyecharts/pyecharts/issues/143) [issue#146](https://github.com/pyecharts/pyecharts/issues/146) 修复默认状态下 Graph 不显示连线的 bug
    * [issue#145](https://github.com/pyecharts/pyecharts/issues/145) 修复 dataZoom 无法正常使用的 bug

* ### version 0.2.2 - 2017.8.31
    #### Added
    * Map 图和 Geo 图增加 [363个二线城市地图](https://github.com/pyecharts/echarts-china-cities-js#featuring-citiesor-for-single-download)
    * Map 图新增 label 模块，现可以利用标签显示地区名称
    * Geo 图新增 3000+ 城市地区经纬度信息，现已基本覆盖全国各个地区
    * Geo 图新增 `geo_cities_coords` 参数，用户可以为自己所选地图提供地区经纬度坐标（这将会覆盖原来预存的城市坐标信息），即完全按照用户提供的坐标来定位。
    * 新增图形种类 ThemeRiver（主题河流图）
    * 新增 `is_more_utils` 参数，在 `add()` 中设置该标志位为 True 则会提供更多的实用工具按钮（建议在 Line, Kilne, Bar 等直角坐标图形中设置）。默认只提供『数据视图』和『下载』按钮。
    * [issue#138](https://github.com/pyecharts/pyecharts/issues/138) 新增 `is_xaxis_inverse`, `is_yaxis_inverse`, `xaxis_pos`, `yaxis_pos` 参数，提供倒映直角坐标系功能
    * [issue#140](https://github.com/pyecharts/pyecharts/issues/140) 为每种图形（包括 Overlap, Grid, Timeline）都提供 Public 的 `options` 属性，返回实例的 `self._option`

    #### Fixed
    * [issue#133](https://github.com/pyecharts/pyecharts/issues/133) 回退 Echarts 版本，从 v3.7.0 回退至原先的 v3.6.2，解决标签不能正常显示的 bug

* ### version 0.2.1 - 2017.8.25

    #### Added
    * [issue#127](https://github.com/pyecharts/pyecharts/issues/127) 新增数据图切换按钮（只针对部分图有效）

    #### Fixed
    * [issue#130](https://github.com/pyecharts/pyecharts/issues/130) 更改 freeze_js，更正文件路径表示方法
    * 修复直角坐标系的标签显示问题


* ### version 0.2.0 - 2017.8.25

    #### Added
    * [issue#118](https://github.com/pyecharts/pyecharts/issues/118) 新增 `datazoom_xaxis_index`, `datazoom_yaxis_index`，可使 datazoom 组件同时控制多个 x y 轴。
    * 新增 jupyter-notebook 中的 js host 参数，用户可自行决定使用本地后者网络 js 文件，确保转移 notebook 时图形可正常显示
    * 新增图形种类 Boxplot（箱形图）
    * [issue#120](https://github.com/pyecharts/pyecharts/issues/120) 新增图形种类 Sankey（桑基图）

    #### Changed
    * 更新 Flask&Django 模板，加载文件的体积大大减小，出图速度更快。
    * 更新 echarts 到 3.7.0

    #### Fixed
    * 修复 Page 类于其他自定义类共用出现问题的 bug


* ### version 0.1.9.7 - 2017.8.20

    #### Fixed
    * [issue#113](https://github.com/pyecharts/pyecharts/issues/113) 修复 requirements.txt 中 jupyter-pip 版本过旧问题
    * [issue#109](https://github.com/pyecharts/pyecharts/issues/109) 修复地图不能正常显示的问题


* ### version 0.1.9.6 - 2017.8.19

    #### Added
    * [issue#95](https://github.com/pyecharts/pyecharts/issues/95) Overlap 类中新增 `xaxis_index`, `is_add_xaxis`, `yaxis_index`, `is_add_yaxis` 参数，现支持多 Y 轴或多 X 轴
    * Page 类现在也支持在 jupyter-notebook 中显示了，直接调用 Page() 实例即可。
    * Graph 图中新增 `graph_edge_symbol`, `graph_edge_symbolsize` 参数
    * [issue#94](https://github.com/pyecharts/pyecharts/issues/94) 提供 pyecharts-snapshot 用于将生成的图片保存为 png 或 pdf 文件，仅静态图片生效。（3D 图和动态图不生效）
    * [issue#98](https://github.com/pyecharts/pyecharts/issues/98) 通用配置项中新增 tooltip 模块

    #### Changed
    * jupyter-notebook 和本地 render() 现在均采用动态加入 js 依赖文件的方法，生成文件体积大大缩小。
    * 更改通用配置项中的 label 的参数 `formatter` 为 `label_formatter`
    * 更改 `clockwise` 参数为 `is_clockwise`
    * 更改 Graph 图中的 `repulsion`, `gravity`, `edge_length`, `layout` 参数为 `graph_repulsion`, `graph_gravity`, `graph_edge_length`, `graph_layout`


* ### version 0.1.9.5 - 2017.8.16

    #### Added
    * 为 xyAxis 模块新增下列参数
       `xaxis_interval`, `xaxis_name_size`, `xaxis_name_gap`, `xaxis_margin`, `is_xaxislabel_align`
        `yaxis_interval`, `yaxis_name_size`, `yaxis_name_gap`, `yaxis_margin`, `is_yaxislabel_align`
    * [issue#86](https://github.com/pyecharts/pyecharts/issues/86) 为 3D 图新增参数用于配置坐标轴选项（参见通用配置项中的 axis3D）
    * 修改自定义模块的接口，现自定义模块有以下 4 个类，具体用法参见文档
        * Grid 类：并行显示多张图
        * Overlap 类：结合不同类型图表叠加画在同张图上
        * Page 类：同一网页按顺序展示多图
        * Timeline 类：提供时间线轮播多张图
    * 新增 Timeline 功能，支持轮播多张图表

    #### Changed
    * jupyter notebook 现在也为离线模式，从本地加载项目所需 js 文件。至此 pyecharts 彻底实现本地化运行。速度更快，不再受网速影响。

    #### Removed
    * 删除冗余 js 文件，压缩项目体积。
    * 废弃 xAxis，yAxis 中的 `interval`, `xy_font_size`, `namegap` 参数。


* ### version 0.1.9.4 - 2017.8.10

    #### Added
    * [issue#76](https://github.com/pyecharts/pyecharts/issues/76) 新增 Page 类，现能同时在一个 html 页面内按顺序展示多个图形。（参见用户自定义）

    #### Changed
    * 更改 Image 依赖模块为 pillow


* ### version 0.1.9.3 - 2017.8.10

    #### Added
    * [issue#72](https://github.com/pyecharts/pyecharts/issues/72) [issue#41](https://github.com/pyecharts/pyecharts/issues/41) 新增 `xaxis_type`, `yaxis_type` 参数，可通过设置该参数指定直角坐标系数轴类型。（参见 Line，Scattre 图）
    * [issue#09](https://github.com/pyecharts/pyecharts/issues/9) 集成 Flask + Django

    #### Removed
    * 废弃 `npcast()`, `pdcast()` 方法，新版本已经在内部封装了处理逻辑，具体参见文档的 pandas&numpy 示例


* ### version 0.1.9.2 - 2017.8.6

    #### Added
    * [issue#52](https://github.com/pyecharts/pyecharts/issues/52) 新增 `xaxis_rotate`, `yaxis_rotate` 参数，可通过设置该参数解决强制显示所有坐标轴标签时因过于密集重叠的问题。参见（Bar 图）
    * 新增 `xaxis_min`, `xaxis_max`. `yaxis_min`, `yaxis_max` 参数，可设置坐标轴上的最大最小值，针对数值轴有效。

    #### Changed
    * [issue#67](https://github.com/pyecharts/pyecharts/issues/67) `render()` 方法现在为离线模式，实现本地生成 .html 文件，加载速度更快。

    #### Fixed
    * [issue#61](https://github.com/pyecharts/pyecharts/issues/61) 解决 3D 图形不能在 jupyter notebook 上正常显示的问题。

    #### Removed
    * 废弃 `render_notebook()` 方法，现可直接调用图形实例显示在 jupyter notebook 上。


* ### version 0.1.9.1 - 2017.7.31

    #### Added
    * 加入 Travis-CI 自动化测试。
    * [issue#46](https://github.com/pyecharts/pyecharts/issues/46) legend 增加 `legend_selectedmode` 参数，图例可以设置为单例或者多例。（参见 Radar 图）
    * visualmap 组件增加 `visual_type` 和 `visual_range_size` 参数。现在支持映射到颜色和图形大小两种方式。（参见 Scatter 图）


* ### version 0.1.9 - 2017.7.30

    #### Added
    * [issue#28](https://github.com/pyecharts/pyecharts/issues/28) datazoom 中增加了将组件效果显示在 y 坐标轴中的功能。（参见 KLine 图）
    * 新增对 Pandas 和 Numpy 数据的简单处理。解决直接传入 Pandas 和 Numpy 数据类型出错的问题。（参见开始使用）
    * 新增 Bar3D, Line3D, Scatter3D 三种 3D 立体图。

    #### Fixed
    * [issue#34](https://github.com/pyecharts/pyecharts/issues/34) 解决在 macos 下安装出错的问题。


* ### version 0.1.8 - 2017.7.28

    #### Added
    * [issue#05](https://github.com/pyecharts/pyecharts/issues/5) 新增在 Jupyter Notebook 中展示图表功能。感谢 [@ygw365](https://github.com/ygw365) 提供这部分的代码模板 和 [@muxuezi](https://github.com/muxuezi) 协助对代码进行改进!
    * 新增对自定义地图的使用说明


* ### version 0.1.7 - 2017.7.26

    #### Added
    * 增加并行显示图表功能


* ### version 0.1.6 - 2017.7.24

    #### Added
    * 新增了热力图


* ### version 0.1.5 - 2017.7.22

    #### Added
    * 新增了 K 线图


* ### version 0.1.4 - 2017.7.20

    #### Added
    * 第一个稳定版本
