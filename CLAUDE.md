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
