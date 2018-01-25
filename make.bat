cd test
nosetests --with-coverage --cover-package pyecharts --cover-package test && cd .. && flake8 --exclude docs --builtins=unicode,xrange,long