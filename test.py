import os

# older nose
# os.system("nosetests --with-coverage --cover-package pyecharts --cover-package .")

# current nose
os.system(
    "nose2 --with-coverage --coverage pyecharts "
    "--coverage-config .coveragerc -s test"
)

# pytest
os.system("pytest -cov-config=.coveragerc --cov=./ test/")

# flake8 for code linting
os.system("flake8 --exclude=build,example,images --max-line-length=89 --ignore=F401")
