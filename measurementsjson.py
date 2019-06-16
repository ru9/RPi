import json
from sensors import *

def measurements_json():
    collectingMeasurementsJson = {
        "temp": temphumid.temp,
        "humid": temphumid.humid
    }
    allMeasurementsJson = json.dumps(collectingMeasurementsJson)
    return allMeasurementsJson