> 地图自定义篇：考虑到项目更好的通用性，以及更好可扩展性，所以决定对地图部分提供自定义模式。适用在 pyecharts v0.1.9.7 以后的版本。

> Echarts 官方地图下载地址 [download-map](http://echarts.baidu.com/download-map.html) 已经暂时关闭

## 如何获得更多地图

自从 0.3.2 开始，为了缩减项目本身的体积以及维持 pyecharts 项目的轻量化运行，pyecharts 将不再自带地图 js 文件。如用户需要用到地图图表，可自行安装对应的地图文件包。下面介绍如何安装。

1. [全球国家地图](https://echarts-maps.github.io/echarts-countries-js/): [echarts-countries-pypkg](https://github.com/pyecharts/echarts-countries-pypkg) (1.9MB): 世界地图和 213 个国家，包括中国地图
2. [中国省级地图](https://echarts-maps.github.io/echarts-china-provinces-js/): [echarts-china-provinces-pypkg](https://github.com/pyecharts/echarts-china-provinces-pypkg) (730KB)：23 个省，5 个自治区
3. [中国市级地图](https://echarts-maps.github.io/echarts-china-cities-js/): [echarts-china-cities-pypkg](https://github.com/pyecharts/echarts-china-cities-pypkg) (3.8MB)：370 个中国城市

需要这些地图的朋友，可以装 pip 命令行:

```
pip install echarts-countries-pypkg
pip install echarts-china-provinces-pypkg
pip install echarts-china-cities-pypkg
```

特别注明，中国地图在 echarts-countries-pypkg 里。


## 如何制作自己的地图扩展

你需要做两个 github 项目：一个是 npm 项目，提供所有的 javascript 脚本；另一个是 python 项目，把前一个项目变成可以用 pip 装的 python 包。

### npm 项目

这个项目首先必须是一个 npm 的项目，并已经启动 gh-pages 来提供地图库。如果未启动 gh-pages , 那么
你的 jupyter 用户不能把 ipynb 下载成 html ，因为下载之后地图将无法显示。

首先，你需要得到以下的项目：

```
pip install yehua
git clone https://github.com/echarts-maps/echarts-js-mobans.git
export YEHUA_FILE=/ABSOLUTE/PATH/TO/echarts-js-mobans/yehua.yml
```

然后你需要移步到你的工作文件夹，以 echarts-united-kingdom-js 为例子运行这个命令

```
$ yh
Yehua will walk you through creating a echarts-maps js package.
Press ^C to quit at any time.

project name: echarts-united-kingdom-js
description: UK maps for echarts
license: MIT
author: C.W.
All done!! project echarts-united-kingdom-js is created
```

文件已经产生了，让我们看看是哪些文件：

```
pyecharts-host:tmp chfw$ cd echarts-united-kingdom-js/
pyecharts-host:echarts-united-kingdom-js chfw$ ls
echarts-united-kingdom-js	package.json			registry.json
```

现在讲原理。一个 echarts-js 包需要以下的文件结构


```
+ echarts-united-kingdom-js
  + registry.json
  + package.json
  + echarts-united-kingdom-js
     + london.js
     + manchester.js
     + index.js
  + other files
```

在 registry.json 里，需要填写的东西是和 pyecharts 衔接的必要信息。
```
{
    "JUPYTER_URL": "/nbextensions/echarts-united-kingdom-js",
    "GITHUB_URL": "https://your.github.io/echarts-united-kingdom-js/echarts-united-kingdoms-js",
    "JUPYTER_ENTRY": "echarts-united-kingdom-js/index",
    "JS_FOLDER": "echarts-united-kingdoms-js",
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

index.js 只为 jupyter notebook 而存在
```
define(["require", "exports"], function (require, exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var version = '1.0.0';
    function load_ipython_extension() {
        console.log("echarts-united-kingdom-js " + version + " has been loaded");
    }
    exports.load_ipython_extension = load_ipython_extension;
});

好了，在 echarts-united-kingdom-js 子文件夹里就需要放地图文件了。每放一个呢，请记住更新 PINYI_MAP 和 FILE_MAP。

```

### python 项目

首先，你需要得到以下的项目：

```
pip install yehua
git clone https://github.com/pyecharts/pypkg-mobans.git
export YEHUA_FILE=/ABSOLUTE/PATH/TO/pypkg-mobans/yehua.yml
```

然后你需要移步到你的工作文件夹，以 echarts-united-kingdom-pykg 为例子运行这个命令

```
$ yh
Yehua will walk you through creating a pyecharts pypkg package.
Press ^C to quit at any time.

project name: echarts-united-kingdom-pypkg
npm project name: echarts-united-kingdom-js
description: pyecharts map extension - united kingdom maps - python package
license: MIT
author: C.W.
contact email: wangc_2011@hotmail.com
github profile/organisation: chfw
copyright owner: C.W.
Cloning into 'mobans'...
remote: Counting objects: 214, done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 214 (delta 8), reused 12 (delta 5), pack-reused 198
Receiving objects: 100% (214/214), 30.31 KiB | 17.00 KiB/s, done.
Resolving deltas: 100% (126/126), done.
Templating CUSTOM_README.rst.jj2 to README.rst
Templating custom_setup.py.jj2 to setup.py
Templating requirements.txt.jj2 to requirements.txt
Templating tests/custom_requirements.txt.jj2 to tests/requirements.txt
Templating docs/source/conf.py.jj2 to docs/source/conf.py
Templating test.script.jj2 to test.sh
Templating _version.py.jj2 to echarts_united_kingdom_pypkg/_version.py
Templating gitignore.jj2 to .gitignore
Templating travis.yml.jj2 to .travis.yml
Templated 9 files.
Initialized empty Git repository in /private/tmp/echarts-united-kingdom-pypkg/.git/
Please review changes before commit!
```

这个时候，这个扩展包的骨架就已经做好了。我们现在做最后一步：


```
pyecharts-host:tmp chfw$ cd echarts-united-kingdom-pypkg/
git submodule add https://github.com/your/npm/project your_project_name_pypkg/resources
git submodule init
```

请把需要的文件加入 git, 然后做:

```
git commit
```

这样呢，这个包就可以放在 github 上了。


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

![customize-map-2](https://user-images.githubusercontent.com/19553554/35104708-9d88455a-fca4-11e7-8fb1-1aff8e0066ef.png)


