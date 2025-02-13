import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Radar, Geo, Map
from pyecharts.globals import ThemeType, ChartType
from pyecharts.faker import Faker


class TestGridComponent(unittest.TestCase):
    def _verify_instance_for_datazoom_and_visualmap(self, chart, key):
        return isinstance(
            chart.options.get(key), list
        ) and all(
            isinstance(
                item,
                (opts.DataZoomOpts if key == "dataZoom" else opts.VisualMapOpts, dict)
            ) for item in chart.options.get(key)
        )

    def _chart_for_grid(self) -> Bar:
        x_data = ["{}月".format(i) for i in range(1, 13)]
        bar = (
            Bar()
            .add_xaxis(x_data)
            .add_yaxis(
                "蒸发量",
                [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
                yaxis_index=0,
            )
            .add_yaxis(
                "降水量",
                [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
                yaxis_index=1,
            )
            .extend_axis(
                yaxis=opts.AxisOpts(name="蒸发量", type_="value", position="right")
            )
            .extend_axis(
                yaxis=opts.AxisOpts(type_="value", name="温度", position="left")
            )
            .set_global_opts(
                yaxis_opts=opts.AxisOpts(name="降水量", position="right", offset=80)
            )
        )

        line = (
            Line()
            .add_xaxis(x_data)
            .add_yaxis(
                "平均温度",
                [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
                yaxis_index=2,
                color="#675bba",
                label_opts=opts.LabelOpts(is_show=False),
            )
        )

        bar.overlap(line)
        return bar

    def _chart_for_set_grid_index(self, gird_index=None) -> Bar:
        bar = (
            Bar()
            .add_xaxis(Faker.choose())
            .add_yaxis("商家A", Faker.values())
            .set_global_opts(
                xaxis_opts=opts.AxisOpts(grid_index=gird_index),
                yaxis_opts=opts.AxisOpts(grid_index=gird_index)
            )
        )
        return bar

    def _chart_for_grid_with_datazoom_and_visualmap(self) -> Bar:
        bar_1 = (
            Bar()
            .add_xaxis(Faker.days_attrs)
            .add_yaxis("商家", Faker.days_values)
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Bar-DataZoom"),
                datazoom_opts=opts.DataZoomOpts(),
                visualmap_opts=opts.VisualMapOpts(),
                toolbox_opts=opts.ToolboxOpts(
                    feature=opts.ToolBoxFeatureOpts(
                        save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(
                            exclude_components=["dataZoom", "toolbox"],
                        )
                    ),
                ),
                legend_opts=opts.LegendOpts(),
            )
        )
        return bar_1

    def _chart_for_grid_with_multiple_datazoom_and_visualmap(self) -> Bar:
        bar_1 = (
            Bar()
            .add_xaxis(Faker.days_attrs)
            .add_yaxis("商家", Faker.days_values)
            .set_global_opts(
                title_opts=opts.TitleOpts(title="Bar-DataZoom"),
                datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts()],
                visualmap_opts=[opts.VisualMapOpts(), opts.VisualMapOpts()],
                toolbox_opts=opts.ToolboxOpts(
                    feature=opts.ToolBoxFeatureOpts(
                        save_as_image=opts.ToolBoxFeatureSaveAsImageOpts(
                            exclude_components=["dataZoom", "toolbox"],
                        )
                    ),
                ),
                legend_opts=opts.LegendOpts(),
            )
        )
        return bar_1

    def test_grid_set_grid_index(self):
        bar_1 = self._chart_for_set_grid_index()
        bar_2 = self._chart_for_set_grid_index()
        bar_3 = self._chart_for_set_grid_index()
        gc = (
            Grid()
            .add(chart=bar_1, grid_index=1, grid_opts=opts.GridOpts())
            .add(chart=bar_2, grid_index=0, grid_opts=opts.GridOpts())
            .add(chart=bar_3, grid_index=2, grid_opts=opts.GridOpts())
        )
        expected_idx = (1, 0, 2)
        for idx, series in enumerate(gc.options.get("xAxis")):
            self.assertEqual(series.get("gridIndex"), expected_idx[idx])

        bar_1 = self._chart_for_set_grid_index()
        bar_2 = self._chart_for_set_grid_index()
        bar_3 = self._chart_for_set_grid_index()
        gc = (
            Grid()
            .add(chart=bar_1, grid_index=0, grid_opts=opts.GridOpts())
            .add(chart=bar_2, grid_index=2, grid_opts=opts.GridOpts())
            .add(chart=bar_3, grid_index=1, grid_opts=opts.GridOpts())
        )
        expected_idx = (1, 0, 2)
        for idx, series in enumerate(gc.options.get("xAxis")):
            self.assertEqual(series.get("gridIndex"), expected_idx[idx])

    def test_grid_set_grid_index_priority(self):
        bar_1 = self._chart_for_set_grid_index(gird_index=2)
        bar_2 = self._chart_for_set_grid_index(gird_index=0)
        bar_3 = self._chart_for_set_grid_index(gird_index=1)
        gc = (
            Grid()
            .add(chart=bar_1, grid_index=1, grid_opts=opts.GridOpts())
            .add(chart=bar_2, grid_index=2, grid_opts=opts.GridOpts())
            .add(chart=bar_3, grid_index=0, grid_opts=opts.GridOpts())
        )
        expected_idx = (2, 0, 1)
        for idx, series in enumerate(gc.options.get("xAxis")):
            self.assertEqual(series.get("gridIndex"), expected_idx[idx])

        bar_1 = self._chart_for_set_grid_index(gird_index=0)
        bar_2 = self._chart_for_set_grid_index(gird_index=2)
        bar_3 = self._chart_for_set_grid_index(gird_index=1)
        gc = (
            Grid()
            .add(chart=bar_1, grid_index=2, grid_opts=opts.GridOpts())
            .add(chart=bar_2, grid_index=1, grid_opts=opts.GridOpts())
            .add(chart=bar_3, grid_index=0, grid_opts=opts.GridOpts())
        )
        expected_idx = (0, 2, 1)
        for idx, series in enumerate(gc.options.get("xAxis")):
            self.assertEqual(series.get("gridIndex"), expected_idx[idx])

    def test_grid_set_grid_out_of_order(self):
        bar_1 = self._chart_for_set_grid_index(gird_index=2)
        bar_2 = self._chart_for_set_grid_index(gird_index=0)
        bar_3 = self._chart_for_set_grid_index(gird_index=1)
        gc = (
            Grid()
            .add(chart=bar_2, grid_index=1, grid_opts=opts.GridOpts())
            .add(chart=bar_3, grid_index=2, grid_opts=opts.GridOpts())
            .add(chart=bar_1, grid_index=0, grid_opts=opts.GridOpts())
        )
        expected_idx = (0, 1, 2)
        for idx, series in enumerate(gc.options.get("xAxis")):
            self.assertEqual(series.get("gridIndex"), expected_idx[idx])

    def test_grid_control_axis_index(self):
        bar = self._chart_for_grid()
        gc = Grid().add(
            bar,
            opts.GridOpts(pos_left="5%", pos_right="20%"),
            is_control_axis_index=True,
        )
        expected_idx = (0, 1, 2)
        for idx, series in enumerate(gc.options.get("series")):
            self.assertEqual(series.get("yAxisIndex"), expected_idx[idx])

    def test_grid_do_not_control_axis_index(self):
        bar = self._chart_for_grid()
        gc = Grid().add(bar, opts.GridOpts(pos_left="5%", pos_right="20%"))
        expected_idx = (0, 0, 0)
        for idx, series in enumerate(gc.options.get("series")):
            self.assertEqual(series.get("yAxisIndex"), expected_idx[idx])

    def test_grid_with_more_datazoom_and_visualmap_opts(self):
        bar_1 = self._chart_for_grid_with_datazoom_and_visualmap()
        bar_2 = self._chart_for_grid_with_datazoom_and_visualmap()
        grid_1 = (
            Grid()
            .add(chart=bar_1, grid_opts=opts.GridOpts())
            .add(chart=bar_2, grid_opts=opts.GridOpts())
        )
        expected_opts_len = 2
        self.assertEqual(
            len(grid_1.options.get("dataZoom")), expected_opts_len
        )
        self.assertEqual(
            len(grid_1.options.get("visualMap")), expected_opts_len
        )
        self.assertEqual(
            self._verify_instance_for_datazoom_and_visualmap(grid_1, "dataZoom"), True
        )
        self.assertEqual(
            self._verify_instance_for_datazoom_and_visualmap(grid_1, "visualMap"), True
        )

        bar_3 = self._chart_for_grid()
        bar_4 = self._chart_for_grid_with_datazoom_and_visualmap()
        grid_2 = (
            Grid()
            .add(chart=bar_3, grid_opts=opts.GridOpts())
            .add(chart=bar_4, grid_opts=opts.GridOpts())
        )
        expected_opts_len = 1
        self.assertEqual(
            len(grid_2.options.get("dataZoom")), expected_opts_len
        )
        self.assertEqual(
            len(grid_2.options.get("visualMap")), expected_opts_len
        )
        self.assertEqual(
            self._verify_instance_for_datazoom_and_visualmap(grid_2, "dataZoom"), True
        )
        self.assertEqual(
            self._verify_instance_for_datazoom_and_visualmap(grid_2, "visualMap"), True
        )

        bar_5 = self._chart_for_grid_with_multiple_datazoom_and_visualmap()
        bar_6 = self._chart_for_grid_with_datazoom_and_visualmap()
        bar_7 = self._chart_for_grid()
        grid_3 = (
            Grid()
            .add(chart=bar_5, grid_opts=opts.GridOpts())
            .add(chart=bar_6, grid_opts=opts.GridOpts())
            .add(chart=bar_7, grid_opts=opts.GridOpts())
        )
        expected_opts_len = 3
        self.assertEqual(
            len(grid_3.options.get("dataZoom")), expected_opts_len
        )
        self.assertEqual(
            len(grid_3.options.get("visualMap")), expected_opts_len
        )
        self.assertEqual(
            self._verify_instance_for_datazoom_and_visualmap(grid_3, "dataZoom"), True
        )
        self.assertEqual(
            self._verify_instance_for_datazoom_and_visualmap(grid_3, "visualMap"), True
        )

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_grid_options(self, fake_writer):
        bar = self._chart_for_grid()
        gc = Grid(init_opts=opts.InitOpts(theme=ThemeType.ESSOS)).add(
            bar, opts.GridOpts(pos_left="5%", pos_right="20%", is_contain_label=True)
        )
        gc.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("containLabel", content)
        self.assertIn("color", content)

    def _chart_for_grid_v2(self):
        x_data = ["{}月".format(i) for i in range(1, 13)]
        bar = (
            Bar()
            .add_xaxis(x_data)
            .add_yaxis(
                "蒸发量",
                [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
                yaxis_index=0,
                color="red",
            )
            .add_yaxis(
                "降水量",
                [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
                yaxis_index=1,
                color="green",
            )
            .extend_axis(
                yaxis=opts.AxisOpts(name="蒸发量", type_="value", position="right")
            )
            .extend_axis(
                yaxis=opts.AxisOpts(type_="value", name="温度", position="left")
            )
            .set_global_opts(
                yaxis_opts=opts.AxisOpts(name="降水量", position="right", offset=80)
            )
        )

        line = (
            Line()
            .add_xaxis(x_data)
            .add_yaxis(
                "平均温度",
                [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
                yaxis_index=2,
                color="blue",
                label_opts=opts.LabelOpts(is_show=False),
            )
            .set_global_opts(visualmap_opts=opts.VisualMapOpts())
        )

        bar.overlap(line)
        self.assertEqual(bar.colors[:3], ["red", "green", "blue"])
        return bar

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_grid_example_1(self, fake_writer):
        bar = self._chart_for_grid_v2()
        gc = Grid().add(
            bar,
            opts.GridOpts(pos_left="5%", pos_right="20%"),
            is_control_axis_index=True,
        )
        expected_idx = (0, 1, 2)
        for idx, series in enumerate(gc.options.get("series")):
            self.assertEqual(series.get("yAxisIndex"), expected_idx[idx])
        gc.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("yAxisIndex", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_grid_geo_bar(self, fake_writer):
        bar = (
            Bar()
            .add_xaxis(Faker.choose())
            .add_yaxis("商家A", Faker.values())
            .add_yaxis("商家B", Faker.values())
            .set_global_opts(
                title_opts=dict(title="Bar 图"),
                legend_opts=opts.LegendOpts(pos_left="20%"),
            )
        )
        geo = (
            Geo()
            .add_schema(maptype="china")
            .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(),
                title_opts=dict(title="Geo 图"),
            )
        )

        grid = (
            Grid()
            .add(bar, grid_opts=opts.GridOpts(pos_top="50%", pos_right="75%"))
            .add(geo, grid_opts=opts.GridOpts(pos_left="60%"))
        )
        grid.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("geo", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_grid_two_radar(self, fake_writer):
        schema = [
            opts.RadarIndicatorItem(name="销售", max_=6500),
            opts.RadarIndicatorItem(name="管理", max_=16000),
            opts.RadarIndicatorItem(name="信息技术", max_=30000),
            opts.RadarIndicatorItem(name="客服", max_=38000),
            opts.RadarIndicatorItem(name="研发", max_=52000),
            opts.RadarIndicatorItem(name="市场", max_=25000),
        ]
        c = (
            Radar()
            .add_schema(schema=schema, center=["25%", "50%"])
            .add(
                series_name="预算分配",
                data=[[4300, 10000, 28000, 35000, 50000, 19000]],
                radar_index=0,
            )
            .set_global_opts(legend_opts=opts.LegendOpts(pos_left="20%"))
        )
        c2 = (
            Radar()
            .add_schema(schema=schema, center=["75%", "50%"])
            .add(
                series_name="实际开销",
                data=[[5000, 14000, 28000, 31000, 42000, 21000]],
                radar_index=1,
            )
            .set_global_opts(legend_opts=opts.LegendOpts(pos_right="20%"))
        )

        grid = (
            Grid().add(c, grid_opts=opts.GridOpts()).add(c2, grid_opts=opts.GridOpts())
        )
        grid.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("radar", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_grid_mutil_yaxis(self, fake_writer):
        bar = (
            Bar()
            .add_xaxis(["{}月".format(i) for i in range(1, 13)])
            .add_yaxis(
                "蒸发量",
                [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
                yaxis_index=0,
                color="#d14a61",
            )
            .add_yaxis(
                "降水量",
                [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
                yaxis_index=1,
                color="#5793f3",
            )
            .extend_axis(
                yaxis=opts.AxisOpts(
                    name="蒸发量",
                    type_="value",
                    min_=0,
                    max_=250,
                    position="right",
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                    ),
                    axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
                )
            )
            .extend_axis(
                yaxis=opts.AxisOpts(
                    type_="value",
                    name="温度",
                    min_=0,
                    max_=25,
                    position="left",
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#675bba")
                    ),
                    axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
                    splitline_opts=opts.SplitLineOpts(
                        is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                    ),
                )
            )
            .set_global_opts(
                yaxis_opts=opts.AxisOpts(
                    name="降水量",
                    min_=0,
                    max_=250,
                    position="right",
                    offset=80,
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                    ),
                    axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
                ),
                title_opts=opts.TitleOpts(title="Grid-Overlap-多 X/Y 轴示例"),
                tooltip_opts=opts.TooltipOpts(
                    trigger="axis", axis_pointer_type="cross"
                ),
                legend_opts=opts.LegendOpts(pos_left="25%"),
            )
        )

        line = (
            Line()
            .add_xaxis(["{}月".format(i) for i in range(1, 13)])
            .add_yaxis(
                "平均温度",
                [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
                yaxis_index=2,
                color="#675bba",
                label_opts=opts.LabelOpts(is_show=False),
            )
        )

        bar1 = (
            Bar()
            .add_xaxis(["{}月".format(i) for i in range(1, 13)])
            .add_yaxis(
                "蒸发量 1",
                [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
                color="#d14a61",
                xaxis_index=1,
                yaxis_index=3,
            )
            .add_yaxis(
                "降水量 2",
                [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
                color="#5793f3",
                xaxis_index=1,
                yaxis_index=3,
            )
            .extend_axis(
                yaxis=opts.AxisOpts(
                    name="蒸发量",
                    type_="value",
                    min_=0,
                    max_=250,
                    position="right",
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#d14a61")
                    ),
                    axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
                )
            )
            .extend_axis(
                yaxis=opts.AxisOpts(
                    type_="value",
                    name="温度",
                    min_=0,
                    max_=25,
                    position="left",
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#675bba")
                    ),
                    axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
                    splitline_opts=opts.SplitLineOpts(
                        is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
                    ),
                )
            )
            .set_global_opts(
                xaxis_opts=opts.AxisOpts(grid_index=1),
                yaxis_opts=opts.AxisOpts(
                    name="降水量",
                    min_=0,
                    max_=250,
                    position="right",
                    offset=80,
                    grid_index=1,
                    axisline_opts=opts.AxisLineOpts(
                        linestyle_opts=opts.LineStyleOpts(color="#5793f3")
                    ),
                    axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
                ),
                tooltip_opts=opts.TooltipOpts(
                    trigger="axis", axis_pointer_type="cross"
                ),
                legend_opts=opts.LegendOpts(pos_left="65%"),
            )
        )

        line1 = (
            Line()
            .add_xaxis(["{}月".format(i) for i in range(1, 13)])
            .add_yaxis(
                "平均温度 1",
                [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
                color="#675bba",
                label_opts=opts.LabelOpts(is_show=False),
                xaxis_index=1,
                yaxis_index=5,
            )
        )

        overlap_1 = bar.overlap(line)
        overlap_2 = bar1.overlap(line1)

        grid = (
            Grid(init_opts=opts.InitOpts(width="1200px", height="800px"))
            .add(
                overlap_1,
                grid_opts=opts.GridOpts(pos_right="58%"),
                is_control_axis_index=True,
            )
            .add(
                overlap_2,
                grid_opts=opts.GridOpts(pos_left="58%"),
                is_control_axis_index=True,
            )
        )
        grid.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("xAxis", content)
        self.assertIn("yAxis", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_grid_geo_map(self, fake_writer):
        data_pair = [list(z) for z in zip(Faker.provinces, Faker.values())]
        geo_chart = (
            Geo()
            .add_schema(maptype="china")
            .add(
                "geo",
                data_pair=data_pair,
                type_=ChartType.SCATTER,
            )
            .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(),
            )
        )
        map_chart = (
            Map()
            .add("LCOH", data_pair=data_pair, maptype="china")
            .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(),
            )
        )
        grid_chart = (
            Grid(init_opts=opts.InitOpts())
            .add(map_chart, grid_opts=opts.GridOpts())
            .add(geo_chart, grid_opts=opts.GridOpts())
        )
        grid_chart.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("geo", content)
