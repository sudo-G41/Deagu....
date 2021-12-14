from flask import Flask
import random as rd
import sqlite3
app = Flask(__name__)

@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>WEB</title>
    </head>
    <body>
        <h1><a href="index.html">WEB</a></h1>
        <ol>
            <li><a href="1.html">html</a></li>
            <li><a href="2.html">css</a></li>
            <li><a href="3.html">js</a></li>
        </ol>
        <h2>Welcome</h2>
        Hello WEB
    </body>
    </html>
    """

@app.route("/read/<id>/")
def read(id):
    return "Read"+id
@app.route("/create/")
def c():
    return "create"

app.run(debug=True,host="0.0.0.0",port="8000")