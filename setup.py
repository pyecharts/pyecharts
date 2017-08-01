#!/usr/bin/env python
#coding=utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__title__ = 'pyecharts'
__description__ = 'Python echarts, make charting easier'
__url__ = 'https://github.com/chenjiandongx/pyecharts'
__version__ = '0.1.9.1'
__author__ = 'chenjiandongx'
__author_email__ = 'chenjiandongx@qq.com'
__license__ = 'MIT'
__requires__ = ['pprint', 'Image', 'jinja2', 'future']
__packages__ = ['pyecharts', 'pyecharts/charts']
__keywords__ = ['echarts', 'charts']


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
