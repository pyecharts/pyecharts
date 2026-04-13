# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

pyecharts is a Python visualization library that generates Apache ECharts charts. It provides a simple API with method chaining support for creating interactive charts.

## Build, Test, and Lint Commands

```bash
# Run all tests
make test
# or
pytest -v --cov-config=pyproject.toml --cov=./ test/

# Run a single test file
pytest test/test_chart.py

# Run a specific test method
pytest test/test_chart.py::TestChartClass::test_chart_dark_mode

# Run linter
make lint
# or
flake8 --exclude=build,images,example,examples,.venv --max-line-length=89 --ignore=F401,F824

# Format code
black .
isort .

# Build package
make build
# or
uv build
```

## Architecture Overview

### Package Structure

- **`pyecharts/charts/`**: Chart classes organized by type
  - `basic_charts/`: Bar, Line, Pie, Map, Geo, Graph, etc.
  - `composite_charts/`: Grid, Page, Tab, Timeline
  - `three_axis_charts/`: Bar3D, Line3D, Scatter3D, Map3D
- **`pyecharts/options/`**: Configuration option classes
  - `global_options.py`: Axis, Grid, Legend, Tooltip, etc.
  - `series_options.py`: Label, LineStyle, AreaStyle, MarkPoint, etc.
  - `charts_options.py`: Chart-specific options (Gauge, Tree, Sunburst, etc.)
- **`pyecharts/render/`**: Rendering engine for HTML, Notebook, and image output
- **`pyecharts/commons/`**: Shared utilities
- **`pyecharts/components/`**: Non-chart components (Table, Image)
- **`pyecharts/datasets/`**: Map and geographic data

### Core Classes

- **`Base`** (`pyecharts/charts/base.py`): Root class for all charts, handles initialization, rendering, and JavaScript dependencies
- **`ChartMixin`** (`pyecharts/charts/mixins.py`): Provides common chart methods
- **Option classes**: All use `BasicOpts` base class with `opts` dict pattern

### Key Patterns

1. **Method chaining**: All chart modification methods return `self`
2. **Options pattern**: Configuration via dataclass-like opts (e.g., `opts.TitleOpts(title="...")`)
3. **Import convention**: `from pyecharts import options as opts`
4. **Rendering**: Uses Jinja2 templates with JSON-serialized options

### JavaScript Dependencies

Charts declare JS dependencies via `js_dependencies` attribute (default: "echarts"). Additional libraries like "echarts-stat" can be added dynamically.

## Additional Notes

- Default locale is Chinese (ZH); configurable via `CurrentConfig`
- Charts support dark mode via `set_dark_mode()` method
- The project uses `uv` for dependency management
- `AGENTS.md` contains additional detailed code style guidelines

---

## Harness 开发模式

> **重要**：本项目采用 Harness 开发模式管理所有功能开发的完整生命周期。

### 强制启动仪式

收到任何涉及 **sprint / harness / 合约 / 评估 / 需求开发** 的任务时，或修改 `pyecharts/`、`test/`、`examples/` 路径下的代码时，**必须先读取以下 3 个文件**：

```bash
read_file .harness/README.md
read_file .harness/prompts/generator.md
read_file .harness/prompts/evaluator.md
```

### 三 Agent 架构执行顺序

```
Step 1: [Planner]    需求分析 → 扩展为完整技术规格
Step 2: [Generator]  写 sprint-N-contract.md（合约先行）
Step 3: [Evaluator]  独立审查合约（sub agent，怀疑视角）
Step 4: ⏸️ 用户确认   与用户讨论合约，等待用户确认
Step 5: [Generator]  实现代码
Step 6: ⚠️ 全量回归   uv run pytest -v --cov-config=pyproject.toml --cov=./ test/
Step 7: [Evaluator]  执行评估脚本 + 独立代码审查
Step 8: 评分判定     ≥ 90 → 继续；< 90 → 修复后重跑（最多 3 轮）
```

### 关键约束

- **禁止跳过合约阶段**：必须先写合约、经 Evaluator 审查、用户确认后才能实现
- **禁止"就近验证"**：回归测试必须跑全量 `uv run pytest -v --cov-config=pyproject.toml --cov=./ test/`，禁止只跑修改涉及的文件
- **评分通过阈值**：90 分（满分 100）
- **独立 Evaluator**：使用 sub agent 以怀疑论者视角独立审查，不受 Generator 自评影响

### 豁免场景

以下场景不触发 Harness：
- 纯文档修改（`.md` 文件）
- 配置文件调整（`.gitignore`、`pyproject.toml` 等）
- CI/CD 脚本修改
- 纯重构（不改变外部行为）

### Harness 文件结构

详见 `.harness/README.md`。
