import json
from sensors import *


def measurements_json():
    collecting_measurements_json = [
        {"name": "temp", "value": temphumid.temp},
        {"name": "humid", "value": temphumid.humid}
    ]

    all_measurements_json = json.dumps(collecting_measurements_json)
    return all_measurements_json
