import os
import codecs


def get_default_rendering_file_content(file_name='render.html'):
    """
    Simply returns the content render.html
    """
    with codecs.open(file_name, 'r', 'utf-8') as f:
        return f.read()


def get_fixture(file_name):
    return os.path.join(
        os.path.dirname(__file__),
        "fixtures",
        file_name)
