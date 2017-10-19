#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Style


def test_style():
    style = Style()
    s1 = style.add(is_random=True, label_pos="top")
    assert s1['is_random'] is True
    assert s1['label_pos'] == "top"
