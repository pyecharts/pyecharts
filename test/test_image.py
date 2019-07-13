from unittest.mock import patch

from nose.tools import assert_in

from pyecharts.components import Image


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_table_base(fake_writer):
    test_src = "http://test-src.com/test.png"
    Image().add(src=test_src).render()
    _, content = fake_writer.call_args[0]
    assert_in(test_src, content)
