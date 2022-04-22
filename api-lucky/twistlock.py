

import datetime
import json

from configuration import config
import requests


def call_twistlock_defenders():
    url = config["TWISTLOCK_URL"]
    if(url == "") or (url is None):
        return {
            "message": "Please set the TWISTLOCK_URL in the config.json file!"
        }
    url = url + "/defenders"
    response = requests.get(url=url, headers={'Content-Type': 'application/json', "Authorization": "Bearer " + config["TWISTLOCK_TOKEN"]}, verify=False)
    defenders = json.loads(response.text)

    hostnames =""
    for defender in defenders:
        hostnames = hostnames + defender["hostname"] + "/" + defender["cluster"] + ", "

    return {
        "message": "I'm happy to get Twistlock Defenders! Number of defenders are: "+ str(len(defenders)) + ". Here is hostname/cluster details: " +hostnames +" . I'm the security geek <3 "
    }