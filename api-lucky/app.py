import json
from random import Random
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
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
    url = "http://magic-api.apps.openshift.aws.zenigma.com/magic"
    response = requests.get(url=url, headers={'Content-Type': 'application/json'})
    print(response.text)
    deserialized = json.loads(response.text)
    return "I'm happy to get magic-number: "+ str(deserialized["data"]) +". I'm the luckiest API :)"
            
            
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)