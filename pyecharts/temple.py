#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding=utf-8

_temple = """
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>ECharts</title>
    <!-- 引入 echarts.js -->
    <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/echarts-all-3.js"></script>
    <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts-stat/ecStat.min.js"></script>
    <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/extension/dataTool.min.js"></script>
    <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/china.js"></script>
    <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/world.js"></script>
    <script type="text/javascript" src="http://oog4yfyu0.bkt.clouddn.com/wordcloud.js"></script>
    <script type="text/javascript" src="http://oog4yfyu0.bkt.clouddn.com/anhui.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/aomen.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/beijing.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/chongqing.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/fujian.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/gansu.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/guangdong.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/guangxi.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/guizhou.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/hainan.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/hebei.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/heilongjiang.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/henan.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/hubei.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/hunan.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/jiangsu.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/jiangxi.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/jilin.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/liaoning.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/neimenggu.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/ningxia.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/qinghai.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/shangdong.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/shanghai.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/shanxi.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/sichuan.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/taiwan.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/tianjin.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/xianggang.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/xinjiang.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/xizang.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/yunnan.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/zhejiang.js "></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/guangdong.js "></script>
    <script type="text/javascript " src="http://api.map.baidu.com/api?v=2.0&ak=ZUONbpqGBsYGXNIYHicvbAbM "></script>
    <script type="text/javascript " src="http://echarts.baidu.com/gallery/vendors/echarts/extension/bmap.min.js "></script>
</head>

<body>
    <!-- 为ECharts准备一个具备大小（宽高）的Dom -->
    <div id="main" style="width: myWidthpx;height:myHeightpx; "></div>
    <script type="text/javascript ">
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('main'));

        // 指定图表的配置项和数据
        var option = myOption;

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
    </script>
</body>

</html>
"""

_temple_wd = """
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>ECharts</title>
    <!-- 引入 echarts.js -->
    <script src='https://cdn.bootcss.com/echarts/3.2.2/echarts.simple.js'></script>
    <script type="text/javascript" src="http://data-visual.cn/datav/src/js/echarts/extension/echarts-wordcloud.min.js"></script>
</head>

<body>
    <style>
        html,
        body,
        #main {
            width: 100%;
            height: 100%;
            margin: 0;
        }
    </style>
    <!-- 为ECharts准备一个具备大小（宽高）的Dom -->
    <div id="main" style="width: myWidthpx;height:myHeightpx; ">
    </div>
    <script type="text/javascript ">
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('main'));

        // 指定图表的配置项和数据
        var option = myOption;

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
    </script>
</body>

</html>
"""

temple = """
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>ECharts</title>
    <!-- 引入 echarts.js -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/echarts/3.5.4/echarts.common.min.js"></script>

</head>

<body>
    <!-- 为ECharts准备一个具备大小（宽高）的Dom -->
    <div id="main" style="width: myWidthpx;height:myHeightpx;"></div>
    <script type="text/javascript">
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('main'));

        // 指定图表的配置项和数据
        var option = myOption;

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
    </script>
</body>

</html>
"""