#Coding utf-8
from flask import Flask, render_template
import requests
import sys

app = Flask(__name__)

@app.route("/")
def index():
    timeData = requests.get("http://"+API_IP+":5000/api")
    currentTime = timeData.json()["time"]
    #currentTime = json.loads(timeData.read())[0]["time"]
    return render_template("index.html", time=currentTime)



if __name__ == "__main__":
    if (len(sys.argv) == 2):
        API_IP = sys.argv[1]

    elif(len(sys.argv) == 1):
        API_IP = "127.0.0.1"

    else:
        print("ERROR: Demasiados parámetros.")

    app.run(debug=True, port=8080)


