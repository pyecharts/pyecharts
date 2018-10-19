# coding=utf8
"""
Common API module
"""

__all__ = ["dumps_json", "cast"]

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
        enable_func=enable_func, post_encode_func=post_encode_func, **kwargs
    )
    return encoder.encode(obj)


def cast(seq):
    """
    转换数据序列，将带字典和元组类型的序列转换为 k_lst,v_lst 两个列表

    元组列表
        [(A1, B1), (A2, B2), ...] -->
            k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]
    字典列表
        [{A1: B1}, {A2: B2}, ...] -->
            k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]
    字典
        {A1: B1, A2: B2, ...} -- >
            k_lst[ A[i1, i2...] ], v_lst[ B[i1, i2...] ]

    :param seq:
        待转换的序列
    :return:
    """
    k_lst, v_lst = [], []
    if isinstance(seq, list):
        for s in seq:
            if isinstance(s, tuple):
                _attr, _value = s
                k_lst.append(_attr)
                v_lst.append(_value)
            elif isinstance(s, dict):
                for k, v in s.items():
                    k_lst.append(k)
                    v_lst.append(v)
    elif isinstance(seq, dict):
        for key in sorted(list(seq.keys())):
            k_lst.append(key)
            v_lst.append(seq[key])
    return k_lst, v_lst
