from unittest.mock import patch

from nose.tools import assert_equal

from pyecharts.faker import Faker, Collector


def test_rand_color():
    rand_color = Faker.rand_color()
    assert rand_color is not None


def test_img_path():
    assert_equal(Faker.img_path(path="/usr/local"), "/usr/local")
