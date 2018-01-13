import os
from nose.tools import eq_

from pyecharts.js_extension import JsExtension


def produce_test_js_extension():
    registry_path = os.path.join('.', 'fixtures')
    return JsExtension(registry_path)


def test_get_js_library():
    test_extension = produce_test_js_extension()
    print(test_extension.registry)
    actual = test_extension.get_js_library('abc')
    eq_(actual, 'the_js_file_name')


def test_get_js_link():
    test_extension = produce_test_js_extension()
    actual = test_extension.get_js_link('abc')
    eq_(actual, '/nbextensions/test-js/the_js_file_name.js')


def test_get_js_link():
    test_extension = produce_test_js_extension()
    actual = test_extension.get_js_link('abc')
    eq_(actual, '/nbextensions/test-js/the_js_file_name.js')
