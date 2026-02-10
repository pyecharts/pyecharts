import unittest
from unittest.mock import patch

from pyecharts import options as opts
from pyecharts.charts import Chord


class TestChordChart(unittest.TestCase):

    @patch("pyecharts.render.engine.write_utf8_html_file")
    def test_chord_base(self, fake_writer):
        c = (
            Chord()
            .add(
                series_name="chord",
                data=[
                    opts.ChordData(name="A"),
                    opts.ChordData(name="B"),
                    opts.ChordData(name="C"),
                    opts.ChordData(name="D"),
                ],
                links=[
                    opts.ChordLink(
                        source="A",
                        target="B",
                        value=40,
                    ),
                    opts.ChordLink(
                        source="A",
                        target="C",
                        value=20,
                    ),
                    opts.ChordLink(
                        source="B",
                        target="D",
                        value=20,
                    ),
                ],
                is_clockwise=False,
                label_opts=opts.LabelOpts(is_show=True),
                linestyle_opts=opts.LineStyleOpts(color="target"),
            )
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertGreater(len(content), 2000)
        self.assertEqual(c.theme, "white")
        self.assertEqual(c.renderer, "canvas")
