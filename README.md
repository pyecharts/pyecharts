<p align="center">
    <img src="https://user-images.githubusercontent.com/19553554/71825144-2d568180-30d6-11ea-8ee0-63c849cfd934.png" alt="pyecharts logo" width=200 height=200 />
</p>
<h1 align="center">pyecharts</h1>
<p align="center">
    <em>Python ❤️ Echarts = pyecharts</em>
</p>
<p align="center">
    <a href="https://travis-ci.org/pyecharts/pyecharts">
        <img src="https://travis-ci.org/pyecharts/pyecharts.svg?branch=master" alt="Travis Build Status">
    </a>
    <a href="https://ci.appveyor.com/project/chenjiandongx/pyecharts">
        <img src="https://ci.appveyor.com/api/projects/status/81cbsfjpfryv1cl8/branch/master?svg=true" alt="Appveyor Build Status">
    </a>
    <a href="https://codecov.io/gh/pyecharts/pyecharts">
        <img src="https://codecov.io/gh/pyecharts/pyecharts/branch/master/graph/badge.svg" alt="Codecov">
    </a>
    <a href="https://badge.fury.io/py/pyecharts">
        <img src="https://badge.fury.io/py/pyecharts.svg" alt="Package version">
    </a>
    <a href="https://pypi.org/project/pyecharts/">
        <img src="https://img.shields.io/pypi/pyversions/pyecharts.svg?colorB=brightgreen" alt="PyPI - Python Version">
    </a>
</p>
<p align="center">
    <a href="https://pypi.org/project/pyecharts">
        <img src="https://img.shields.io/pypi/format/pyecharts.svg" alt="PyPI - Format">
    </a>
     <a href="https://github.com/pyecharts/pyecharts/pulls">
        <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions welcome">
    </a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" alt="License">
    </a>
</p>

[English README](README.en.md)

## 📣 简介

[Echarts](https://github.com/ecomfe/echarts) 是一个由百度开源的数据可视化，凭借着良好的交互性，精巧的图表设计，得到了众多开发者的认可。而 Python 是一门富有表达力的语言，很适合用于数据处理。当数据分析遇上数据可视化时，[pyecharts](https://github.com/pyecharts/pyecharts) 诞生了。

## ✨ 特性

* 简洁的 API 设计，使用如丝滑般流畅，支持链式调用
* 囊括了 30+ 种常见图表，应有尽有
* 支持主流 Notebook 环境，Jupyter Notebook 和 JupyterLab
* 可轻松集成至 Flask，Sanic，Django 等主流 Web 框架
* 高度灵活的配置项，可轻松搭配出精美的图表
* 详细的文档和示例，帮助开发者更快的上手项目
* 多达 400+ 地图文件，并且支持原生百度地图，为地理数据可视化提供强有力的支持

## ⏳ 版本

v0.5.x 和 V1 间不兼容，V1 是一个全新的版本，详见 [ISSUE#892](https://github.com/pyecharts/pyecharts/issues/892)，[ISSUE#1033](https://github.com/pyecharts/pyecharts/issues/1033)。

### V0.5.x

> 支持 Python2.7，3.4+

经开发团队决定，0.5.x 版本将不再进行维护，0.5.x 版本代码位于 *05x* 分支，文档位于 [05x-docs.pyecharts.org](http://05x-docs.pyecharts.org)。

### V1

> 仅支持 Python3.6+

新版本系列将从 v1.0.0 开始，文档位于 [pyecharts.org](https://pyecharts.org)；示例位于 [gallery.pyecharts.org](https://gallery.pyecharts.org)

## 🔰 安装

**pip 安装**
```shell
# 安装 v1 以上版本
$ pip install pyecharts -U

# 如果需要安装 0.5.11 版本的开发者，可以使用
# pip install pyecharts==0.5.11
```

**源码安装**
```shell
# 安装 v1 以上版本
$ git clone https://github.com/pyecharts/pyecharts.git
# 如果需要安装 0.5.11 版本，请使用 git clone https://github.com/pyecharts/pyecharts.git -b v05x
$ cd pyecharts
$ pip install -r requirements.txt
$ python setup.py install
```

## 📝 使用

### 本地环境

#### 生成 HTML
```python
from pyecharts.charts import Bar
from pyecharts import options as opts

# V1 版本开始支持链式调用
bar = (
    Bar()
    .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
    .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
    .set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
)
bar.render()

# 不习惯链式调用的开发者依旧可以单独调用方法
bar = Bar()
bar.add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
bar.set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
bar.render()
```
<p align="center">
<img src="https://user-images.githubusercontent.com/19553554/55270272-d6ff1b80-52d7-11e9-820f-30660a068e3e.gif"  width="85%" />
</p>

#### 生成图片
```python
from snapshot_selenium import snapshot as driver

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.render import make_snapshot


def bar_chart() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
        .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-测试渲染图片"))
    )
    return c

# 需要安装 snapshot-selenium 或者 snapshot-phantomjs
make_snapshot(driver, bar_chart().render(), "bar.png")
```
<p align="center">
<img src="https://user-images.githubusercontent.com/19553554/56089096-11fc7400-5ec0-11e9-9c21-551624036836.png"  width="85%" />
</p>

### Notebook 环境

#### Jupyter Notebook

![](https://user-images.githubusercontent.com/19553554/55270255-b3d46c00-52d7-11e9-8aa5-f7b3819a1e88.png)

#### JupyterLab

![](https://user-images.githubusercontent.com/19553554/55270259-c0f15b00-52d7-11e9-8811-93bfca1cc027.png)

#### Web 框架

![](https://user-images.githubusercontent.com/19553554/35081158-3faa7c34-fc4d-11e7-80c9-2de79371374f.gif)

## 🔖 Demo

> Demo 代码位于 example 文件夹下，欢迎参考 pyecharts 画廊 [pyecharts-gallery](https://github.com/pyecharts/pyecharts-gallery)。

<div align="center">
<img src="https://user-images.githubusercontent.com/19553554/52197440-843a5200-289a-11e9-8601-3ce8d945b04a.gif" width="33%" alt="bar"/>
<img src="https://user-images.githubusercontent.com/19553554/52360729-ad640980-2a77-11e9-84e2-feff7e11aea5.gif" width="33%" alt="boxplot"/>
<img src="https://user-images.githubusercontent.com/19553554/52535290-4b611800-2d87-11e9-8bf2-b43a54a3bda8.png" width="33%" alt="effectScatter"/>
<img src="https://user-images.githubusercontent.com/19553554/52332816-ac5eb800-2a36-11e9-8227-3538976f447d.gif" width="33%" alt="funnel"/>
<img src="https://user-images.githubusercontent.com/19553554/52332988-0b243180-2a37-11e9-9db8-eb6b8c86a0de.png" width="33%" alt="gague"/>
<img src="https://user-images.githubusercontent.com/19553554/52344575-133f9980-2a56-11e9-93e0-568e484936ce.gif" width="33%" alt="geo"/>
<img src="https://user-images.githubusercontent.com/19553554/35082102-fd8d884a-fc52-11e7-9e40-5f94098d4493.gif" width="33%" alt="geo"/>
<img src="https://user-images.githubusercontent.com/19553554/52727805-f7f20280-2ff0-11e9-91ab-cd99848e3127.gif" width="33%" alt="graph"/>
<img src="https://user-images.githubusercontent.com/19553554/52345115-6534ef00-2a57-11e9-80cd-9cbfed252139.gif" width="33%" alt="heatmap"/>
<img src="https://user-images.githubusercontent.com/19553554/52345490-4a16af00-2a58-11e9-9b43-7bbc86aa05b6.gif" width="33%" alt="kline"/>
<img src="https://user-images.githubusercontent.com/19553554/52346064-b7770f80-2a59-11e9-9e03-6dae3a8c637d.gif" width="33%" alt="line"/>
<img src="https://user-images.githubusercontent.com/19553554/52347117-248ba480-2a5c-11e9-8402-5a94054dca50.gif" width="33%" alt="liquid"/>
<img src="https://user-images.githubusercontent.com/19553554/52347915-0a52c600-2a5e-11e9-8039-41268238576c.gif" width="33%" alt="map"/>
<img src="https://user-images.githubusercontent.com/19553554/57545910-431c7700-738e-11e9-896b-e071b55115c7.png" width="33%" alt="bmap"/>
<img src="https://user-images.githubusercontent.com/19553554/52535013-e48e2f80-2d83-11e9-8886-ac0d2122d6af.png" width="33%" alt="parallel"/>
<img src="https://user-images.githubusercontent.com/19553554/52348202-bb596080-2a5e-11e9-84a7-60732be0743a.gif" width="33%" alt="pie"/>
<img src="https://user-images.githubusercontent.com/19553554/35090457-afc0658e-fc74-11e7-9c58-24c780436287.gif" width="33%" alt="ploar"/>
<img src="https://user-images.githubusercontent.com/19553554/52533994-932b7380-2d76-11e9-93b4-0de3132eb941.gif" width="33%" alt="radar"/>
<img src="https://user-images.githubusercontent.com/19553554/52348431-420e3d80-2a5f-11e9-8cab-7b415592dc77.gif" width="33%" alt="scatter"/>
<img src="https://user-images.githubusercontent.com/19553554/44004598-5636d74e-9e97-11e8-8a5c-92de6278880d.gif" width="33%" alt="tree"/>
<img src="https://user-images.githubusercontent.com/19553554/35082251-b9e23982-fc53-11e7-8341-e7da1842389f.gif" width="33%" alt="treemap"/>
<img src="https://user-images.githubusercontent.com/19553554/52348737-01fb8a80-2a60-11e9-94ac-dacbd7b58811.png" width="33%" alt="wordCloud"/>
<img src="https://user-images.githubusercontent.com/19553554/52433989-4f075b80-2b49-11e9-9979-ef32c2d17c96.gif" width="33%" alt="bar3D"/>
<img src="https://user-images.githubusercontent.com/19553554/52464826-4baab900-2bb7-11e9-8299-776f5ee43670.gif" width="33%" alt="line3D"/>
<img src="https://user-images.githubusercontent.com/19553554/52802261-8d0cfe00-30ba-11e9-8ae7-ae0773770a59.gif" width="33%" alt="sankey"/>
<img src="https://user-images.githubusercontent.com/19553554/52464647-aee81b80-2bb6-11e9-864e-c544392e523a.gif" width="33%" alt="scatter3D"/>
<img src="https://user-images.githubusercontent.com/19553554/52465183-a55fb300-2bb8-11e9-8c10-4519c4e3f758.gif" width="33%" alt="surface3D"/>
<img src="https://user-images.githubusercontent.com/19553554/52798246-7ebae400-30b2-11e9-8489-6c10339c3429.gif" width="33%" alt="themeRiver"/>
<img src="https://user-images.githubusercontent.com/17564655/57567164-bdd5a880-7407-11e9-8d19-9be2776c57fa.png" width="33%" alt="sunburst"/>
<img src="https://user-images.githubusercontent.com/19553554/52349544-c2ce3900-2a61-11e9-82af-28aaaaae0d67.gif" width="33%" alt="overlap"/>
<img src="https://user-images.githubusercontent.com/19553554/35089737-ccc1c01c-fc72-11e7-874d-8ba8b89572eb.png" width="33%" alt="grid"/>
<img src="https://user-images.githubusercontent.com/19553554/56976071-b9f28c80-6ba4-11e9-8efd-603203c77619.png" width="33%" alt="grid">
<img src="https://user-images.githubusercontent.com/19553554/35082279-e111743c-fc53-11e7-9362-580160593715.gif" width="33%" alt="timeline"/>
</div>

更多详细文档，请访问

* [中文文档](http://pyecharts.org/#/zh-cn/)
* [English Documentation](http://pyecharts.org/#/en-us/)
* [示例 Example](https://gallery.pyecharts.org)

## ⛏ 代码质量

### 单元测试

```shell
$ pip install -r test/requirements.txt
$ make
```

### 集成测试

使用 [Travis CI](https://travis-ci.org/) 和 [AppVeyor](https://ci.appveyor.com/) 持续集成环境。

### 代码规范

使用 [flake8](http://flake8.pycqa.org/en/latest/index.html), [Codecov](https://codecov.io/) 以及 [pylint](https://www.pylint.org/) 提升代码质量。

## 😉 Author

pyecharts 主要由以下几位开发者开发维护

* [@chenjiandongx](https://github.com/chenjiandongx)
* [@chfw](https://github.com/chfw)
* [@kinegratii](https://github.com/kinegratii)
* [@sunhailin-Leo](https://github.com/sunhailin-Leo)

更多贡献者信息可以访问 [pyecharts/graphs/contributors](https://github.com/pyecharts/pyecharts/graphs/contributors)

## 💌 捐赠

开发和维护 pyecharts 花费了我巨大的心力，如果你觉得项目帮助到您，请认真考虑请作者喝一杯咖啡 😄

<img src="https://user-images.githubusercontent.com/19553554/35425853-500d6b5c-0299-11e8-80a1-ebb6629b497e.png" width="21.7%" alt="Alipay">　　　　　<img src="https://user-images.githubusercontent.com/19553554/35425854-504e716a-0299-11e8-81fc-4a511f1c47e8.png" width="22%" alt="Wechat">


如果其他开发者帮助到了您，也可以请他们喝咖啡 [捐赠通道](http://pyecharts.org/#/zh-cn/donate)

## 💡 贡献

期待能有更多的开发者参与到 pyecharts 的开发中来，我们会保证尽快 Reivew PR 并且及时回复。但提交 PR 请确保

1. 通过所有单元测试，如若是新功能，请为其新增单元测试
2. 遵守开发规范，使用 black 以及 isort 格式化代码（$ pip install -r requirements-dev.txt）
3. 如若需要，请更新相对应的文档

我们也非常欢迎开发者能为 pyecharts 提供更多的示例，共同来完善文档，文档项目位于 [pyecharts/website](https://github.com/pyecharts/website)

## 📃 License

MIT [©chenjiandongx](https://github.com/chenjiandongx)
