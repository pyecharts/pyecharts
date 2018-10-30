# coding=utf8

from mock import patch
from nose.tools import assert_raises

from pyecharts.cli.commands.jupyter_install import _validate_registry

JUPYTER_EXTENSION_DIR = ''


def mock_jupyter_install():
    pass


@patch('codecs.open')
@patch('json.loads')
def test_validate_registry(json_load, open_loads):
    json_load.return_value = {
        "FILE_MAP": {},
        "GITHUB_URL": "",
        "JS_FOLDER": "",
        "JUPYTER_URL": "",
        "PINYIN_MAP": {}
    }
    valid = _validate_registry('Foo.json')
    assert valid


@patch('codecs.open')
@patch('json.loads')
def test_validate_registry_with_invalid_data(json_load, open_loads):
    json_load.return_value = {
        "FILE_MAP": {},
        "GITHUB_URL": "",
        "JS_FOLDER": "",
        "PINYIN_MAP": {}
    }

    with assert_raises(ValueError):
        _validate_registry('Foo.json')
