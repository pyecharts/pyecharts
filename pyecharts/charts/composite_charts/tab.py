import uuid

from jinja2 import Environment

from ... import types
from ...commons import utils
from ...globals import CurrentConfig, ThemeType
from ...options.charts_options import TabChartGlobalOpts
from ...render import engine
from ..mixins import CompositeMixin


DEFAULT_TAB_CSS: str = """
.chart-container {
    display: block;
}

.chart-container:nth-child(n+2) {
    display: none;
}

.tab {
    overflow: hidden;
    border: 1px solid #ccc;
    background-color: #f1f1f1;
}

"""
DEFAULT_TAB_BUTTON_CSS: str = """
.tab button {
    background-color: inherit;
    float: left;
    border: none;
    outline: none;
    cursor: pointer;
    padding: 12px 16px;
    transition: 0.3s;
}

"""
DEFAULT_TAB_BUTTON_HOVER_CSS: str = """
.tab button:hover {
    background-color: #ddd;
}

"""
DEFAULT_TAB_BUTTON_ACTIVE_CSS: str = """
.tab button.active {
    background-color: #ccc;
}

"""


class Tab(CompositeMixin):
    def __init__(
        self,
        page_title: str = CurrentConfig.PAGE_TITLE,
        js_host: str = "",
        bg_color: str = "",
        tab_css_opts: TabChartGlobalOpts = TabChartGlobalOpts(),
    ):
        self.js_host: str = js_host or CurrentConfig.ONLINE_HOST
        self.page_title: str = page_title
        self.bg_color = bg_color
        self.download_button: bool = False
        self.use_custom_tab_css = tab_css_opts.opts.get("enable")
        self.tab_custom_css = self._prepare_tab_css(css_opts=tab_css_opts)
        self.js_functions: utils.OrderedSet = utils.OrderedSet()
        self.js_dependencies: utils.OrderedSet = utils.OrderedSet()
        self._charts: list = []

    def add(self, chart, tab_name):
        chart.tab_name = tab_name
        self._charts.append(chart)
        for d in chart.js_dependencies.items:
            self.js_dependencies.add(d)
        return self

    def _prepare_tab_css(self, css_opts: TabChartGlobalOpts) -> str:
        result = ""
        if isinstance(css_opts, TabChartGlobalOpts):
            css_opts = css_opts.opts
        css_opts = utils.remove_key_with_none_value(css_opts)

        def _dict_to_str(opts: dict, key: str, css_selector: str) -> str:
            _inner_result = ""
            for k, v in opts.get(key, dict()).items():
                _inner_result += "{}:{}; ".format(k, v)
            return (
                f"{css_selector} " + "{ " + _inner_result + " }\n"
                if _inner_result != ""
                else ""
            )

        # .tab
        tab_base = _dict_to_str(opts=css_opts, key="base", css_selector=".tab")
        result += tab_base if tab_base != "" else DEFAULT_TAB_CSS
        # .tab button
        tab_button_base = _dict_to_str(
            opts=css_opts, key="button_base", css_selector=".tab button"
        )
        result += tab_button_base if tab_button_base != "" else DEFAULT_TAB_BUTTON_CSS
        # .tab button:hover
        tab_button_hover = _dict_to_str(
            opts=css_opts, key="button_hover", css_selector=".tab button:hover"
        )
        result += (
            tab_button_hover if tab_button_hover != "" else DEFAULT_TAB_BUTTON_HOVER_CSS
        )
        # .tab button.active
        tab_button_active = _dict_to_str(
            opts=css_opts, key="button_active", css_selector=".tab button.active"
        )
        result += (
            tab_button_active
            if tab_button_active != ""
            else DEFAULT_TAB_BUTTON_ACTIVE_CSS
        )
        if ".chart-container" not in result:
            result += """
            .chart-container { display: block; }

            .chart-container:nth-child(n+2) { display: none; }
            """
        return result

    def _prepare_render(self):
        for c in self:
            if not hasattr(c, "_is_tab_chart"):
                setattr(c, "_is_tab_chart", True)
            if hasattr(c, "dump_options"):
                c.json_contents = c.dump_options()
            if hasattr(c, "theme"):
                if c.theme not in ThemeType.BUILTIN_THEMES:
                    self.js_dependencies.add(c.theme)

    def render(
        self,
        path: str = "render.html",
        template_name: str = "simple_tab.html",
        env: types.Optional[Environment] = None,
        **kwargs,
    ) -> str:
        self._prepare_render()
        return engine.render(self, path, template_name, env, **kwargs)

    def render_embed(
        self,
        template_name: str = "simple_tab.html",
        env: types.Optional[Environment] = None,
        **kwargs,
    ) -> str:
        self._prepare_render()
        return engine.render_embed(self, template_name, env, **kwargs)

    def render_notebook(self):
        self._prepare_render()
        # only notebook env need to re-generate chart_id
        for c in self:
            c.chart_id = uuid.uuid4().hex
        return engine.render_notebook(
            self, "nb_jupyter_notebook_tab.html", "nb_jupyter_lab_tab.html"
        )
