#!/usr/bin/env python
# coding=utf-8

from pyecharts import WordCloud


name = [
    'Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World',
    'Charter Communications', 'Chick Fil A', 'Planet Fitness',
    'Pitch Perfect', 'Express', 'Home', 'Johnny Depp', 'Lena Dunham',
    'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham',
    'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break'
    ]

value = [
    10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112,
    965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265
    ]


def test_wordcloud_default():
    wordcloud = WordCloud(width=1300, height=620)
    wordcloud.add("", name, value, word_size_range=[30, 100], rotate_step=66)
    assert "diamond" not in wordcloud._repr_html_()


def test_wordcloud_shape_diamond():
    wordcloud = WordCloud(width=1300, height=620)
    wordcloud.add("", name, value, word_size_range=[30, 100], shape='diamond')
    assert "diamond" in wordcloud._repr_html_()
