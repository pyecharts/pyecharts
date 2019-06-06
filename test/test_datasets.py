import os
from unittest.mock import patch

from nose.tools import eq_

from pyecharts.datasets import EXTRA, register_url


@patch("pyecharts.datasets.urllib.request.urlopen")
def test_register_url(fake):
    current_path = os.path.dirname(__file__)
    fake_registry = os.path.join(current_path, "fixtures", "registry.json")
    with open(fake_registry, encoding="utf8") as f:
        fake.return_value = f
        register_url("http://register.url/is/used")
        eq_(
            EXTRA,
            {
                "http://register.url/is/used/js/": {
                    "安庆": ["shape-with-internal-borders/an1_hui1_an1_qing4", "js"],
                    "English Name": [
                        "shape-with-internal-borders/an1_hui1_an1_qing4",
                        "js",
                    ],
                }
            },
        )
