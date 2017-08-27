# Version Log

## 项目期待

* 更开放，更自由，更方便，更实用。


## 版本信息

* ### version 0.2.2 (Dev)
    #### Added
    * 增加331个二线城市地图: 六盘水,安顺,毕节,贵阳,遵义,铜仁,黔东南苗族侗族自治州,黔南布依族苗族自治州,黔西南布依族苗族自治州,三门峡,信阳,南阳,周口,商丘,安阳,平顶山,开封,新乡,洛阳,漯河,濮阳,焦作,许昌,郑州,驻马店,鹤壁,东营,临沂,威海,德州,日照,枣庄,泰安,济南,济宁,淄博,滨州,潍坊,烟台,聊城,莱芜,菏泽,青岛,乐山,内江,凉山彝族自治州,南充,宜宾,巴中,广元,广安,德阳,成都,攀枝花,泸州,甘孜藏族自治州,眉山,绵阳,自贡,资阳,达州,遂宁,阿坝藏族羌族自治州,雅安,南京,南通,宿迁,常州,徐州,扬州,无锡,泰州,淮安,盐城,苏州,连云港,镇江,果洛藏族自治州,海东,海北藏族自治州,海南藏族自治州,海西蒙古族藏族自治州,玉树藏族自治州,西宁,黄南藏族自治州,三明,南平,厦门,宁德,泉州,漳州,福州,莆田,龙岩,丽水,台州,嘉兴,宁波,杭州,温州,湖州,绍兴,舟山,衢州,金华,十堰,咸宁,孝感,宜昌,恩施土家族苗族自治州,武汉,荆州,荆门,襄阳,鄂州,随州,黄冈,黄石,上饶,九江,南昌,吉安,宜春,抚州,新余,景德镇,萍乡,赣州,鹰潭,山南,拉萨,日喀则,昌都,林芝,那曲地区,阿里地区,七台河,伊春,佳木斯,双鸭山,哈尔滨,大兴安岭地区,大庆,牡丹江,绥化,鸡西,鹤岗,黑河,齐齐哈尔,云浮,佛山,广州,惠州,揭阳,梅州,汕头,汕尾,江门,河源,深圳,清远,湛江,潮州,珠海,肇庆,茂名,阳江,韶关,临沧,丽江,保山,大理白族自治州,德宏傣族景颇族自治州,怒江傈僳族自治州,文山壮族苗族自治州,昆明,昭通,普洱,曲靖,楚雄彝族自治州,玉溪,红河哈尼族彝族自治州,西双版纳傣族自治州,迪庆藏族自治州,北海,南宁,崇左,来宾,柳州,桂林,梧州,河池,玉林,百色,贵港,贺州,钦州,防城港,咸阳,商洛,安康,宝鸡,延安,榆林,汉中,渭南,西安,铜川,临夏回族自治州,兰州,天水,定西,平凉,庆阳,张掖,武威,甘南藏族自治州,白银,酒泉,金昌,陇南,保定,唐山,廊坊,张家口,承德,石家庄,秦皇岛,衡水,邢台,邯郸,中卫,吴忠,固原,石嘴山,银川,吉林,四平,延边朝鲜族自治州,松原,白城,白山,辽源,通化,长春,娄底,岳阳,常德,张家界,怀化,株洲,永州,湘潭,湘西土家族苗族自治州,益阳,衡阳,邵阳,郴州,长沙,亳州,六安,合肥,安庆,宣城,宿州,池州,淮北,淮南,滁州,芜湖,蚌埠,铜陵,阜阳,马鞍山,黄山,乌兰察布,乌海,兴安盟,包头,呼伦贝尔,呼和浩特,巴彦淖尔,赤峰,通辽,鄂尔多斯,锡林郭勒盟,阿拉善盟,临汾,吕梁,大同,太原,忻州,晋中,晋城,朔州,运城,长治,阳泉,万宁,三亚,三沙,东方,临高县,乐东黎族自治县,五指山,保亭黎族苗族自治县,儋州,定安县,屯昌县,文昌,昌江黎族自治县,海口,澄迈县,琼中黎族苗族自治县,琼海,白沙黎族自治县,陵水黎族自治县,丹东,大连,抚顺,朝阳,本溪,沈阳,盘锦,营口,葫芦岛,辽阳,铁岭,锦州,阜新,鞍山


* ### version 0.2.1 - 2017.8.25（Current）

    #### Added
    * [issue#127](https://github.com/chenjiandongx/pyecharts/issues/127) 新增数据图切换按钮（只针对部分图有效）

    #### Fixed
    * [issue#130](https://github.com/chenjiandongx/pyecharts/issues/130) 更改 freeze_js，更正文件路径表示方法
    * 修复直角坐标系的标签显示问题


* ### version 0.2.0 - 2017.8.25

    #### Added
    * [issue#118](https://github.com/chenjiandongx/pyecharts/issues/118) 新增 `datazoom_xaxis_index`, `datazoom_yaxis_index`，可使 datazoom 组件同时控制多个 x y 轴。
    * 新增 jupyter-notebook 中的 js host 参数，用户可自行决定使用本地后者网络 js 文件，确保转移 notebook 时图形可正常显示
    * 新增图形种类 Boxplot（箱形图）
    * [issue#120](https://github.com/chenjiandongx/pyecharts/issues/120) 新增图形种类 Sankey（桑基图）

    #### Changed
    * 更新 Flask&Django 模板，加载文件的体积大大减小，出图速度更快。
    * 更新 echarts 到 3.7.0

    #### Fixed
    * 修复 Page 类于其他自定义类共用出现问题的 bug


* ### version 0.1.9.7 - 2017.8.20

    #### Fixed
    * [issue#113](https://github.com/chenjiandongx/pyecharts/issues/113) 修复 requirements.txt 中 jupyter-pip 版本过旧问题
    * [issue#109](https://github.com/chenjiandongx/pyecharts/issues/109) 修复地图不能正常显示的问题


* ### version 0.1.9.6 - 2017.8.19

    #### Added
    * [issue#95](https://github.com/chenjiandongx/pyecharts/issues/95) Overlap 类中新增 `xaxis_index`, `is_add_xaxis`, `yaxis_index`, `is_add_yaxis` 参数，现支持多 Y 轴或多 X 轴
    * Page 类现在也支持在 jupyter-notebook 中显示了，直接调用 Page() 实例即可。
    * Graph 图中新增 `graph_edge_symbol`, `graph_edge_symbolsize` 参数
    * [issue#94](https://github.com/chenjiandongx/pyecharts/issues/94) 提供 pyecharts-snapshot 用于将生成的图片保存为 png 或 pdf 文件，仅静态图片生效。（3D 图和动态图不生效）
    * [issue#98](https://github.com/chenjiandongx/pyecharts/issues/98) 通用配置项中新增 tooltip 模块
    
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
    * [issue#86](https://github.com/chenjiandongx/pyecharts/issues/86) 为 3D 图新增参数用于配置坐标轴选项（参见通用配置项中的 axis3D）
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
    * [issue#76](https://github.com/chenjiandongx/pyecharts/issues/76) 新增 Page 类，现能同时在一个 html 页面内按顺序展示多个图形。（参见用户自定义）

    #### Changed
    * 更改 Image 依赖模块为 pillow


* ### version 0.1.9.3 - 2017.8.10

    #### Added
    * [issue#72](https://github.com/chenjiandongx/pyecharts/issues/72) [issue#41](https://github.com/chenjiandongx/pyecharts/issues/41) 新增 `xaxis_type`, `yaxis_type` 参数，可通过设置该参数指定直角坐标系数轴类型。（参见 Line，Scattre 图）
    * [issue#09](https://github.com/chenjiandongx/pyecharts/issues/9) 集成 Flask + Django

    #### Removed
    * 废弃 `npcast()`, `pdcast()` 方法，新版本已经在内部封装了处理逻辑，具体参见文档的 pandas&numpy 示例


* ### version 0.1.9.2 - 2017.8.6

    #### Added
    * [issue#52](https://github.com/chenjiandongx/pyecharts/issues/52) 新增 `xaxis_rotate`, `yaxis_rotate` 参数，可通过设置该参数解决强制显示所有坐标轴标签时因过于密集重叠的问题。参见（Bar 图）
    * 新增 `xaxis_min`, `xaxis_max`. `yaxis_min`, `yaxis_max` 参数，可设置坐标轴上的最大最小值，针对数值轴有效。

    #### Changed
    * [issue#67](https://github.com/chenjiandongx/pyecharts/issues/67) `render()` 方法现在为离线模式，实现本地生成 .html 文件，加载速度更快。

    #### Fixed
    * [issue#61](https://github.com/chenjiandongx/pyecharts/issues/61) 解决 3D 图形不能在 jupyter notebook 上正常显示的问题。

    #### Removed
    * 废弃 `render_notebook()` 方法，现可直接调用图形实例显示在 jupyter notebook 上。


* ### version 0.1.9.1 - 2017.7.31

    #### Added
    * 加入 Travis-CI 自动化测试。 
    * [issue#46](https://github.com/chenjiandongx/pyecharts/issues/46) legend 增加 `legend_selectedmode` 参数，图例可以设置为单例或者多例。（参见 Radar 图）
    * visualmap 组件增加 `visual_type` 和 `visual_range_size` 参数。现在支持映射到颜色和图形大小两种方式。（参见 Scatter 图）


* ### version 0.1.9 - 2017.7.30

    #### Added
    * [issue#28](https://github.com/chenjiandongx/pyecharts/issues/28) datazoom 中增加了将组件效果显示在 y 坐标轴中的功能。（参见 KLine 图）
    * 新增对 Pandas 和 Numpy 数据的简单处理。解决直接传入 Pandas 和 Numpy 数据类型出错的问题。（参见开始使用）
    * 新增 Bar3D, Line3D, Scatter3D 三种 3D 立体图。

    #### Fixed
    * [issue#34](https://github.com/chenjiandongx/pyecharts/issues/34) 解决在 macos 下安装出错的问题。


* ### version 0.1.8 - 2017.7.28

    #### Added
    * [issue#05](https://github.com/chenjiandongx/pyecharts/issues/5) 新增在 Jupyter Notebook 中展示图表功能。感谢 [@ygw365](https://github.com/ygw365) 提供这部分的代码模板 和 [@muxuezi](https://github.com/muxuezi) 协助对代码进行改进!
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
