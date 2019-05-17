import os

here = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(here, "pyecharts", "_version.py")) as f:
    exec(f.read(), about)

os.system("python setup.py bdist_wheel")
os.system("pip uninstall pyecharts -y")
os.system(
    "pip install -U dist/pyecharts-{}-py3-none-any.whl --no-cache-dir".format(
        about["__version__"]
    )
)
