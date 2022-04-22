import datetime
import json
from flask import Flask
from flask_cors import CORS
import fileops
import twistlock
from configuration import config
import requests


app = Flask(__name__)
CORS(app) # This will enable CORS for all routes

@app.route('/',methods=['GET'])
def default():
    return {
        "message": "Hello World! I'm the Lucky API!"
    }

@app.route('/lucky',methods=['GET'])
def magic():
    url = config["MAGIC_URL"]
    if(url == "") or (url is None):
        return {
            "message": "Please set the MAGIC_URL in the config.json file!"
        }
    response = requests.get(url=url, headers={'Content-Type': 'application/json'})
    deserialized = json.loads(response.text)
    magic_value = deserialized["data"]
    timeString = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fileops.write_to_file(timeString+ " - Magic value is:" + str(magic_value) + "\n")
    return {
        "message": "I'm happy to get magic-number: "+ str(magic_value) +". I'm the luckiest API :)"
    }

@app.route('/defenders',methods=['GET'])
def defenders():
    return twistlock.call_twistlock_defenders() 

@app.route('/read-file',methods=['GET'])
def read_file():
    return {
        "content": fileops.read_from_file()
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)