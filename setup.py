#!/usr/bin/env python
#coding=utf-8

from setuptools import setup
from setuptools.command.install import install

try:
    from jupyterpip import cmdclass
except:
    import pip, importlib
    pip.main(['install', 'jupyter-pip']); cmdclass = importlib.import_module('jupyterpip').cmdclass


__title__ = 'pyecharts'
__description__ = 'Python echarts, make charting easier'
__url__ = 'https://github.com/chenjiandongx/pyecharts'
__version__ = '0.1.9.5'
__author__ = 'chenjiandongx'
__author_email__ = 'chenjiandongx@qq.com'
__license__ = 'MIT'
__requires__ = ['pillow', 'jinja2', 'future', 'jupyter-pip']
__packages__ = ['pyecharts', 'pyecharts/charts', 'pyecharts/custom']
__keywords__ = ['echarts', 'charts']
__jupyter_echarts__ = 'pyecharts/templates/js/echarts'


setup(
    name=__title__,
    version=__version__,
    description=__description__,
    url=__url__,
    author=__author__,
    author_email=__author_email__,
    license=__license__,
    packages=__packages__,
    keywords=__keywords__,
    install_requires=__requires__,
    zip_safe=False,
    include_package_data=True,
    cmdclass=cmdclass(__jupyter_echarts__, enable="echarts/main"),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ]
)
