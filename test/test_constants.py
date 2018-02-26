# coding=utf-8

from __future__ import unicode_literals

import pyecharts.conf as conf
from nose.tools import eq_


DEFAULT_JS_LIBRARIES = dict(
    echarts='echarts.min',
    echartsgl='echarts-gl.min',
    liquidfill='echarts-liquidfill.min',
    wordcloud='echarts-wordcloud.min'
)

CITY_NAME_PINYIN_MAP = {
    "重庆": "chongqing",
    "澳门": "aomen",
    "北京": "beijing",
    "天津": "tianjin",
    "香港": "xianggang",
    "上海": "shanghai",
}

PROVINCE_NAME_PINYIN_MAP = {
    "广东": "guangdong",
    "安徽": "anhui",
    "福建": "fujian",
    "甘肃": "gansu",
    "广西": "guangxi",
    "贵州": "guizhou",
    "海南": "hainan",
    "河北": "hebei",
    "黑龙江": "heilongjiang",
    "河南": "henan",
    "湖北": "hubei",
    "湖南": "hunan",
    "江苏": "jiangsu",
    "江西": "jiangxi",
    "吉林": "jilin",
    "辽宁": "liaoning",
    "内蒙古": "neimenggu",
    "宁夏": "ningxia",
    "青海": "qinghai",
    "山东": "shandong",
    "山西": "shanxi",
    "四川": "sichuan",
    "台湾": "taiwan",
    "新疆": "xinjiang",
    "西藏": "xizang",
    "云南": "yunnan",
    "浙江": "zhejiang"
}


def test_core_js_libraries():
    __jupyter_echarts__ = conf.EXTENSION_MANAGER.get_a_extension('echarts')
    __file_map__ = __jupyter_echarts__.registry.get('FILE_MAP')
    for key, value in DEFAULT_JS_LIBRARIES.items():
        eq_(value, __file_map__[key])


def test_province_names():
    __provinces__ = conf.EXTENSION_MANAGER.get_a_extension(
        'echarts-china-provinces-js')
    __pinyin_map__ = __provinces__.registry.get('PINYIN_MAP')
    for key, value in PROVINCE_NAME_PINYIN_MAP.items():
        eq_(value, __pinyin_map__[key])


def test_city_names():
    __cities__ = conf.EXTENSION_MANAGER.get_a_extension(
        'echarts-china-cities-js')
    __pinyin_map__ = __cities__.registry.get('PINYIN_MAP', {})
    for key, value in CITY_NAME_PINYIN_MAP.items():
        eq_(value, __pinyin_map__[key])
