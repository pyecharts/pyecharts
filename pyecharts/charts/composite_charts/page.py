import json
import os
import re
import uuid

from jinja2 import Environment

from ... import types
from ...commons import utils
from ...datasets import FILENAMES
from ...globals import CurrentConfig, NotebookType, ThemeType
from ...options import PageLayoutOpts
from ...render.display import HTML, Javascript
from ...render.engine import RenderEngine

_MARK_FREEDOM_LAYOUT = "_MARK_FREEDOM_LAYOUT_"

DOWNLOAD_CFG_FUNC = """
function downloadCfg () {
    const fileName = 'chart_config.json'
    let downLink = document.createElement('a')
    downLink.download = fileName

    let result = []
    for(let i=0; i<charts_id.length; i++) {
        chart = $('#'+charts_id[i])
        result.push({
            cid: charts_id[i],
            width: chart.css("width"),
            height: chart.css("height"),
            top: chart.offset().top + "px",
            left: chart.offset().left + "px"
        })
    }

    let blob = new Blob([JSON.stringify(result)])
    downLink.href = URL.createObjectURL(blob)
    document.body.appendChild(downLink)
    downLink.click()
    document.body.removeChild(downLink)
}"""


class Page:
    """
    `Page` A container object to present multiple charts vertically in a single page
    """

    SimplePageLayout = PageLayoutOpts(
        justify_content="center", display="flex", flex_wrap="wrap"
    )
    DraggablePageLayout = PageLayoutOpts()

    def __init__(
        self,
        page_title: str = CurrentConfig.PAGE_TITLE,
        js_host: str = "",
        interval: int = 1,
        layout: types.Union[PageLayoutOpts, dict] = PageLayoutOpts(),
    ):
        self.page_title = page_title
        self.page_interval = interval
        self.js_dependencies = utils.OrderedSet()
        self.js_functions: utils.OrderedSet = utils.OrderedSet()
        self.js_host = js_host or CurrentConfig.ONLINE_HOST
        self.layout = self._assembly_layout(layout)
        self.download_button: bool = False
        self._charts = []

    def add(self, *charts):
        for c in charts:
            self._charts.append(c)
            for d in c.js_dependencies.items:
                self.js_dependencies.add(d)
        return self

    def _assembly_layout(self, layout: types.Union[PageLayoutOpts, dict]) -> str:
        if layout is Page.DraggablePageLayout:
            return _MARK_FREEDOM_LAYOUT
        result = ""
        if isinstance(layout, PageLayoutOpts):
            layout = layout.opts
        layout = utils.remove_key_with_none_value(layout)
        for k, v in layout.items():
            result += "{}:{}; ".format(k, v)
        return result

    # List-Like Feature
    def __iter__(self):
        for chart in self._charts:
            yield chart

    def __len__(self):
        return len(self._charts)

    def _prepare_render(self):
        for c in self:
            c.json_contents = c.dump_options()
            if c.theme not in ThemeType.BUILTIN_THEMES:
                self.js_dependencies.add(c.theme)

        charts_id = []
        if self.layout == _MARK_FREEDOM_LAYOUT:
            self.download_button = True
            for c in self:
                charts_id.append("'{}'".format(c.chart_id))
                self.add_js_funcs(
                    # make charts resizable and draggable
                    f"$('#{c.chart_id}')"
                    ".resizable()"
                    ".draggable()"
                    ".css('border-style', 'dashed')"
                    ".css('border-width', '1px');"
                    # make charts Responsive
                    f'$("#{c.chart_id}>div:nth-child(1)")'
                    '.width("100%")'
                    '.height("100%");',
                    # call resize function
                    "new ResizeSensor("
                    f"jQuery('#{c.chart_id}'), "
                    f"function() {{ chart_{c.chart_id}.resize()}});",
                )
            for lib in ("jquery", "jquery-ui", "resize-sensor"):
                self.js_dependencies.add(lib)

            self.add_js_funcs(
                "var charts_id = [{}];".format(",".join(charts_id)) + DOWNLOAD_CFG_FUNC
            )
            self.css_libs = [self.js_host + link for link in ("jquery-ui.css",)]
            self.layout = ""

    def add_js_funcs(self, *fns):
        for fn in fns:
            self.js_functions.add(fn)
        return self

    def render(
        self,
        path: str = "render.html",
        template_name: str = "simple_page.html",
        env: types.Optional[Environment] = None,
    ):
        self._prepare_render()
        RenderEngine(env).render_chart_to_file(
            template_name=template_name, chart=self, path=path
        )
        return os.path.abspath(path)

    def render_embed(
        self,
        template_name: str = "simple_page.html",
        env: types.Optional[Environment] = None,
    ):
        self._prepare_render()
        return RenderEngine(env).render_chart_to_template(
            template_name=template_name, chart=self
        )

    def render_notebook(self):
        for c in self:
            c.json_contents = c.dump_options()
            c.chart_id = uuid.uuid4().hex
            if c.theme not in ThemeType.BUILTIN_THEMES:
                self.js_dependencies.add(c.theme)

        if CurrentConfig.NOTEBOOK_TYPE == NotebookType.JUPYTER_NOTEBOOK:
            require_config = utils.produce_require_dict(
                self.js_dependencies, self.js_host
            )
            return HTML(
                RenderEngine().render_chart_to_notebook(
                    template_name="jupyter_notebook.html",
                    charts=self,
                    config_items=require_config["config_items"],
                    libraries=require_config["libraries"],
                )
            )

        if CurrentConfig.NOTEBOOK_TYPE == NotebookType.JUPYTER_LAB:
            return HTML(
                RenderEngine().render_chart_to_notebook(
                    template_name="jupyter_lab.html", charts=self
                )
            )

        if CurrentConfig.NOTEBOOK_TYPE == NotebookType.NTERACT:
            pass

    def load_javascript(self):
        scripts = []
        for dep in self.js_dependencies.items:
            f, ext = FILENAMES[dep]
            scripts.append("{}{}.{}".format(CurrentConfig.ONLINE_HOST, f, ext))
        return Javascript(lib=scripts)

    @staticmethod
    def save_resize_html(
        source: str = "render.html",
        *,
        cfg_file: types.Optional[str] = None,
        cfg_dict: types.Optional[list] = None,
        dest: str = "resize_render.html",
    ) -> str:
        with open(source, "r", encoding="utf8") as f:
            html = f.read()

        if cfg_dict is None and cfg_dict is None:
            raise ValueError("Chart layout config is empty")

        if cfg_file:
            with open(cfg_file, "r", encoding="utf8") as f:
                charts = json.load(f)

        if cfg_dict:
            charts = cfg_dict

        for chart in charts:
            s = (
                '<div id="{cid}" style="position: absolute; '
                'width: {width}; height: {height}; top: {top}; left: {left};">'.format(
                    cid=chart["cid"],
                    width=chart["width"],
                    height=chart["height"],
                    top=chart["top"],
                    left=chart["left"],
                )
            )
            html = re.sub('<div id="{}" style="(.*?)">'.format(chart["cid"]), s, html)
            html = re.sub("'border-width', '1px'", "'border-width', '0px'", html)
            html = re.sub(
                r'<button onclick="downloadCfg\(\)">Save Config</button>', "", html
            )

        with open(dest, "w+", encoding="utf8") as f:
            f.write(html)

        return html
