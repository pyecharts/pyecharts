isort $(find pyecharts -name "*.py"|xargs echo) $(find test -name "*.py"|xargs echo) setup.py
black -l 79 pyecharts test
