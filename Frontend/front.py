#Coding utf-8
from flask import Flask, render_template
import requests
import sys

app = Flask(__name__)

@app.route("/")
def index():
    timeData = requests.get("http://"+API_IP+":5000/api")
    currentTime = timeData.json()["time"]
    return render_template("index.html", time=currentTime)



if __name__ == "__main__":
    ok = False
    if (len(sys.argv) == 2):
        API_IP = sys.argv[1]
        ok = True

    elif(len(sys.argv) == 1):
        API_IP = "127.0.0.1"
        ok = True

    else:
        print("ERROR: Demasiados parámetros.")

    if ok:
        app.run(host="0.0.0.0", port="8080", debug=True)


