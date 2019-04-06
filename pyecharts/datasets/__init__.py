# coding=utf-8
import json
import os
import urllib.request

from ..commons.types import Optional

__HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(__HERE, "map_filename.json"), "r", encoding="utf8") as f:
    FILENAMES: dict = json.load(f)

with open(os.path.join(__HERE, "city_coordinates.json"), "r", encoding="utf8") as f:
    COORDINATES: dict = json.load(f)

EXTRA = {}


def register_url(asset_url: Optional[str]):
    if asset_url:
        registry = asset_url + "/registry.json"
        try:
            contents = urllib.request.urlopen(registry).read()
            contents = json.loads(contents)
        except Exception as e:
            raise e
        files = {}
        for name, pinyin in contents["PINYIN_MAP"].items():
            file_name = contents["FILE_MAP"][pinyin]
            files[name] = [file_name, "js"]

        EXTRA[contents["GITHUB_URL"] + "/"] = files


def register_files(asset_files: Optional[dict]):
    if asset_files:
        FILENAMES.update(asset_files)


def register_coords(coords: dict):
    if coords:
        COORDINATES.update(coords)
