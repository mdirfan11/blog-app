from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1> Hello world!!!<h1>"

@app.route("/index1")
def index():
    return render_template("index.html")

#Custom Error pages
#Page not foune error
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal server error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
