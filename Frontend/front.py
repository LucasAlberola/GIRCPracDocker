#Coding utf-8
from flask import Flask, render_template
import requests
import sys

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



if __name__ == "__main__":
    if (len(sys.argv) == 2):
        API_IP = sys.argv[1]

    elif(len(sys.argv) == 1):
        API_IP = "127.0.0.1"

    else:
        print("ERROR: Demasiados parámetros.")

    app.run(debug=True)


