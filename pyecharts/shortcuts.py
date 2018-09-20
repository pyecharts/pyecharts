# coding=utf8
"""
Common API module
"""

from pyecharts.javascripthon.api import MyJSONEncoder


def dumps_json(obj, enable_func=False, post_encode_func=None, **kwargs):
    """A simple wrapper for json.dumps
    :param obj:
    :param enable_func:
    :param post_encode_func
    :param kwargs:
    :return:
    """
    encoder = MyJSONEncoder(
        enable_func=enable_func,
        post_encode_func=post_encode_func,
        **kwargs
    )
    return encoder.encode(obj)
