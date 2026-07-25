import unittest
from unittest.mock import MagicMock, patch

from pyecharts.render.display import HTML, Javascript


class TestDisplay(unittest.TestCase):

    def test_display_html(self):
        html_content = "<p>hello world<p/>"
        obj = HTML(html_content)
        self.assertEqual(obj.data, html_content)
        self.assertEqual(obj.__html__(), html_content)

    def test_display_javascript(self):
        js_content = "console.log('hello world')"
        obj = Javascript(js_content)
        self.assertEqual(obj.data, js_content)
        self.assertEqual(obj._repr_javascript_(), js_content)

    def test_display_javascript_v1(self):
        js_content = "console.log('hello world')"
        obj = Javascript(js_content, lib="test lib", css="test css")
        self.assertEqual(obj.data, js_content)

        obj_1 = Javascript(
            data=js_content,
            lib=["lib1", "lib2"],
            css=["css1", "css2"],
        )
        self.assertEqual(obj_1.data, js_content)
        self.assertIn(js_content, obj_1._repr_javascript_())

    def test_display_javascript_v2(self):
        obj = Javascript(
            lib=["https://assets.pyecharts.org/assets/v5/echarts.min.js"]
        )
        obj.load_javascript_contents()
        self.assertIn(
            "echarts",
            obj.javascript_contents[
                "https://assets.pyecharts.org/assets/v5/echarts.min.js"
            ],
        )

        obj_1 = Javascript(
            lib=["https://assets.pyecharts.org/assets/v4/echarts.min.js"]
        )
        try:
            obj_1.load_javascript_contents()
        except RuntimeError:
            pass

    @patch("pyecharts.render.display.http.client.HTTPConnection")
    def test_display_javascript_v3_http(self, mock_http_conn_cls):
        mock_resp = MagicMock()
        mock_resp.status = 200
        mock_resp.read.return_value = b"var echarts = {};"

        mock_conn = MagicMock()
        mock_conn.getresponse.return_value = mock_resp
        mock_http_conn_cls.return_value = mock_conn

        url = "http://localhost:8080/assets/echarts.min.js"
        obj = Javascript(lib=[url])
        obj.load_javascript_contents()

        mock_http_conn_cls.assert_called_once_with("localhost", 8080)
        mock_conn.request.assert_called_once_with(
            "GET", "/assets/echarts.min.js"
        )
        self.assertEqual(obj.javascript_contents[url], "var echarts = {};")
