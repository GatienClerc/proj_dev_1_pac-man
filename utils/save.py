# ***********************************************************************************************************************
# Program name:         save.py
# Description:          read setting and save into json
# Author:               Gatien Clerc
# Creation date:        08.09.2026
# Modified by:          -
# Modification date:    -
# Version:              0.1
# ***********************************************************************************************************************
import json
import os

save_file = "config.json"

default_settings = {
    "audio": 70,
    "pixel_size": 3
}


def save(settings):
    with open(save_file, "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=4)


def load():
    if not os.path.exists(save_file):
        save(default_settings)
        return default_settings

    with open(save_file, "r", encoding="utf-8") as file:
        return json.load(file)