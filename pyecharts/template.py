#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import warnings

from jinja2 import FileSystemLoader
from pyecharts.engine import EchartsEnvironment
import pyecharts.constants as constants
from pyecharts.utils import get_resource_dir, LazyObject
from pyecharts.conf import CURRENT_CONFIG


def get_current_engine():
    return EchartsEnvironment(
        loader=FileSystemLoader([CURRENT_CONFIG.echarts_template_dir, get_resource_dir('templates')])
    )


JINJA2_ENV = LazyObject(get_current_engine)


def produce_require_configuration(dependencies, jshost):
    """
    :param dependencies:
    :param jshost:
    :return:
    """
    _d = ensure_echarts_is_in_the_front(dependencies)
    # if no nick name register, we treat the location as location.js
    require_conf_items = [
        "'%s': '%s/%s'" % (key,
                           jshost,
                           constants.DEFAULT_JS_LIBRARIES.get(key, key))
        for key in _d]
    require_libraries = ["'%s'" % key for key in _d]
    return dict(
        config_items=require_conf_items,
        libraries=require_libraries
    )


def produce_html_script_list(dependencies):
    """
    :param dependencies:
    :return:
    """
    _d = ensure_echarts_is_in_the_front(dependencies)
    script_list = [
        '%s' % constants.DEFAULT_JS_LIBRARIES.get(key, key)
        for key in _d]
    return script_list


def ensure_echarts_is_in_the_front(dependencies):
    """
    make sure echarts is the item in the list
    require(['echarts'....], function(ec) {..}) need it to be first
    but dependencies is a set so has no sequence
    :param dependencies:
    :return:
    """
    if len(dependencies) > 1:
        dependencies.remove('echarts')
        dependencies = ['echarts'] + list(dependencies)
    elif len(dependencies) == 1:
        # make a new list
        dependencies = list(dependencies)
    else:
        raise Exception("No js library found. Nothing works!")
    return dependencies


def online(host=constants.DEFAULT_HOST):
    warnings.warn('The online will be deprecated,use "pyecharts.configure" instead.', DeprecationWarning)
    constants.CONFIGURATION['HOST'] = host
    CURRENT_CONFIG.jshost = host
