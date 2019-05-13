import os

from pyecharts.datasets import register_url, EXTRA
from unittest.mock import patch
from nose.tools import eq_


@patch('pyecharts.datasets.urllib.request.urlopen')
def test_register_url(fake):
    with open(os.path.join("test", "fixtures", "registry.json")) as f:
        fake.return_value = f
        register_url('fake_url')
        eq_(EXTRA, {
            'https://echarts-maps.github.io/echarts-china-cities-js/js/':
            {'安庆': ['shape-with-internal-borders/an1_hui1_an1_qing4', 'js']}
        })
