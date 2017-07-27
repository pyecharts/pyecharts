#!/usr/bin/env python
#coding=utf-8


_temple_notebook = """
<div id="{{ chartId }}" style="width:{{ myWidth }}px; height:{{ myHeight }}px;"></div>
<script>
    require.config({
         paths:{
            echarts: '//cdn.bootcss.com/echarts/3.6.2/echarts.min',
            china: '//echarts.baidu.com/gallery/vendors/echarts/map/js/china',
         }
    });
    require(['echarts', 'china'],function(ec){
    var myChart = ec.init(document.getElementById('{{ chartId }}'));
               var option =  {{ myOption }};
               myChart.setOption(option);
    });
</script>
"""


_temple_map_notebook = """
<div id="{{ chartId }}" style="width:{{ myWidth }}px; height:{{ myHeight }}px;"></div>
<script>
    require.config({
         paths:{
            echarts: '//cdn.bootcss.com/echarts/3.6.2/echarts.min',
            china: '//echarts.baidu.com/gallery/vendors/echarts/map/js/china',
            ##locationJs
         }
    });
    require(['echarts', 'china', '##location'],function(ec){
    var myChart = ec.init(document.getElementById('{{ chartId }}'));
               var option =  {{ myOption }};
               myChart.setOption(option);
    });
</script>
"""


_temple_lq_notebook = '''
<div id="{{ chartId }}" style="width:{{ myWidth }}px; height:{{ myHeight }}px;"></div>
<script>
    require.config({
         paths:{
           echarts: '//cdn.bootcss.com/echarts/3.2.2/echarts',
           liquidFill: '//oog4yfyu0.bkt.clouddn.com/liquidfill'
         }
    });
    require(['echarts','liquidFill'],function(ec){
    var myChart = ec.init(document.getElementById('{{ chartId }}'));
               var option =  {{ myOption }};
               myChart.setOption(option);
    });
</script>'''


_temple_wd_notebook = '''
<body>
    <style>
        html,
        body,
        # {{ chartId }} {
            width: 100%;
            height: 100%;
            margin: 0;
        }
    </style>
<div id="{{ chartId }}" style="width:{{ myWidth }}px; height:{{ myHeight }}px;"></div>
<script>
    require.config({
        paths:{
        echarts: '//cdn.bootcss.com/echarts/3.2.2/echarts.simple',
        wordCloud: '//data-visual.cn/datav/src/js/echarts/extension/echarts-wordcloud.min'
        }
    });
    require(['echarts','wordCloud'],function(ec){
    var myChart = ec.init(document.getElementById('{{ chartId }}'));
            var option =  {{ myOption }};
            myChart.setOption(option);
    });
</script>
</body>
'''


_temple_wd = """
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>ECharts</title>
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
    <div id="main" style="width:{{ myWidth }}px;height:{{ myHeight }}px; ">
    </div>
    <script type="text/javascript ">
        var myChart = echarts.init(document.getElementById('main'));
        var option = {{ myOption }};
        myChart.setOption(option);
    </script>
</body>

</html>
"""

_temple_lq = """
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>ECharts</title>
    <script src='https://cdn.bootcss.com/echarts/3.2.2/echarts.js'></script>
    <script src='http://oog4yfyu0.bkt.clouddn.com/liquidfill.js'></script>
</head>

<body>
    <div id="main" style="width:{{ myWidth }}px;height:{{ myHeight }}px;"></div>
    <script type="text/javascript">
        var myChart = echarts.init(document.getElementById('main'));
        var option = {{ myOption }};
        myChart.setOption(option);
    </script>
</body>

</html>
"""


_temple="""
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <title>ECharts</title>
    <script src="http://oog4yfyu0.bkt.clouddn.com/echarts.min.js"></script>
    <script type="text/javascript " src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/china.js"></script>
    <script type="text/javascript " src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/world.js"></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/wordcloud.js"></script>
    <script type="text/javascript " src="http://oog4yfyu0.bkt.clouddn.com/anhui.js "></script>
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
</head>

<body>
    <div id="main" style="width:{{ myWidth }}px;height:{{ myHeight }}px;"></div>
    <script type="text/javascript">
        var myChart = echarts.init(document.getElementById('main'));
        var option = {{ myOption }};
        myChart.setOption(option);
    </script>
</body>

</html>
"""


_mapindex = {
    "安徽": "anhui: '//oog4yfyu0.bkt.clouddn.com/anhui'",
    "澳门": "aomen: '//oog4yfyu0.bkt.clouddn.com/aomen'",
    "北京": "beijing: '//oog4yfyu0.bkt.clouddn.com/beijing'",
    "重庆": "chongqing: '//oog4yfyu0.bkt.clouddn.com/chongqing'",
    "福建": "fujian: '//oog4yfyu0.bkt.clouddn.com/fujian'",
    "甘肃": "gansu: '//oog4yfyu0.bkt.clouddn.com/gansu'",
    "广东": "guangdong: '//oog4yfyu0.bkt.clouddn.com/guangdong'",
    "广西": "guangxi: '//oog4yfyu0.bkt.clouddn.com/guangxi'",
    "贵州": "guizhou: '//oog4yfyu0.bkt.clouddn.com/guizhou'",
    "海南": "hainan: '//oog4yfyu0.bkt.clouddn.com/hainan'",
    "河北": "hebei: '//oog4yfyu0.bkt.clouddn.com/hebei'",
    "黑龙江": "heilongjiang: '//oog4yfyu0.bkt.clouddn.com/heilongjiang'",
    "河南": "henan: '//oog4yfyu0.bkt.clouddn.com/henan'",
    "湖北": "hubei: '//oog4yfyu0.bkt.clouddn.com/hubei'",
    "湖南": "hunan: '//oog4yfyu0.bkt.clouddn.com/hunan'",
    "江苏": "jiangsu: '//oog4yfyu0.bkt.clouddn.com/jiangsu'",
    "江西": "jiangxi: '//oog4yfyu0.bkt.clouddn.com/jiangxi'",
    "吉林": "jilin: '//oog4yfyu0.bkt.clouddn.com/jilin'",
    "辽宁": "liaoning: '//oog4yfyu0.bkt.clouddn.com/liaoning'",
    "内蒙古": "neimenggu: '//oog4yfyu0.bkt.clouddn.com/neimenggu'",
    "宁夏": "ningxia: '//oog4yfyu0.bkt.clouddn.com/ningxia'",
    "青海": "qinghai: '//oog4yfyu0.bkt.clouddn.com/qinghai'",
    "山东": "shangdong: '//oog4yfyu0.bkt.clouddn.com/shangdong'",
    "上海": "shanghai: '//oog4yfyu0.bkt.clouddn.com/shanghai'",
    "山西": "shanxi: '//oog4yfyu0.bkt.clouddn.com/shanxi'",
    "四川": "sichuan: '//oog4yfyu0.bkt.clouddn.com/sichuan'",
    "台湾": "taiwan: '//oog4yfyu0.bkt.clouddn.com/taiwan'",
    "天津": "tianjin: '//oog4yfyu0.bkt.clouddn.com/tianjin'",
    "香港": "xianggang: '//oog4yfyu0.bkt.clouddn.com/xianggang'",
    "新疆": "xinjiang: '//oog4yfyu0.bkt.clouddn.com/xinjiang'",
    "西藏": "xizang: '//oog4yfyu0.bkt.clouddn.com/xizang'",
    "云南": "yunnan: '//oog4yfyu0.bkt.clouddn.com/yunnan'",
    "浙江": "zhejiang: '//oog4yfyu0.bkt.clouddn.com/zhejiang'"
}

def get_map(map_name):
    """

    :param map_name:
    :return:
    """
    _location_js = _mapindex.get(map_name, "")
    _location = ""
    try:
        _location = _location_js.split(":")[0]
    except:
        pass
    return _temple_map_notebook.replace('##locationJs', _location_js).replace('##location', _location)
