python setup.py bdist_wheel
pip uninstall pyecharts -y
pip install -U dist\pyecharts-1.0.0.tar.gz  --no-cache-dir
