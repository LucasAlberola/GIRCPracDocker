#Coding utf-8
from flask import Flask
app = Flask(__name__)


@app.route('/')
def home():
    return "Bienvenido a mi primera API con Flask!"



if __name__ == "__main__":
    app.run(debug=True)