import unittest

from pyecharts.faker import Faker, Collector


class TestFaker(unittest.TestCase):

    def test_rand_color(self):
        rand_color = Faker.rand_color()
        assert rand_color is not None

    def test_img_path(self):
        self.assertEqual(Faker.img_path(path="/usr/local"), "/usr/local")

    def test_collector(self):
        def _add(x, y):
            return x + y

        c = Collector()
        c.funcs(_add)
        self.assertEqual(c.charts[0][1], "_add")
