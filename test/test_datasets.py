import os
import unittest
from unittest.mock import patch

from pyecharts.datasets import (
    EXTRA,
    FuzzyDict,
    register_url,
    register_files,
    register_coords,
)


class TestDatasets(unittest.TestCase):

    @patch("pyecharts.datasets.urllib.request.urlopen")
    def test_register_url(self, fake):
        current_path = os.path.dirname(__file__)
        fake_registry = os.path.join(current_path, "fixtures", "registry.json")
        file_name = ["shape-with-internal-borders/an1_hui1_an1_qing4", "js"]
        with open(fake_registry, encoding="utf8") as f:
            fake.return_value = f
            register_url("http://register.url/is/used")
            # set maxDiff
            self.assertEqual.__self__.maxDiff = None
            self.assertEqual(
                EXTRA["http://register.url/is/used/js/"],
                {
                    "安庆": file_name,
                    "English Name": file_name,
                },
            )

        fake_registry_1 = os.path.join(current_path, "fixtures", "registry_1.json")
        with open(fake_registry_1, encoding="utf8") as f:
            fake.return_value = f
            register_url("http://register.url/is/used")
            self.assertEqual(
                EXTRA["http://register.url/is/used/"],
                {
                    "安庆": file_name,
                    "English Name": file_name,
                },
            )

    # TODO: Github Workflow cannot test it well...Fix it future...
    # def test_register_url_error():
    #     try:
    #         register_url("http://127.0.0.1")
    #     except (urllib.error.HTTPError, ConnectionRefusedError) as err:
    #         assert_in(type(err), [urllib.error.HTTPError, ConnectionRefusedError])

    def test_register_url_error(self):
        try:
            register_url("error_asset_url")
        except ValueError as err:
            self.assertIn(type(err), [ValueError])

    def test_fuzzy_search_dict(self):
        fd = FuzzyDict()
        fd.update({"我是北京市": [1, 2]})
        self.assertEqual(fd["我是北京"], [1, 2])

    def test_fuzzy_search_key_error(self):
        with self.assertRaises(KeyError):
            fd = FuzzyDict()
            fd.cutoff = 0.9
            _ = fd["我是北京"]

    def test_register_files(self):
        register_files(asset_files={"x": 1})

    def test_register_coords(self):
        register_coords(coords={"深圳": [113, 23]})

    def test_type_error_with_non_string_key(self):
        fd = FuzzyDict()
        fd[1] = "one"
        fd[2] = "two"

        result = fd._search("1")
        self.assertFalse(result[0])  # Ensure no match found

    def test_type_error_with_non_string_lookfor(self):
        fd = FuzzyDict()
        fd["one"] = 1
        fd["two"] = 2

        with self.assertRaises(KeyError):
            _ = fd[1]
