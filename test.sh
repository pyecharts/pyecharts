cd test
nosetests --with-coverage --cover-package pyecharts --cover-package test && cd .. && flake8 --max-complexity 12 --exclude docs --builtins=unicode,xrange,long,basestring
