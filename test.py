import os

os.system("nosetests --with-coverage --cover-package pyecharts --cover-package")
os.system("flake8 --exclude build --max-line-length 89 --ignore=F401")
