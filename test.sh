cd test
nosetests --with-coverage --cover-package pyecharts --cover-package test && flake8 pyecharts --builtins=unicode,xrange,long
