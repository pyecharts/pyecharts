import os

from nose.tools import assert_equal, assert_not_equal

from pyecharts.globals import RenderSepType


def test_render_sep_type():
    # normal test
    render_sep_type = RenderSepType.SepType
    assert_equal(os.linesep, render_sep_type)

    # test modification
    before_modify_type = RenderSepType.SepType
    RenderSepType.SepType = "\t"
    after_modify_type = RenderSepType.SepType
    assert_not_equal(before_modify_type, after_modify_type)

    # Restore config
    RenderSepType.SepType = os.linesep
