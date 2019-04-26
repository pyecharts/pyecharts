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


def test_wordcloud_base():
    c = WordCloud().add("", words, word_size_range=[20, 100])
    assert c.theme == "white"
    assert c.renderer == "canvas"
    c.render("render.html")
