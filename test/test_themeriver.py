#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import ThemeRiver


def test_themeriver():
    data = [
        ['2015/11/08', 10, 'DQ'],
        ['2015/11/09', 15, 'DQ'],
        ['2015/11/10', 35, 'DQ'],
        ['2015/11/14', 7, 'DQ'],
        ['2015/11/15', 2, 'DQ'],
        ['2015/11/16', 17, 'DQ'],
        ['2015/11/17', 33, 'DQ'],
        ['2015/11/18', 40, 'DQ'],
        ['2015/11/19', 32, 'DQ'],
        ['2015/11/20', 26, 'DQ'],
        ['2015/11/21', 35, 'DQ'],
        ['2015/11/22', 40, 'DQ'],
        ['2015/11/23', 32, 'DQ'],
        ['2015/11/24', 26, 'DQ'],
        ['2015/11/25', 22, 'DQ'],
        ['2015/11/08', 35, 'TY'],
        ['2015/11/09', 36, 'TY'],
        ['2015/11/10', 37, 'TY'],
        ['2015/11/11', 22, 'TY'],
        ['2015/11/12', 24, 'TY'],
        ['2015/11/13', 26, 'TY'],
        ['2015/11/14', 34, 'TY'],
        ['2015/11/15', 21, 'TY'],
        ['2015/11/16', 18, 'TY'],
        ['2015/11/17', 45, 'TY'],
        ['2015/11/18', 32, 'TY'],
        ['2015/11/19', 35, 'TY'],
        ['2015/11/20', 30, 'TY'],
        ['2015/11/21', 28, 'TY'],
        ['2015/11/22', 27, 'TY'],
        ['2015/11/23', 26, 'TY'],
        ['2015/11/24', 15, 'TY'],
        ['2015/11/25', 30, 'TY'],
        ['2015/11/26', 35, 'TY'],
        ['2015/11/27', 42, 'TY'],
        ['2015/11/28', 42, 'TY'],
        ['2015/11/08', 21, 'SS'],
        ['2015/11/09', 25, 'SS'],
        ['2015/11/10', 27, 'SS'],
        ['2015/11/11', 23, 'SS'],
        ['2015/11/12', 24, 'SS'],
        ['2015/11/13', 21, 'SS'],
        ['2015/11/14', 35, 'SS'],
        ['2015/11/15', 39, 'SS'],
        ['2015/11/16', 40, 'SS'],
        ['2015/11/17', 36, 'SS'],
        ['2015/11/18', 33, 'SS'],
        ['2015/11/19', 43, 'SS'],
        ['2015/11/20', 40, 'SS'],
        ['2015/11/21', 34, 'SS'],
        ['2015/11/22', 28, 'SS'],
        ['2015/11/14', 7, 'QG'],
        ['2015/11/15', 2, 'QG'],
        ['2015/11/16', 17, 'QG'],
        ['2015/11/17', 33, 'QG'],
        ['2015/11/18', 40, 'QG'],
        ['2015/11/19', 32, 'QG'],
        ['2015/11/20', 26, 'QG'],
        ['2015/11/21', 35, 'QG'],
        ['2015/11/22', 40, 'QG'],
        ['2015/11/23', 32, 'QG'],
        ['2015/11/24', 26, 'QG'],
        ['2015/11/25', 22, 'QG'],
        ['2015/11/26', 16, 'QG'],
        ['2015/11/27', 22, 'QG'],
        ['2015/11/28', 10, 'QG'],
        ['2015/11/08', 10, 'SY'],
        ['2015/11/09', 15, 'SY'],
        ['2015/11/10', 35, 'SY'],
        ['2015/11/11', 38, 'SY'],
        ['2015/11/12', 22, 'SY'],
        ['2015/11/13', 16, 'SY'],
        ['2015/11/14', 7, 'SY'],
        ['2015/11/15', 2, 'SY'],
        ['2015/11/16', 17, 'SY'],
        ['2015/11/17', 33, 'SY'],
        ['2015/11/18', 40, 'SY'],
        ['2015/11/19', 32, 'SY'],
        ['2015/11/20', 26, 'SY'],
        ['2015/11/21', 35, 'SY'],
        ['2015/11/22', 4, 'SY'],
        ['2015/11/23', 32, 'SY'],
        ['2015/11/24', 26, 'SY'],
        ['2015/11/25', 22, 'SY'],
        ['2015/11/26', 16, 'SY'],
        ['2015/11/27', 22, 'SY'],
        ['2015/11/28', 10, 'SY'],
        ['2015/11/08', 10, 'DD'],
        ['2015/11/09', 15, 'DD'],
        ['2015/11/10', 35, 'DD'],
        ['2015/11/11', 38, 'DD'],
        ['2015/11/12', 22, 'DD'],
        ['2015/11/13', 16, 'DD'],
        ['2015/11/14', 7, 'DD'],
        ['2015/11/15', 2, 'DD'],
        ['2015/11/16', 17, 'DD'],
        ['2015/11/17', 33, 'DD'],
        ['2015/11/18', 4, 'DD'],
        ['2015/11/19', 32, 'DD'],
        ['2015/11/20', 26, 'DD'],
        ['2015/11/21', 35, 'DD'],
        ['2015/11/22', 40, 'DD'],
        ['2015/11/23', 32, 'DD'],
        ['2015/11/24', 26, 'DD'],
        ['2015/11/25', 22, 'DD'],
    ]
    tr = ThemeRiver("主题河流图示例图")
    tr.add(['DQ', 'TY', 'SS', 'QG', 'SY', 'DD'], data, is_label_show=True)
    tr.render()
