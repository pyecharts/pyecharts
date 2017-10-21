#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from pyecharts import Bar, Line, Scatter, EffectScatter, Kline
from pyecharts import Overlap
from test.constants import CLOTHES


def test_overlap_bar_line():
    attr = ['A', 'B', 'C', 'D', 'E', 'F']
    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [38, 28, 58, 48, 78, 68]
    bar = Bar("Line-Bar 示例")
    bar.add("bar", attr, v1)
    line = Line()
    line.add("line", attr, v2)

    overlap = Overlap()
    overlap.add(bar)
    overlap.add(line)
    overlap.render()


def test_overlap_es_scatter():
    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [30, 30, 30, 30, 30, 30]
    v3 = [50, 50, 50, 50, 50, 50]
    v4 = [10, 10, 10, 10, 10, 10]
    es = EffectScatter("Scatter-EffectScatter 示例")
    es.add("es", v1, v2)
    scatter = Scatter()
    scatter.add("scatter", v1, v3)
    es_1 = EffectScatter()
    es_1.add("es_1", v1, v4, symbol='pin', effect_scale=5)

    overlap = Overlap()
    overlap.add(es)
    overlap.add(scatter)
    overlap.add(es_1)
    overlap.render()


def test_overlap_kline_line():
    import random
    v1 = [[2320.26, 2320.26, 2287.3, 2362.94],
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
          [2255.77, 2270.28, 2253.31, 2276.22]]
    attr = ["2017/7/{}".format(i + 1) for i in range(31)]
    kline = Kline("Kline-Line 示例")
    kline.add("日K", attr, v1)
    line_1 = Line()
    line_1.add("line-1", attr, [random.randint(2400, 2500) for _ in range(31)])
    line_2 = Line()
    line_2.add("line-2", attr, [random.randint(2400, 2500) for _ in range(31)])

    overlap = Overlap()
    overlap.add(kline)
    overlap.add(line_1)
    overlap.add(line_2)
    overlap.render()


def test_overlap_two_yaxis():
    attr = ["{}月".format(i) for i in range(1, 13)]
    v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
    v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
    v3 = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]

    bar = Bar(width=1200, height=600)
    bar.add("蒸发量", attr, v1)
    bar.add("降水量", attr, v2, yaxis_formatter=" ml", yaxis_max=250)

    line = Line()
    line.add("平均温度", attr, v3, yaxis_formatter=" °C")

    overlap = Overlap()
    overlap.add(bar)
    overlap.add(line, yaxis_index=1, is_add_yaxis=True)
    overlap.render()


def test_line_es():
    v1 = [5, 20, 36, 10, 10, 100]
    line = Line("line-EffectScatter 示例")
    line.add("", CLOTHES, v1, is_random=True)
    es = EffectScatter()
    es.add("", CLOTHES, v1, effect_scale=8)

    overlap = Overlap()
    overlap.add(line)
    overlap.add(es)
    overlap.render()
