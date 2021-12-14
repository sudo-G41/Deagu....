from flask import Flask, request, redirect
import random as rd
import sqlite3
app = Flask(__name__)

@app.route("/")
def index():
    con = sqlite3.connect("data2.db")
    Cursor = con.cursor()
    Cursor.execute("SELECT * FROM topic")
    rows = Cursor.fetchall()
    liTag = ''
    for row in rows:
        liTag = liTag+ f'<li><a href = "/read/{row[0]}">{row[1]}</a></li>'
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>WEB</title>
    </head>
    <body>
        <h1><a href="/">WEB</a></h1>
        <ol>
            {liTag}
        </ol>
        <h2>Welcome</h2>
        Hello WEB
        <ul>
            <li><a href="/create">create</a></li>
        </ul>
    </body>
    </html>
    """

@app.route("/read/<id>/")
def read(id):
    con = sqlite3.connect("data2.db")
    Cursor = con.cursor()
    Cursor.execute("SELECT * FROM topic")
    rows = Cursor.fetchall()
    liTag = ''
    for row in rows:
        liTag = liTag+ f'<li><a href = "/read/{row[0]}">{row[1]}</a></li>'
    Cursor.execute("SELECT * FROM topic WHERE id = ?", (id,))
    topic = Cursor.fetchone()
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{topic[1]}</title>
    </head>
    <body>
        <h1><a href="/">WEB</a></h1>
        <ol>
            {liTag}
        </ol>
        <h2>{topic[1]}</h2>
        {topic[2]}
        <ul>
            <li><a href="/create">create</a></li>
            <li>
                <form action="/delete/{id}" method="post">
                        <input type="submit" value="삭제">
                </form>
                <li><a href="/update/{id}">update</a></li>
            </li>
        </ul>
    </body>
    </html>
    """
@app.route("/create/")
def c():
    con = sqlite3.connect("data2.db")
    Cursor = con.cursor()
    Cursor.execute("SELECT * FROM topic")
    rows = Cursor.fetchall()
    liTag = ''
    for row in rows:
        liTag = liTag+ f'<li><a href = "/read/{row[0]}">{row[1]}</a></li>'
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>WEB</title>
    </head>
    <body>
        <h1><a href="/">WEB</a></h1>
        <ol>
            {liTag}
        </ol>

        <form action="/create_precess" method="post">
            <p><input type="text" placeholder="title" name="title"></p>
            <p><input type="text" placeholder="body" name="body"></p>
            <p><input type="submit" value="생성"></p>
        </form>

        <ul>
            <li><a href="/create">create</a></li>
        </ul>
    </body>
    </html>
    """
@app.route("/update/<id>/")
def update(id):
    con = sqlite3.connect("data2.db")
    Cursor = con.cursor()
    Cursor.execute("SELECT * FROM topic WHERE id = ?", (id,))
    topic = Cursor.fetchone()
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{topic[1]}</title>
    </head>
    <body>
        <form action="/update_process/{id}" method="post">
            <p><input type="text" placeholder="title" name="title" value="{topic[1]}"></p>
            <p><input type="text" placeholder="body" name="body" value="{topic[2]}"></p>
            <p><input type="submit" value="수정"></p>
        </form>
    </body>
    </html>
    """
@app.route("/create_precess", methods=["POST"])
def create_precess():
    title = request.form.get("title")
    body = request.form.get("body")
    print(title,body)
    sql = "INSERT INTO topic (title, body) VALUES(?, ?)"
    con = sqlite3.connect("data2.db")
    Cursor = con.cursor()
    Cursor.execute(sql, [title, body])
    con.commit()
    return redirect(f"/read/{Cursor.lastrowid}")

@app.route("/delete/<id>", methods=["POST"])
def delete(id):
    con = sqlite3.connect("data2.db")
    Cursor = con.cursor()
    sql = "DELETE FROM topic WHERE id = ?"
    Cursor.execute(sql, [id])
    con.commit()
    return redirect(f"/")

@app.route("/update_process/<id>", methods=["POST"])
def update_preoess(id):
    title = request.form.get("title")
    body = request.form.get("body")
    con = sqlite3.connect("data2.db")
    Cursor = con.cursor()
    sql = "UPDATE topic SET title = ?, body = ? WHERE id = ?"
    Cursor.execute(sql, [title, body, id])
    con.commit()
    return redirect(f"/")

app.run(debug=True,host="0.0.0.0",port="8000")