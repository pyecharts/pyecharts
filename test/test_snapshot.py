# coding=utf8

"""
Test Cases for SnapshotEnvironment
Note: These cases will use Mock library instead of calling directly.
"""

from mock import MagicMock, patch

from pyecharts import Bar
from test.constants import CLOTHES

# Mock a SnapshotEnvironment object

FAKE_CONFIG = MagicMock(jupyter_presentation="svg")
FAKE_ENV = MagicMock(
    pyecharts_config=FAKE_CONFIG,
    render_chart_to_file=MagicMock(return_value="fake svg"),
)


def create_a_bar(title, renderer="canvas"):
    v1 = [5, 20, 36, 10, 75, 90]
    v2 = [10, 25, 8, 60, 20, 80]
    bar = Bar(title, renderer=renderer)
    bar.add("商家A", CLOTHES, v1, is_stack=True)
    bar.add("商家B", CLOTHES, v2, is_stack=True)
    return bar


@patch("pyecharts.engine.create_default_environment")
@patch("os.unlink")
def test_render_as_svg(fake_unlink, fake_env):
    fake_env.return_value = FAKE_ENV
    bar = create_a_bar("test", renderer="svg")
    svg_content = bar._repr_svg_()
    fake_unlink.assert_called()
    assert svg_content == "fake svg"


# @raises(exceptions.InvalidConfiguration)
# def test_render_as_svg_with_wrong_configuration():
#     bar = create_a_bar("test")
#     bar._repr_svg_()

#
# @patch("pyecharts.engine.create_default_environment")
# @patch("os.unlink")
# @raises(exceptions.InvalidConfiguration)
# def test_render_as_png_with_wrong_configuration(fake_unlink, fake_env):
#     fake_env.return_value = FAKE_ENV
#     with jupyter_image("png"):
#         bar = create_a_bar("test", renderer="svg")
#         bar._repr_png_()
