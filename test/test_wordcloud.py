from unittest.mock import patch

from nose.tools import eq_

from pyecharts.charts import WordCloud

words = [
    ("Sam S Club", 10000),
    ("Macys", 6181),
    ("Amy Schumer", 4386),
    ("Jurassic World", 4055),
    ("Charter Communications", 2467),
    ("Chick Fil A", 2244),
    ("Planet Fitness", 1868),
    ("Pitch Perfect", 1484),
]


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_wordcloud_base(fake_writer):
    c = WordCloud().add("", words, word_size_range=[20, 100])
    c.render()
    _, content = fake_writer.call_args[0]
    eq_(c.theme, "white")
    eq_(c.renderer, "canvas")
