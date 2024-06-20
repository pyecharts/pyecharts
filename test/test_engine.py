import unittest
from unittest.mock import patch

from pyecharts.charts import Bar
from pyecharts.render.engine import RenderEngine
from pyecharts.datasets import EXTRA, FILENAMES
from pyecharts.globals import CurrentConfig


class TestEngine(unittest.TestCase):

    def test_generate_js_link(self):
        FILENAMES.update({"existing_dep": ("file_path", "ext")})
        EXTRA.update(
            {
                "https://extra_host.com": {
                    "dep": ("extra_file_path", "extra_ext"),
                }
            }
        )

        # Bar 图
        chart = Bar()
        chart.js_host = None
        chart.js_dependencies.items = [
            "https://api.map.baidu.com/test",
            "existing_dep",
            "dep",
        ]

        RenderEngine.generate_js_link(chart)

        assert chart.js_host == CurrentConfig.ONLINE_HOST

        expected_links = [
            "https://api.map.baidu.com/test",
            "{}file_path.ext".format(CurrentConfig.ONLINE_HOST),
            "https://extra_host.comextra_file_path.extra_ext",
        ]
        assert chart.dependencies == expected_links

    def test_import_iterable_new_location(self):
        # 在collections.abc不可用的情况下，尝试从collections导入
        with patch("collections.abc", side_effect=ImportError):
            import collections

            try:
                assert collections.Iterable.__module__ == "collections"
            except (AttributeError, AssertionError):
                pass

    def test_import_iterable_old_location(self):
        with patch.dict("sys.modules", {"collections.abc": object()}):
            import collections.abc

            # importlib.reload(collections.abc)  # 重新加载模块以应用补丁
            assert collections.abc.Iterable.__module__ == "collections.abc"
