from nose.tools import eq_

from example.commons import Faker
from pyecharts.charts import EffectScatter


def test_effectscatter_base():
    c = EffectScatter().add_xaxis(Faker.choose()).add_yaxis("", Faker.values())
    eq_(c.theme, "white")
    eq_(c.renderer, "canvas")
    c.render()
