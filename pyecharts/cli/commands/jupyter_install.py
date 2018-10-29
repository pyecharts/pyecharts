# coding=utf8

import codecs
import importlib
import json
import os
from collections import namedtuple

import click


def _get_jupyter_install_api():
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


def _jupyter_install(package_name, package_main, package_installation_path):
    install_nbextension, ConfigManager = _get_jupyter_install_api()
    print("Installing %s to jupyter.." % package_name)
    install_nbextension(
        package_installation_path, symlink=False, user=True
    )
    print("Enabling %s on jupyter.." % package_name)
    cm = ConfigManager()
    cm.update("notebook", {"load_extensions": {package_main: True}})


def _validate_registry(registry_path):
    with codecs.open(registry_path, "r", encoding="utf-8") as f:
        registry = json.load(f)

    required_fields = [
        "FILE_MAP",
        "GITHUB_URL",
        "JS_FOLDER",
        "JUPYTER_URL",
        "PINYIN_MAP",
    ]
    for key in required_fields:
        if key not in registry:
            raise ValueError("{} is missing".format(key))


PackageInfo = namedtuple('PackageInfo',
                         ['package_name', 'import_name', 'extension_dir'])

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

PACKAGE_INFO_LOOKUP = {item[0]: PackageInfo(*item) for item in _PACKAGE_RAW}


def _retrieve_package_info(package_name):
    info = PACKAGE_INFO_LOOKUP.get(package_name, None)
    if not info:
        print('No info found for {}'.format(package_name))
        return

    # This target package must be installed first.
    package_path = os.path.dirname(
        importlib.import_module(info.import_name).__file__
    )

    node_package_path = os.path.join(package_path, 'resources')
    registry_path = os.path.join(node_package_path, 'registry.json')

    assert os.path.exists(registry_path)

    extension_path = os.path.join(
        node_package_path, info.extension_dir
    )
    assert os.path.exists(os.path.join(extension_path, 'main.js'))
    main_entry = '/'.join([info.extension_dir, 'main'])
    return {
        'PackageName': package_name,
        'PackagePath': package_path,
        'RegistryPath': registry_path,
        'ExtensionDir': extension_path,
        'MainEntry': main_entry
    }


@click.command()
@click.argument('package_name')
@click.option('--fake/--no-fake', default=False)
def cli(package_name, fake):
    """
    A simple wrapper for installation API.
    Demo: pye_cli jupyter_install jupyter-echarts-pypkg
    :param package_name:
    :param fake:
    :return:
    """
    package_info = _retrieve_package_info(package_name)
    if fake:
        click.echo(package_info)
    else:
        _validate_registry(package_info['RegistryPath'])
        _jupyter_install(
            package_name=package_name,
            package_main=package_info['MainEntry'],
            package_installation_path=package_info['ExtensionDir']
        )
