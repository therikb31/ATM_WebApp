from flask import Flask, request
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/login", methods=['GET', 'POST'])
def callLogin():
    if request.method == 'POST':
        accountNumber = request.form['accountNumber']
        pin = request.form['pin']
    return render_template("login.html")


@app.route("/create", methods=['GET', 'POST'])
def createAccount():
    return render_template("createAccount.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)