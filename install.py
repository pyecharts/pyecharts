import os

here = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(here, "pyecharts", "_version.py")) as f:
    exec(f.read(), about)

UNINSTALL = "{} uninstall pyecharts -y"
INSTALL = "{} install -U dist/pyecharts-{}-py3-none-any.whl --no-cache-dir"

os.system("python setup.py bdist_wheel")
os.system(UNINSTALL.format("pip"))
os.system(UNINSTALL.format("pip3"))
os.system(INSTALL.format("pip", about["__version__"]))
os.system(INSTALL.format("pip3", about["__version__"]))
