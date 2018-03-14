import codecs


def get_default_rendering_file_content(file_name='render.html'):
    """
    Simply returns the content render.html
    """
    with codecs.open(file_name, 'r', 'utf-8') as f:
        return f.read()
