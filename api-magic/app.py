from random import Random
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # This will enable CORS for all routes

@app.route('/',methods=['GET','POST'])
def default():
    return {
        "message": "Hello World! I'm the Magic API!"
    }

@app.route('/magic',methods=['GET','POST'])
def magic():
    randomizer = Random()
    return {
        "message": "Hey I'm the Magic API! Please look data field for the magic number!",
        "data": randomizer.randint(1, 5000)
    }


            
            
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)