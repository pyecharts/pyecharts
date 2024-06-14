import os
import unittest

from pyecharts.globals import RenderSepType


class TestGlobals(unittest.TestCase):
    def test_render_sep_type(self):
        # normal test
        render_sep_type = RenderSepType.SepType
        self.assertEqual(os.linesep, render_sep_type)

        # test modification
        before_modify_type = RenderSepType.SepType
        RenderSepType.SepType = "\t"
        after_modify_type = RenderSepType.SepType
        self.assertNotEqual(before_modify_type, after_modify_type)

        # Restore config
        RenderSepType.SepType = os.linesep
