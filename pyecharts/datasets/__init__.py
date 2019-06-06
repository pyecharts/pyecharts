import json
import os
import urllib.request

__HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(__HERE, "map_filename.json"), "r", encoding="utf8") as f:
    FILENAMES: dict = json.load(f)

with open(os.path.join(__HERE, "city_coordinates.json"), "r", encoding="utf8") as f:
    COORDINATES: dict = json.load(f)

EXTRA = {}


def register_url(asset_url: str):
    if asset_url:
        registry = asset_url + "/registry.json"
        try:
            contents = urllib.request.urlopen(registry).read()
            contents = json.loads(contents)
        except Exception as e:
            raise e
        files = {}
        pinyin_names = set()
        for name, pinyin in contents["PINYIN_MAP"].items():
            file_name = contents["FILE_MAP"][pinyin]
            files[name] = [file_name, "js"]
            pinyin_names.add(pinyin)

        for key, file_name in contents["FILE_MAP"].items():
            if key not in pinyin_names:
                # English names
                files[key] = [file_name, "js"]

        js_folder_name = contents["JS_FOLDER"]
        if js_folder_name == "/":
            js_file_prefix = f"{asset_url}/"
        else:
            js_file_prefix = f"{asset_url}/{js_folder_name}/"
        EXTRA[js_file_prefix] = files


def register_files(asset_files: dict):
    if asset_files:
        FILENAMES.update(asset_files)


def register_coords(coords: dict):
    if coords:
        COORDINATES.update(coords)
