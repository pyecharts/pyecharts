> 主题自定义篇：扩展主题插件，多样化图表配色。V0.5.2+ 新增

自 0.5.2+ 起，pyecharts 支持更换主题。下面是更换为 "dark" 的例子：

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

默认主题的效果

![default](https://user-images.githubusercontent.com/19553554/39868566-c20b699e-548c-11e8-861f-5a1b063434c3.png)


## 使用主题插件

echarts 自带 `dark` 主题，pyecharts 也就自带了 `dark`。 [echarts-themes-pypkg](https://github.com/pyecharts/echarts-themes-pypkg) 主题插件提供了如下主题

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


### 安装主题插件

```shell
$ pip install echarts-themes-pypkg
```

### 使用主题

更换单个图形主题
```python
bar.use_theme("vintage")
```

更换运行环境内所有图表主题
```python
from pyecharts import configure

# 将这行代码置于首部
configure(global_theme='dark')

bar = Bar()
# 其他代码
```

## 主题风格

### vintage

![vintage](https://user-images.githubusercontent.com/19553554/39868887-1bed3ae0-548e-11e8-99f5-8440ea578080.png)

### macarons

![macarons](https://user-images.githubusercontent.com/19553554/39868570-c3563a0e-548c-11e8-9795-e0ebea18853f.png)

### infographic

![infographic](https://user-images.githubusercontent.com/19553554/39868564-c1884dac-548c-11e8-9009-f61162759be3.png)

### shine

![shine](https://user-images.githubusercontent.com/19553554/39868565-c1c8951a-548c-11e8-8351-2973cce47679.png)

### roma

![roma](https://user-images.githubusercontent.com/19553554/39868568-c2c7b798-548c-11e8-9de8-3d3ae148f172.png)

### westeros

![westeros](https://user-images.githubusercontent.com/19553554/43997578-077ff444-9e12-11e8-947b-9b37b279e99f.png)

### wonderland

![wonderland](https://user-images.githubusercontent.com/19553554/43997583-31b32b8c-9e12-11e8-8f39-4ef027e7a223.png)

### chalk

![chalk](https://user-images.githubusercontent.com/19553554/43997593-6835b652-9e12-11e8-98ff-1894c4475b5a.png)

### halloween

![halloween](https://user-images.githubusercontent.com/19553554/43997599-97fcc038-9e12-11e8-878d-0a9a538ad75e.png)

### essos

![essos](https://user-images.githubusercontent.com/19553554/43997602-c0ce6390-9e12-11e8-94ba-5215b9e2c85b.png)

### walden

![walden](https://user-images.githubusercontent.com/19553554/43997620-3868a01e-9e13-11e8-84d5-79e998051170.png)

### purple-passion

![purple-passion](https://user-images.githubusercontent.com/19553554/43997624-56ed56e2-9e13-11e8-95be-8815e1bdf0e5.png)

### romantic

![romantic](https://user-images.githubusercontent.com/19553554/44029175-eef6f170-9f2e-11e8-82cb-b60a39b28762.png)


## 使用自己构建的主题

Echarts 提供了[主题构建工具](http://echarts.baidu.com/theme-builder/)，你可以从中构建喜欢的主题，如 `myTheme.js`。然后 hack *echarts-themes-pypkg* 包。具体操作如下

1. cd 到你 Python 安装环境下的 `Lib/site-packages/echarts_themes_pypkg/resources` 目录下，具体路径因操作系统而异
2. 将 `myTheme.js` 放入到 `resources/echarts-themes-js` 文件夹下
3. 改动 `resources/registry.json` 文件

```
 "PINYIN_MAP": {
        "shine": "shine",
        ...
        "myTheme": "myTheme"    # 这行
    },
    "FILE_MAP": {
        "shine": "shine",
        ...
        "myTheme": "myTheme"    # 还有这行
    }
```
4. cd 到 notebook 安装环境下的 `jupyter/nbextensions/echarts-themes-js` 目录下，具体路径因操作系统而异
5. 将 `myTheme.js` 放入到 `echarts-themes-js` 文件夹下
6. 使用 `chart.use_theme("myTheme")`

**4、5 为可选项，如果不使用 notebook 的话可以忽略该步骤。**