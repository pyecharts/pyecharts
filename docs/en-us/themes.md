> Theme customization: Expand the theme plugin, diversified chart color matching. V0.5.2+ added

Since 0.5.2+, pyecharts has supported the replacement of themes. The following is an example of replacing with "dark":

```python
import random

from pyecharts import Bar


X_AXIS = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
bar = Bar("我的第一个图表", "这里是副标题")
bar.use_theme("dark")
bar.add("商家A", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家B", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家C", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家D", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.render()
```
![dark](https://user-images.githubusercontent.com/19553554/39868563-c136646a-548c-11e8-87c2-dbf7ae85e844.png)

Default theme effect

![default](https://user-images.githubusercontent.com/19553554/39868566-c20b699e-548c-11e8-861f-5a1b063434c3.png)


## Theme plugins usage

ECharts comes with the `dark` theme, and pyecharts comes with `dark`.  
[echarts-themes-pypkg](https://github.com/pyecharts/echarts-themes-pypkg) theme plugin provides the following topics :  

* [vintage](#vintage)
* [macarons](#macarons)
* [infographic](#infographic)
* [shine](#shine)
* [roma](#roma)
* [westeros](#westeros)
* [wonderland](#wonderland)
* [chalk](#chalk)
* [halloween](#halloween)
* [essos](#essos)
* [walden](#walden)
* [purple-passion](#purple-passion)
* [romantic](#romantic)

### Installing theme plugin

```shell
$ pip install echarts-themes-pypkg
```

### Theme usage

Replace a single graphic theme
```python
bar.use_theme("vintage")
```

Replace all chart topics in the operating environment
```python
from pyecharts import configure

# Put this line of code in the header
configure(global_theme='dark')

bar = Bar()
# other code
```

### Example

#### vintage

![vintage](https://user-images.githubusercontent.com/19553554/39868887-1bed3ae0-548e-11e8-99f5-8440ea578080.png)

#### macarons

![macarons](https://user-images.githubusercontent.com/19553554/39868570-c3563a0e-548c-11e8-9795-e0ebea18853f.png)

#### infographic

![infographic](https://user-images.githubusercontent.com/19553554/39868564-c1884dac-548c-11e8-9009-f61162759be3.png)

#### shine

![shine](https://user-images.githubusercontent.com/19553554/39868565-c1c8951a-548c-11e8-8351-2973cce47679.png)

#### roma

![roma](https://user-images.githubusercontent.com/19553554/39868568-c2c7b798-548c-11e8-9de8-3d3ae148f172.png)

#### westeros

![westeros](https://user-images.githubusercontent.com/19553554/43997578-077ff444-9e12-11e8-947b-9b37b279e99f.png)

#### wonderland

![wonderland](https://user-images.githubusercontent.com/19553554/43997583-31b32b8c-9e12-11e8-8f39-4ef027e7a223.png)

#### chalk

![chalk](https://user-images.githubusercontent.com/19553554/43997593-6835b652-9e12-11e8-98ff-1894c4475b5a.png)

#### halloween

![halloween](https://user-images.githubusercontent.com/19553554/43997599-97fcc038-9e12-11e8-878d-0a9a538ad75e.png)

#### essos

![essos](https://user-images.githubusercontent.com/19553554/43997602-c0ce6390-9e12-11e8-94ba-5215b9e2c85b.png)

#### walden

![walden](https://user-images.githubusercontent.com/19553554/43997620-3868a01e-9e13-11e8-84d5-79e998051170.png)

#### purple-passion

![purple-passion](https://user-images.githubusercontent.com/19553554/43997624-56ed56e2-9e13-11e8-95be-8815e1bdf0e5.png)

#### romantic

![romantic](https://user-images.githubusercontent.com/19553554/44029175-eef6f170-9f2e-11e8-82cb-b60a39b28762.png)


## Use your own built theme

ECharts provides [Theme Build Tools](http://echarts.baidu.com/theme-builder/), from which you can build favorite themes like `myTheme.js`. Then hack the *echarts-themes-pypkg* package. The specific operation is as follows

1. cd to your Python installation environment `Lib/site-packages/echarts_themes_pypkg/resources`. The specific path varies by operating system
2. Move `myTheme.js` to `resources/echarts-themes-js` folder
3. Change the `resources/registry.json` file

```
"PINYIN_MAP": {
        "shine": "shine",
        ...
        "myTheme": "myTheme"    # here
    },
    "FILE_MAP": {
        "shine": "shine",
        ...
        "myTheme": "myTheme"    # and here
    }
```
4. cd to `jupyter/nbextensions/echarts-themes-js` directory in the notebook installation environment, the specific path varies by operating system
5. Move `myTheme.js` to `echarts-themes-js` folder
6. Use `chart.use_theme("myTheme")`

**4、5 as options, you can ignore this step if you don't use a notebook.**
