SET FILES=*.py pyecharts/**/*.py test/*.py
lias %FILES% -sp .isort.cfg
pink %FILES%
