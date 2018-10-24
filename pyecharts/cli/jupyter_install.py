# coding=utf8
import codecs
import json
import os
import warnings

from setuptools.command.install import install

REGISTRY_FILE = "registry.json"
JUPYTER_ENTRY = "JUPYTER_ENTRY"
REGISTRY_KEYS = [
    "FILE_MAP",
    "GITHUB_URL",
    "JS_FOLDER",
    "JUPYTER_URL",
    "PINYIN_MAP",
]


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


def _load_registry_json(file_path):
    with codecs.open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def _validate_registry(registry):
    for key in REGISTRY_KEYS:
        if key not in registry:
            raise InvalidRegistry("%s is missing" % key)


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
            install_nbextension = None
            ConfigManager = None
    return install_nbextension, ConfigManager
