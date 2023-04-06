from unittest.mock import patch

from nose.tools import assert_equal

from pyecharts.faker import Faker, Collector


def test_rand_color():
    rand_color = Faker.rand_color()
    assert rand_color is not None


def test_img_path():
    assert_equal(Faker.img_path(path="/usr/local"), "/usr/local")


def test_collector():
    def _add(x, y):
        return x + y

    c = Collector()
    c.funcs(_add)
    assert_equal(c.charts[0][1], "_add")
