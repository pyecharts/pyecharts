
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import pyecharts.__version__ as about


setup(
    name=about.__title__,
    version=about.__version__,
    description=about.__description__,
    url=about.__url__,
    author=about.__author__,
    author_email=about.__author_email__,
    license=about.__license__,
    packages=about.__packages__,
    keywords=about.__keywords__,
    install_requires=about.__requires__,
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