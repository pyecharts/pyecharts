import os
from mock import patch
from nose.tools import eq_, raises

from pyecharts.js_extensions import JsExtension
import pyecharts.exceptions as exceptions


def produce_test_js_extension():
    registry_path = os.path.join('.', 'fixtures')
    return JsExtension.from_registry_path(registry_path)


def test_get_js_library():
    test_extension = produce_test_js_extension()
    actual = test_extension.get_js_library('pinyin')
    eq_(actual, 'the_js_file_name')


def test_get_js_link():
    test_extension = produce_test_js_extension()
    actual = test_extension.get_js_link('pinyin')
    assert actual in (
        './fixtures/test-js/the_js_file_name.js',
        '.\\fixtures\\test-js/the_js_file_name.js')


def test_get_js_link_no_match():
    test_extension = produce_test_js_extension()
    actual = test_extension.get_js_link('missing')
    assert actual is None


def test_get_js_link_use_github():
    test_extension = produce_test_js_extension()
    actual = test_extension.get_js_link('pinyin', jshost='local/path')
    eq_(actual, 'local/path/the_js_file_name.js')


def test_require_config():
    test_extension = produce_test_js_extension()
    actual = test_extension.produce_require_config_syntax('pinyin')
    eq_(actual, "'pinyin': '/nbextensions/test-js/the_js_file_name'")


def test_require_config_no_match():
    test_extension = produce_test_js_extension()
    actual = test_extension.produce_require_config_syntax('missing')
    assert actual is None


def test_read_js_library():
    test_extension = produce_test_js_extension()
    patcher = patch('os.path.join')
    fake_joinner = patcher.start()
    fake_joinner.return_value = "test_js_extension.py"
    content = test_extension.read_js_library('pinyin')
    assert 'test_read_js_library' in content
    patcher.stop()


def test_read_js_library_no_match():
    test_extension = produce_test_js_extension()
    content = test_extension.read_js_library('missing')
    assert content is None


@raises(exceptions.InvalidRegistry)
def test_validate_registry():
    from pyecharts.js_extensions import _validate_registry
    test = {}
    _validate_registry(test)
