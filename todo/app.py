from flask import Flask,request,render_template
import sqlite3

db = sqlite3.connect("tasks.db")
cur = db.cursor()
cur.execute("CREATE table if not exists tasks(name text,date text)")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/tasks")
def tasks():
    name = request.args.get("name")
    date = request.args.get("date")


    db = sqlite3.connect("tasks.db")
    cur = db.cursor()
    if name and date:
        cur.execute("INSERT into tasks(name,date) VALUES(?,?)",(name,date))
    cur.execute("SELECT * from tasks")
    fetch = cur.fetchall()
    db.commit()
    db.close()
    return render_template("table.html",data=fetch)
