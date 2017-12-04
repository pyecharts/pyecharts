#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

from mock import patch, MagicMock

from nose.tools import eq_, raises
from pyecharts.template import ensure_echarts_is_in_the_front


def test_echarts_postion_in_dependency_list():
    test_sequence = set(['guangdong', 'shanghai', 'echarts'])
    result = ensure_echarts_is_in_the_front(test_sequence)
    eq_(result[0], 'echarts')


def test_echarts_postion_with_one_element_set():
    test_sequence = set(['echarts'])
    result = ensure_echarts_is_in_the_front(test_sequence)
    eq_(result[0], 'echarts')


@raises(Exception)
def test_echarts_postion_with_nothing():
    test_sequence = set()
    ensure_echarts_is_in_the_front(test_sequence)


@patch('pyecharts.template.create_builtin_template_engine')
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

    from pyecharts.template import render

    test_pills = dict(canIGet='The Pills Back',
                      orCanINot='Get them back')
    render('tmp', **test_pills)
    fake_get_template.assert_called_with('tmp')
    fake_render.assert_called_with(**test_pills)
