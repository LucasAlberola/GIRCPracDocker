#Coding utf-8
from flask import Flask
import json
import time
 
app = Flask(__name__)


@app.route('/')
def home():
    return "Bienvenido a mi primera API con Flask!"


@app.route("/api", methods=["GET"])
def apiGet():
    currentTime = time.time()
    dataDict = {
        "time": currentTime
    }

    jsonData = json.dumps(dataDict)
    return jsonData

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="5000",debug=True)