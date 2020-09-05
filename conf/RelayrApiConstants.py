import json
import os
import pathlib

API_CONSTANTS = {}

path = pathlib.Path(__file__).parent.absolute()
config_json = os.path.join(path,"relayrapi.json")

with open(config_json, "r") as jsonfile:
    API_CONSTANTS = json.load(jsonfile)


