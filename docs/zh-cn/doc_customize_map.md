> 地图自定义篇：考虑到项目更好的通用性，以及更好可扩展性，所以决定对地图部分提供自定义模式。适用在 pyecharts v0.1.9.7 以后的版本。

> Echarts 官方地图下载地址 [download-map](http://echarts.baidu.com/download-map.html) 已经暂时关闭

## 如何获得更多地图

自从 0.3.2 开始，[世界各国的地图](https://github.com/pyecharts/echarts-countries-js)变成了可选地图。需要这些地图的朋友，可以装 pyecharts-cli 命令行:

```
pip install pyecharts-cli
```

然后再装世界地图:

```
pyecharts-cli install echarts-countries-js
```

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

或者自己开发pyecharts的地图扩展


## pyecharts 的地图扩展

首先，地图扩展必须是一个 github 的项目，并已经启动 gh-pages 来提供地图库。如果未启动 gh-pages , 那么
你的 jupyter 用户不能把 ipynb 下载成 html ，因为下载之后地图将无法显示。

需要是这样一个结构：

```
+ your-map-extension-js
  + registry.json
  + your-map-extension-js
     + london.js
     + manchester.js
     + index.js
  + other files
```

在 registry.json 里，需要填写这些项目:
```
{
    "JUPYTER_URL": "/nbextensions/your-map-extension-js",
    "GITHUB_URL": "https://your.github.io/your-map-extension-js/your-map-extensions-js",
    "JUPYTER_ENTRY": "your-map-extension-js/index",
    "JS_FOLDER": "your-map-extensions-js",
    "PINYIN_MAP": {
        "伦敦": "lundun",
        "曼彻斯特": "manqiesite"
    },
    "FILE_MAP": {
        "lundun": "london",
        "manqiesite": "manchester"
    }
}
```

index.js 可以是这样：
```
define(["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var version = '1.0.0';
    function load_ipython_extension() {
        console.log("your-map-extension-js " + version + " has been loaded");
    }
    exports.load_ipython_extension = load_ipython_extension;
});

```

最后，就是通知我们把你的扩展加入 pyecharts-cli 的目录，方便你和其他人装你的地图扩展。
