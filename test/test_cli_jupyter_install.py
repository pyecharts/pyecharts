# coding=utf8

from mock import patch, MagicMock
from nose.tools import assert_raises
from click.testing import CliRunner

from pyecharts.cli.commands.jupyter_install import (
    _validate_registry,
    retrieve_package_info
)


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


# Mock the import for different cases.
err_module = MagicMock(
    side_effect=ImportError('can not import this module.')
)
normal_module = MagicMock(return_value=MagicMock(__file__=r'\usr\foo\init'))


@patch('importlib.import_module', err_module)
def test_command_with_import_error():
    with assert_raises(ImportError):
        retrieve_package_info('jupyter-echarts-pypkg')


@patch('importlib.import_module', normal_module)
@patch('os.path.exists', MagicMock(return_value=True))
def test_command():
    info = retrieve_package_info('jupyter-echarts-pypkg')
    print(info)
    assert r'\usr\foo\resources\registry.json' == info['RegistryPath']
