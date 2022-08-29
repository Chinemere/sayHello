import imp
from flask import Flask, render_template, request, flash, url_for
app = Flask(__name__)
app.secret_key = b"see you there"

@app.route("/hello")
def index():
    flash("what is your name")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi "+ str(request.form["name_input"]) + ",  Great to see you! " )
    return render_template("index.html")
       



if __name__== "__main__":
    app.run(host="127.0.0.1", port=9000, debug=True)