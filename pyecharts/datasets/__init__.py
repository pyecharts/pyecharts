# coding=utf-8
import json
import os
import urllib.request


__HERE = os.path.abspath(os.path.dirname(__file__))
EXTRA = {}
with open(os.path.join(__HERE, "map_filename.json"), "r", encoding="utf8") as f:
    FILENAMES = json.load(f)

with open(os.path.join(__HERE, "city_coordinates.json"), "r", encoding="utf8") as f:
    COORDINATES = json.load(f)


def register(additional_asset_url):
    contents = urllib.request.urlopen(additional_asset_url + '/registry.json').read()
    contents = json.loads(contents)
    files = {}
    for name, pinyin in contents['PINYIN_MAP'].items():
        file_name = contents['FILE_MAP'][pinyin]
        files[name] = [file_name, 'js']

    EXTRA[contents['GITHUB_URL'] + '/'] = files
