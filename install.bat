python setup.py bdist_wheel
pip uninstall pyecharts -y
pip install -U dist/pyecharts-1.0.0-py2.py3-none-any.whl --no-cache-dir
