from flask import Flask
from flask.templating import render_template
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True,port=8000)
