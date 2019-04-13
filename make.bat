cd test
nosetests --with-coverage --cover-package pyecharts --cover-package test && cd .. && flake8  --max-complexity 14 --exclude docs --max-line-length 89 --ignore=F401
