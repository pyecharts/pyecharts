import os
import codecs


def get_default_rendering_file_content(file_name="render.html"):
    """
    Simply returns the content render.html
    """
    with codecs.open(file_name, "r", "utf-8") as f:
        return f.read()


def get_fixture_content(file_name):
    fixture_file = os.path.join("fixtures", file_name)
    with codecs.open(fixture_file, "r", "utf-8") as f:
        return f.read()


def store_fixture_content(file_name, content):
    fixture_file = os.path.join("fixtures", file_name)
    with codecs.open(fixture_file, "w", "utf-8") as f:
        return f.write(content)
