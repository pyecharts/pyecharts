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
        # Arrange
        dummy_data = [["2015-01-01", 10]]
        # Act: chamadas lineares e encadeadas (sem 'for' ou 'if')
        c = (
            Calendar()
            .add("2015", dummy_data, calendar_opts=opts.CalendarOpts(range_="2015"), calendar_index=0)
            .add("2016", dummy_data, calendar_opts=opts.CalendarOpts(range_="2016"), calendar_index=1)
            .add("2017", dummy_data, calendar_opts=opts.CalendarOpts(range_="2017"), calendar_index=2)
        )
        c.render()
        _, content = fake_writer.call_args[0]
        # Assert: verifica se as configurações e múltiplos calendários foram gerados
        self.assertEqual(len(c.options.get("calendar")), 3)
        self.assertEqual(len(c.options.get("series")), 3)
        self.assertIn("calendar", content)
