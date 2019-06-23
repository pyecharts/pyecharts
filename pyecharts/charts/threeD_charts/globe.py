from ... import types
from ...charts.chart import Chart3D
from ...options import InitOpts


class Globe(Chart3D):
    """
    """

    def __init__(self, init_opts: types.Init = InitOpts()):

        super().__init__(init_opts)
        self.options.update(
            globe={
                "show": True,
                "shading": 'lambert',
                "light": {
                    "ambient": {
                        "intensity": 0.6
                    },
                    "main": {
                        "intensity": 0.2
                    }
                }
            })
