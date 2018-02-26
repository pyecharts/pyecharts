# coding=utf8

from __future__ import unicode_literals

try:
    from unittest.mock import patch, MagicMock
except ImportError:
    from mock import patch, MagicMock


@patch('pyecharts.engine.EchartsEnvironment')
def test_template_render(fake_creator):
    fake_render = MagicMock(
        return_value='OK'
    )
    fake_get_template = MagicMock(
        return_value=MagicMock(
            render=fake_render
        )
    )
    fake_env = MagicMock(
        get_template=fake_get_template
    )
    fake_creator.return_value = fake_env

    from pyecharts.engine import render

    test_pills = dict(canIGet='The Pills Back',
                      orCanINot='Get them back')
    render('tmp', **test_pills)
    fake_get_template.assert_called_with('tmp')
    fake_render.assert_called_with(**test_pills)
