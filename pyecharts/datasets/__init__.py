import json
import os

__HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(__HERE, "map_filename.json"), "r", encoding="utf8") as f:
    FILENAMES = json.load(f)

with open(os.path.join(__HERE, "city_coordinates.json"), "r", encoding="utf8") as f:
    COORDINATES = json.load(f)
