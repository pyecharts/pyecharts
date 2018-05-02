#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import json

from pyecharts import Polar, Kline, Bar, Scatter
from nose.tools import eq_
from mock import patch
from pyecharts_javascripthon.api import DefaultJsonEncoder
from test.utils import get_fixture_content


@patch('random.randint')
def test_polar_type_scatter_one(patched):
    patched.return_value = '1'
    data = [i for i in range(101)]
    polar = Polar("极坐标系-散点图示例")
    polar.add(
        "",
        data,
        boundary_gap=False,
        type='scatter',
        is_splitline_show=False,
        is_axisline_show=True,
    )
    actual_options = json.dumps(
        polar.options, sort_keys=True, indent=4, cls=DefaultJsonEncoder
    )
    expected = get_fixture_content('polar_options.json')
    for a, b in zip(actual_options.split('\n'), expected.split('\n')):
        eq_(a.strip(), b.strip())


DATE = ["2017/7/{}".format(i + 1) for i in range(31)]
data = [
    [2320.26, 2320.26, 2287.3, 2362.94],
    [2300, 2291.3, 2288.26, 2308.38],
    [2295.35, 2346.5, 2295.35, 2345.92],
    [2347.22, 2358.98, 2337.35, 2363.8],
    [2360.75, 2382.48, 2347.89, 2383.76],
    [2383.43, 2385.42, 2371.23, 2391.82],
    [2377.41, 2419.02, 2369.57, 2421.15],
    [2425.92, 2428.15, 2417.58, 2440.38],
    [2411, 2433.13, 2403.3, 2437.42],
    [2432.68, 2334.48, 2427.7, 2441.73],
    [2430.69, 2418.53, 2394.22, 2433.89],
    [2416.62, 2432.4, 2414.4, 2443.03],
    [2441.91, 2421.56, 2418.43, 2444.8],
    [2420.26, 2382.91, 2373.53, 2427.07],
    [2383.49, 2397.18, 2370.61, 2397.94],
    [2378.82, 2325.95, 2309.17, 2378.82],
    [2322.94, 2314.16, 2308.76, 2330.88],
    [2320.62, 2325.82, 2315.01, 2338.78],
    [2313.74, 2293.34, 2289.89, 2340.71],
    [2297.77, 2313.22, 2292.03, 2324.63],
    [2322.32, 2365.59, 2308.92, 2366.16],
    [2364.54, 2359.51, 2330.86, 2369.65],
    [2332.08, 2273.4, 2259.25, 2333.54],
    [2274.81, 2326.31, 2270.1, 2328.14],
    [2333.61, 2347.18, 2321.6, 2351.44],
    [2340.44, 2324.29, 2304.27, 2352.02],
    [2326.42, 2318.61, 2314.59, 2333.67],
    [2314.68, 2310.59, 2296.58, 2320.96],
    [2309.16, 2286.6, 2264.83, 2333.29],
    [2282.17, 2263.97, 2253.25, 2286.33],
    [2255.77, 2270.28, 2253.31, 2276.22],
]


@patch('random.randint')
def test_kline_default(patched):
    patched.return_value = "1"
    kline = Kline("K 线图-默认示例")
    kline.add("日K", DATE, data)
    actual_options = json.dumps(
        kline.options, sort_keys=True, indent=4, cls=DefaultJsonEncoder
    )
    expected = get_fixture_content('kline_options.json')
    for a, b in zip(actual_options.split('\n'), expected.split('\n')):
        eq_(a.strip(), b.strip())


@patch('random.randint')
def test_bar_default(patched):
    patched.return_value = "1"
    attr = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
    bar = Bar("Bar chart", "precipitation and evaporation one year")
    bar.add(
        "precipitation",
        attr,
        v1,
        mark_line=["average"],
        mark_point=["max", "min"],
    )
    bar.add(
        "evaporation",
        attr,
        v2,
        mark_line=["average"],
        mark_point=["max", "min"],
    )
    actual_options = json.dumps(
        bar.options, sort_keys=True, indent=4, cls=DefaultJsonEncoder
    )
    expected = get_fixture_content('bar_options.json')
    for a, b in zip(actual_options.split('\n'), expected.split('\n')):
        eq_(a.strip(), b.strip())


@patch('random.randint')
def test_scatter_option(patched):
    patched.return_value = "1"
    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [10, 20, 30, 40, 50, 60]
    scatter = Scatter("scatter test")
    scatter.add("A", v1, v2)
    scatter.add("B", v1[::-1], v2)
    actual_options = json.dumps(
        scatter.options, sort_keys=True, indent=4, cls=DefaultJsonEncoder
    )
    expected = get_fixture_content('scatter_options.json')
    for a, b in zip(actual_options.split('\n'), expected.split('\n')):
        eq_(a.strip(), b.strip())
