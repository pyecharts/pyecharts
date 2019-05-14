import os
from unittest.mock import patch

from nose.tools import eq_

from pyecharts.datasets import EXTRA, register_url


@patch("pyecharts.datasets.urllib.request.urlopen")
def test_register_url(fake):
    current_path = os.path.dirname(__file__)
    with open(
        os.path.join(current_path, "fixtures", "registry.json"), encoding="utf8"
    ) as f:
        fake.return_value = f
        register_url("fake_url")
        eq_(
            EXTRA,
            {
                "https://echarts-maps.github.io/echarts-china-cities-js/js/": {
                    "安庆": ["shape-with-internal-borders/an1_hui1_an1_qing4", "js"]
                }
            },
        )
