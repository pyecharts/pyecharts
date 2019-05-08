<p align="center">
    <img src="https://user-images.githubusercontent.com/19553554/39612358-499eb2ae-4f91-11e8-8f56-179c4f0bf2df.png" alt="pyecharts logo" width=200 height=200 />
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

## 📣 Introduction

[Echarts](https://github.com/ecomfe/echarts) is easy-to-use, highly interactive and highly performant javascript visualization library under Apache license. Since its first public release in 2013, it now dominates over 74% of Chinese web front-end market. Yet Python is an expressive language and is loved by data science community. Combining the strength of both technologies, [pyecharts](https://github.com/pyecharts/pyecharts) is born.

## ✨ Feature hightlights

* Simple API, Sleek and method chaining
* Support 30 + popular charts
* Suppot data science tools: Jupyter Notebook, JupyterLab, nteract
* Integrate with Flask，Django at ease
* Easy to use and highly configurable
* Detialed documentation and examples.
* More than 400+ geomaps assets for geograpic information processing

## 🔰 Installation

**pip install**
```shell
$ pip install pyecharts
```

**Install from source**
```shell
$ git clone https://github.com/pyecharts/pyecharts.git
$ cd pyecharts
$ pip install -r requirements.txt
$ python setup.py install
```

## 📝 Usage

### Local computer

#### HTML
```python
from pyecharts.charts import Bar
from pyecharts import options as opts

bar = (
    Bar()
    .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
    .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
    .set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
)
bar.render()
```
<p align="center">
<img src="https://user-images.githubusercontent.com/19553554/55270272-d6ff1b80-52d7-11e9-820f-30660a068e3e.gif"  width="85%" />
</p>

#### image
```python
from pyecharts.render import make_snapshot

# needs to configure selenium
make_snapshot(bar.render(), "bar.png")
```
<p align="center">
<img src="https://user-images.githubusercontent.com/19553554/55270432-7a9cfb80-52d9-11e9-81b5-4ceb4dcd1756.png"  width="85%" />
</p>

### Notebook

#### Jupyter Notebook

![](https://user-images.githubusercontent.com/19553554/55270255-b3d46c00-52d7-11e9-8aa5-f7b3819a1e88.png)

#### JupyterLab

![](https://user-images.githubusercontent.com/19553554/55270259-c0f15b00-52d7-11e9-8811-93bfca1cc027.png)

#### Web framework

![](https://user-images.githubusercontent.com/19553554/35081158-3faa7c34-fc4d-11e7-80c9-2de79371374f.gif)

## 🔖 Demo

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
<img src="https://user-images.githubusercontent.com/19553554/52349544-c2ce3900-2a61-11e9-82af-28aaaaae0d67.gif" width="33%" alt="overlap"/>
<img src="https://user-images.githubusercontent.com/19553554/35089737-ccc1c01c-fc72-11e7-874d-8ba8b89572eb.png" width="33%" alt="grid"/>
<img src="https://user-images.githubusercontent.com/19553554/35082279-e111743c-fc53-11e7-9362-580160593715.gif" width="33%" alt="timeline"/>
</div>

For more documentaiton, please visit

* [Chinese documentation](http://pyecharts.org/#/zh-cn/)
* [English Documentation](http://pyecharts.org/#/en-us/)

## ⛏ Software development

### Unit tests

```shell
$ pip install -r test/requirements.txt
$ make
```

### Team development

[Travis CI](https://travis-ci.org/) and [AppVeyor](https://ci.appveyor.com/) is place for continuous integration.

### Coding styles

[flake8](http://flake8.pycqa.org/en/latest/index.html), [Codecov](https://codecov.io/) and [pylint](https://www.pylint.org/) are used

## 😉 Author

pyecharts are co-maintained by:

* [@chenjiandongx](https://github.com/chenjiandongx)
* [@chfw](https://github.com/chfw)
* [@kinegratii](https://github.com/kinegratii)

For more contributors, please visit [pyecharts/graphs/contributors](https://github.com/pyecharts/pyecharts/graphs/contributors)

## 💌 Donation

To develop and maintain pyecharts, it took me a lot of overnights. If you think pyecharts has helped you, please consider buying me a coffee:

<img src="https://user-images.githubusercontent.com/19553554/35425853-500d6b5c-0299-11e8-80a1-ebb6629b497e.png" width="19.8%" alt="Alipay">　　　<img src="https://user-images.githubusercontent.com/19553554/35425854-504e716a-0299-11e8-81fc-4a511f1c47e8.png" width="20%" alt="Wechat">


Please also buy the other maintainer a coffee if you think their work helped you too [donation details](http://pyecharts.org/#/zh-cn/donate)

## 📃 License

MIT [©chenjiandongx](https://github.com/chenjiandongx)
