# Build Context — pyecharts

> 累积的架构决策和项目上下文，供 Agent 在每个 Sprint 中参考。

## 项目概述

pyecharts 是一个 Python 可视化库，用于生成 Apache ECharts 图表。它提供：
- 简洁的 Python API，支持方法链调用
- 丰富的图表类型：基础图表、组合图表、3D 图表
- 灵活的配置系统：通过 Options 模式配置图表样式
- 多种渲染方式：HTML 文件、Notebook 嵌入、图片导出
- 暗色模式支持
- 国际化支持（中文/英文）

## 核心设计模式

### 方法链
```python
from pyecharts.charts import Bar
from pyecharts import options as opts

bar = (
    Bar()
    .add_xaxis(["A", "B", "C"])
    .add_yaxis("series", [1, 2, 3])
    .set_global_opts(title_opts=opts.TitleOpts(title="Demo"))
)
```

### Options 模式
```python
from pyecharts.options.global_options import TitleOpts
# 所有 Options 类继承 BasicOpts，内部使用 opts 字典
class TitleOpts(BasicOpts):
    def __init__(self, title="", subtitle="", ...):
        self.opts = {"title": title, "subtitle": subtitle, ...}
```

### 渲染引擎
- Jinja2 模板生成 HTML
- ECharts 选项通过 JSON 序列化嵌入
- JS 依赖通过 CDN 或本地文件加载

## 项目结构

```
pyecharts/
├── charts/                  # 图表类
│   ├── base.py              # Base 基类（所有图表的根）
│   ├── mixins.py            # ChartMixin（通用图表方法）
│   ├── basic_charts/        # 基础图表（Bar, Line, Pie, Map, Geo...）
│   ├── composite_charts/    # 组合图表（Grid, Page, Tab, Timeline）
│   └── three_axis_charts/   # 3D 图表（Bar3D, Line3D, Scatter3D, Map3D）
│
├── options/                 # 配置选项类
│   ├── global_options.py    # 全局选项（Axis, Grid, Legend, Tooltip...）
│   ├── series_options.py    # 系列选项（Label, LineStyle, AreaStyle...）
│   └── charts_options.py    # 图表特定选项（Gauge, Tree, Sunburst...）
│
├── render/                  # 渲染引擎
│   ├── engine.py            # 渲染核心逻辑
│   ├── display.py           # Notebook 显示
│   ├── snapshot.py          # 图片导出
│   └── templates/           # Jinja2 HTML 模板
│
├── commons/                 # 共享工具
├── components/              # 非图表组件（Table, Image）
├── datasets/                # 地图和地理数据
├── globals.py               # 全局配置（CurrentConfig）
├── types.py                 # 类型定义
├── faker.py                 # 测试数据生成器
├── exceptions.py            # 自定义异常
└── _version.py              # 版本号
```

## 核心组件

### Base
- 位置: `pyecharts/charts/base.py`
- 职责: 所有图表的根类，处理初始化、渲染、JS 依赖
- 关键方法: `render()`, `render_embed()`, `render_notebook()`

### ChartMixin
- 位置: `pyecharts/charts/mixins.py`
- 职责: 提供通用图表方法
- 关键方法: `set_global_opts()`, `set_series_opts()`, `add_dataset()`

### Options 体系
- 基类: `BasicOpts`（位于 `pyecharts/options/series_options.py`）
- 全局选项: `TitleOpts`, `LegendOpts`, `TooltipOpts`, `AxisOpts` 等
- 系列选项: `LabelOpts`, `LineStyleOpts`, `AreaStyleOpts`, `MarkPointOpts` 等
- 图表选项: `GaugeDetailOpts`, `TreeMapBreadcrumbOpts` 等

## 构建与测试命令

```bash
# 构建
uv build

# 单元测试
uv run pytest -v --cov-config=pyproject.toml --cov=./ test/

# Lint
make lint

# 格式化
black .
isort .
```

## 已知约束

1. Python >= 3.7 兼容性要求
2. 默认语言为中文（ZH），可切换为英文（EN）
3. JS 依赖通过 CDN 加载，离线使用需配置本地资源
4. 图片导出需要额外依赖（selenium/phantomjs/pyppeteer）
5. 部分图表类型需要额外 ECharts 扩展库

## Sprint 历史

（随着 Sprint 完成逐步填充）

| Sprint | 功能 | 日期 | 评分 |
|--------|------|------|------|
| — | 尚无 Sprint | — | — |

## 技术债务

（随着开发过程逐步记录）

| 编号 | 描述 | 优先级 | 来源 Sprint |
|------|------|--------|------------|
| — | 尚无技术债务 | — | — |
