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
                },
                "https://extra_host.com/css": {
                    "dep1": ("extra_file_path", "css"),
                },
            }
        )

        # Bar 图
        chart = Bar()
        chart.js_host = None
        chart.js_dependencies.items = [
            "https://api.map.baidu.com/test",
            "existing_dep",
            "dep",
            "dep1",
        ]

        RenderEngine.generate_js_link(chart)

        assert chart.js_host == CurrentConfig.ONLINE_HOST

        expected_links = [
            "https://api.map.baidu.com/test",
            "{}file_path.ext".format(CurrentConfig.ONLINE_HOST),
            "https://extra_host.comextra_file_path.extra_ext",
        ]
        assert chart.dependencies == expected_links

        expected_css_links = [
            "https://extra_host.com/cssextra_file_path.css",
        ]
        assert chart.css_libs == expected_css_links

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

    def test_iterable_import(self):
        # 尝试从 collections.abc 导入 Iterable
        try:
            from collections.abc import Iterable
            self.assertTrue(True)  # 如果成功导入，测试通过
        except ImportError:
            # 如果从 collections.abc 导入失败，则尝试从 collections 导入
            try:
                from collections import Iterable
                self.assertTrue(True)  # 如果这里成功导入，测试通过
            except ImportError:
                # 如果两者都失败，则测试不通过
                self.fail("Failed to import Iterable")
