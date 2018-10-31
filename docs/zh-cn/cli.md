> pye-CLI 篇： pyecharts 开发工具。

## 概述

从 pyecharts v0.6.0 开始，新增用于基于命令的开发工具 *pye-CLI*，这些命令均类似于下面的形式：

```shell
$ pye_cli <COMMAND> <param1> <param2>
```

## Jupyter_install : 安装地图数据插件

pyecharts 默认提供了一系列 js 格式的地图数据文件，这些文件按照分类被打包到多个 Python 包（插件）。可以使用 pip 安装这些包到本地 Python 环境，即 *site-packages* 目录下之下。

```shell
$ pip install jupyter-echarts-pypkg
```

类似地，命令 `jupyter_install` 将数据包安装到所在的 jupyter 环境中，目前该命令只读取本地包，即需要先行使用 pip 安装。

```shell
$ pye_cli jupyter_install jupyter-echarts-pypkg
```

目前仅支持以下数据包：

- jupyter-echarts-pypkg
- echarts-themes-pypkg
- echarts-cities-pypkg
- echarts-china-counties-pypkg
- echarts-china-provinces-pypkg
- echarts-coutries-pypkg
- echarts-china-misc-pypkg
- echarts-china-cities-pypkg
- echarts-united-kingdom-pypkg