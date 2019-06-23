from ... import types
from ...charts.chart import Chart3D
from ...charts.basic_charts.map import MapMixin
from ...options import InitOpts
from .globe import Globe
from jinja2 import Environment

import os
from ...render.engine import RenderEngine
import uuid

from ...commons import utils
from ...globals import CurrentConfig, NotebookType
from ...render.display import HTML


class MapGlobe(Chart3D, MapMixin):
    """
    Globe Map
    """

    def __init__(self, init_opts: types.Init = InitOpts()):
        super().__init__(init_opts)
        self.globe = Globe()

    def set_globe(self, a_globe):
        self.globe = a_globe

    def add_schema(
            self,
            maptype: str = "china",
            box_opts: dict = None
    ):
        self.js_dependencies.add(maptype)
        return self

    def render(
        self,
        path: str = "render.html",
        template_name: str = "simple_globe.html",
        env: types.Optional[Environment] = None,
    ) -> str:
        self._prepare_render()
        RenderEngine(env).render_chart_to_file(
            chart=self, path=path, template_name=template_name
        )
        return os.path.abspath(path)

    def render_notebook(self):
        self.chart_id = uuid.uuid4().hex
        self._prepare_render()
        if CurrentConfig.NOTEBOOK_TYPE == NotebookType.JUPYTER_NOTEBOOK:
            require_config = utils.produce_require_dict(
                self.js_dependencies, self.js_host
            )
            return HTML(RenderEngine().render_chart_to_notebook(
                    template_name="jupyter_globe.html",
                    charts=(self,),
                    config_items=require_config["config_items"],
                    libraries=require_config["libraries"],
                ))

        if CurrentConfig.NOTEBOOK_TYPE == NotebookType.JUPYTER_LAB:
            return HTML(
                RenderEngine().render_chart_to_notebook(
                    template_name="jupyter_lab.html", charts=(self,)
                )
            )

        if CurrentConfig.NOTEBOOK_TYPE == NotebookType.NTERACT:
            pass
