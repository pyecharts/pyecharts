from unittest.mock import patch

from nose.tools import assert_in

from example.commons import Faker
from pyecharts.charts import Bar, Line, Tab


def _create_bar() -> Bar:
    return Bar().add_xaxis(Faker.week).add_yaxis("商家A", [1, 2, 3, 4, 5, 6, 7])


def _create_line() -> Line:
    return Line().add_xaxis(Faker.week).add_yaxis("商家A", [7, 6, 5, 4, 3, 2, 1])


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_tab_base(fake_writer):
    bar = _create_bar()
    line = _create_line()
    tab = Tab().add(bar, "bar-example").add(line, "line-example")
    tab.render()
    _, content = fake_writer.call_args[0]
    assert_in("bar-example", content)
    assert_in("line-example", content)
