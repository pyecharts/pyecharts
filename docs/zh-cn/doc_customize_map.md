> 考虑到项目更好的通用性，以及更好可扩展性，所以决定对地图部分提供自定义模式。适用在pyecharts 0.1.9.7 以后的版本。

## 下载地图

这里是 Echarts 官方地图下载地址 [download-map](http://echarts.baidu.com/download-map.html)

![customize-map-0](https://raw.githubusercontent.com/chenjiandongx/pyecharts/master/images/customize-map-0.png)

除了官方提供的主要省份的地图，还可根据自己的需求自定义。

![customize-map-1](https://raw.githubusercontent.com/chenjiandongx/pyecharts/master/images/customize-map-1.png)

所有地图均要下载成 JS 格式。

请注意：

* 地图名称千万要把beijing变成中文的城市名称
* 2.2.0 之后，[363个二线城市地图](https://github.com/chfw/echarts-china-cities-js#featuring-citiesor-for-single-download)已经内嵌了，无需下载。


## 如何手动添加(0.1.9.7+)
下面就以广东省汕头市南澳县地图为例，说明如何自行添加地图。

### 保存地图文件
先下载南澳县地图的 JS 文件，请更名为 nanao.js。将其保存在项目安装目录下的 templates/js/echarts 文件夹中。Windows 下一般为 Lib/site-packages/pyecharts/templates/js/echarts

然后呢，在你的代码里需要加下面的两行

```
import pyecharts.constants as constants

constants.CITY_NAME_PINYIN_MAP['南澳县'] = 'nanao'
```

请注意格式：关键词是“南澳县”，对应的文件名是"nanao"， 并且不加'js'后缀。下面是所有的代码

```python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Map
import pyecharts.constants as constants

constants.CITY_NAME_PINYIN_MAP['南澳县']='nanao'

value = []
attr = []
map = Map("南澳县地图示例", width=1200, height=600)
map.add("", attr, value, maptype='南澳县', is_visualmap=True, visual_text_color='#000')
map.render()
```

如果只是使用 render() 生成 .html 文件的话到这里就可以了。还想要在 jupyter-notebook 上展示地图的话，还需要下面一个步骤。

```
$ jupyter nbextensions install --user [python lib dir]/site-packages/pyecharts/templates/js/echarts
...
Copying: .../echarts/nanao.js -> /.../jupyter/nbextensions/echarts/nanao.js
...
    To initialize this nbextension in the browser every time the notebook (or other app) loads:

          jupyter nbextension enable <the entry point>
```

请特别注意，`[python lib dir]/site-packages/pyecharts/templates/js/echarts`路径后面不加`/`.

你可以选择性的执行下面的语句。如果你已经装了 0.1.9.7+ 在你现在的 Python 环境，就可以跳过

```
jupyter nbextension enable echarts/main
```

然后，让我们检查以下是否已经装上了。请先运行 Jupyter-notebook，再打开这个链接：http://localhost:8889/nbextensions/echarts/nanao.js。
如果能下载到，那就祝贺你，成功了。否则，请检查你的步骤。

![customize-map-2](https://raw.githubusercontent.com/chenjiandongx/pyecharts/master/images/customize-map-2.png)

## 如何把手动加的地图变成自动的

如果用户期望 pyecharts 支持自己的地图，请发请求然后再发来改动。
