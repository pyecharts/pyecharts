import datetime
import random
import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import Calendar


class TestCalendarChart(unittest.TestCase):

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_calendar_base(self, fake_writer):
        begin = datetime.date(2017, 1, 1)
        end = datetime.date(2017, 12, 31)
        data = [
            [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
            for i in range((end - begin).days + 1)
        ]

        c = (
            Calendar()
            .add("", data, calendar_opts=opts.CalendarOpts(range_="2017"))
            .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(
                    max_=20000,
                    min_=500,
                    orient="horizontal",
                    is_piecewise=True,
                    pos_top="230px",
                    pos_left="100px",
                )
            )
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")
        self.assertIn("visualMap", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_calendar_setting(self, fake_writer):
        begin = datetime.date(2017, 1, 1)
        end = datetime.date(2017, 12, 31)
        data = [
            [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
            for i in range((end - begin).days + 1)
        ]

        c = Calendar().add(
            "",
            data,
            calendar_opts=opts.CalendarOpts(
                range_="2017",
                cell_size=15,
                daylabel_opts=opts.CalendarDayLabelOpts(name_map="cn"),
                monthlabel_opts=opts.CalendarMonthLabelOpts(name_map="cn"),
            ),
            visualmap_opts=opts.VisualMapOpts(
                max_=20000,
                min_=500,
                orient="horizontal",
                is_piecewise=True,
                pos_top="230px",
                pos_left="100px",
            ),
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("cellSize", content)
        self.assertIn("dayLabel", content)
        self.assertIn("monthLabel", content)
        self.assertIn("visualMap", content)

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_multi_calendar(self, fake_writer):

        def get_calendar_data(year: int):
            begin = datetime.date(year, 1, 1)
            end = datetime.date(year, 12, 31)
            return [
                [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
                for i in range((end - begin).days + 1)
            ]

        c = (
            Calendar(init_opts=opts.InitOpts(width="1300px", height="600px"))
            .add(
                series_name="2015",
                yaxis_data=get_calendar_data(year=2015),
                calendar_opts=opts.CalendarOpts(
                    range_="2015",
                    cell_size=["auto", 20],
                    pos_left="100",
                ),
                calendar_index=0,
            )
            .add(
                series_name="2016",
                yaxis_data=get_calendar_data(year=2016),
                calendar_opts=opts.CalendarOpts(
                    range_="2016",
                    pos_top="260",
                    cell_size=["auto", 20],
                    pos_left="100",
                ),
                calendar_index=1,
            )
            .add(
                series_name="2017",
                yaxis_data=get_calendar_data(year=2017),
                calendar_opts=opts.CalendarOpts(
                    range_="2017",
                    pos_top="450",
                    cell_size=["auto", 20],
                    pos_left="100",
                ),
                calendar_index=2,
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="2015~2017 年微信步数情况"),
                visualmap_opts=opts.VisualMapOpts(
                    max_=20000,
                    min_=500,
                    orient="vertical",
                    is_calculable=True,
                ),
            )
        )

        c.render()
        _, content = fake_writer.call_args[0]
        self.assertIn("cellSize", content)
        self.assertIn("visualMap", content)
