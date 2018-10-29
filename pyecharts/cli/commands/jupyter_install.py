# coding=utf8
import codecs
import json
import os
import warnings
import importlib

from setuptools.command.install import install

import click

REGISTRY_FILE = "registry.json"
JUPYTER_ENTRY = "JUPYTER_ENTRY"
REGISTRY_KEYS = [
    "FILE_MAP",
    "GITHUB_URL",
    "JS_FOLDER",
    "JUPYTER_URL",
    "PINYIN_MAP",
]


def _load_registry_json(file_path):
    with codecs.open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def _validate_registry(registry):
    for key in REGISTRY_KEYS:
        if key not in registry:
            raise InvalidRegistry("%s is missing" % key)


def install_cmd_for(package_name, package_path):
    # Command used for standard installs
    class InstallCommand(install):
        def run(self):
            print("Installing pyecharts module...")
            install.run(self)
            print("Installing javascript extensions %s ..." % package_name)
            _install(package_name, package_path)
            print("All done")

    return dict(install=InstallCommand)


class InvalidRegistry(Exception):
    pass


def _install(package_name, package_path):
    try:
        __registry__ = _load_registry_json(
            os.path.join(package_path, "..", REGISTRY_FILE)
        )
        _validate_registry(__registry__)
        _jupyter_install(
            package_name, __registry__[JUPYTER_ENTRY], package_path
        )
    except InvalidRegistry as e:
        print("Invalid registry: " + str(e))


def _jupyter_install(package_name, package_main, package_installation_path):
    install_nbextension, ConfigManager = __get_jupyter_note_utils()
    if install_nbextension and ConfigManager:
        print("Installing %s to jupyter.." % package_name)
        install_nbextension(
            package_installation_path, symlink=False, user=True
        )
        print("Enabling %s on jupyter.." % package_name)
        cm = ConfigManager()
        cm.update("notebook", {"load_extensions": {package_main: True}})
    else:
        warnings.warn(
            "No jupyter notebook found in your environment. "
            "Hence jupyter nbextensions were not installed. "
            "If you would like to have them,"
            "please issue 'pip install jupyter'."
        )


def __get_jupyter_note_utils():
    try:
        # IPython/Jupyter 4.0
        from notebook.nbextensions import install_nbextension
        from notebook.services.config import ConfigManager
    except ImportError:
        # Pre-schism
        try:
            from IPython.html.nbextensions import install_nbextension
            from IPython.html.services.config import ConfigManager
        except ImportError:
            raise
    return install_nbextension, ConfigManager


_INFO_FIELDS = ['import_name', 'extension_dir']
_PACKAGE_RAW = [
    ['jupyter-echarts-pypkg', 'jupyter_echarts_pypkg', 'echarts'],
    ['echarts-themes-pypkg', 'echarts_themes_pypkg', 'echarts-themes-js'],
    ['echarts-cities-pypkg', 'echarts_cities_pypkg', 'echarts_cities_js'],
    ['echarts-china-counties-pypkg', 'echarts_china_counties_pypkg',
     'echarts-china-counties-js'],
    ['echarts-china-provinces-pypkg', 'echarts_china_provinces_pypkg',
     'echarts-china-provinces-js'],
    ['echarts-coutries-pypkg', 'echarts_coutries_pypkg',
     'echarts-countries-js'],
    ['echarts-china-misc-pypkg', 'echarts_china_misc_pypkg',
     'echarts-china-misc-js'],
    ['echarts-china-cities-pypkg', 'echarts_china_cities_pypkg',
     'echarts-china-cities-js'],
    ['echarts-united-kingdom-pypkg', 'echarts_united_kingdom_pypkg',
     'echarts-united-kingdom-js']
]

PACKAGE_INFO_LOOKUP = {
    item[0]: {k: v for k, v in zip(_INFO_FIELDS, item[1:])} for item in
    _PACKAGE_RAW
    }


def install_(package_name):
    info = PACKAGE_INFO_LOOKUP.get(package_name, None)
    if not info:
        print('No info found for {}'.format(package_name))
        return

    # This target package must be installed first.
    package_path = os.path.dirname(
        importlib.import_module(info['import_name']).__file__
    )

    node_package_path = os.path.join(package_path, 'resources')

    assert os.path.exists(os.path.join(node_package_path, 'registry.json'))

    extension_path = os.path.join(
        node_package_path, info['extension_dir']
    )
    assert os.path.exists(os.path.join(extension_path, 'main.js'))
    main_entry = '/'.join([info['extension_dir'], 'main'])
    print({
        'PackageName': package_name,
        'PackagePath': package_path,
        'ExtensionDir': extension_path,
        'MainEntry': main_entry
    })

    # _jupyter_install(
    #     package_name=package_name,
    #     package_main=main_entry,
    #     package_installation_path=extension_path
    # )


@click.command()
@click.argument('package_name')
def cli(package_name):
    """
    A simple wrapper for installation API.
    :param package_name:
    :return:
    """
    # pyecharts_cli jupyter_install jupyter_echarts_pypkg
    install_(package_name)
