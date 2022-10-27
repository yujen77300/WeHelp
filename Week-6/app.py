# 載入flask物件
from curses.ascii import isdigit
from pickle import TRUE
from sqlite3 import Cursor
from unittest import result
from flask import Flask, request, redirect, render_template, url_for, session
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'website'

# 如果沒有設定，app.secret_key，則Flask將不允許您設定或訪問 session 字典。
app.secret_key = "my secret key"

# 建立資料庫連線
db = MySQL(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if 'account' in request.form and 'pwd' in request.form:
        username = request.form['account']
        password = request.form['pwd']
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "SELECT * FROM member WHERE username=%s AND password=%s", (username, password))
        info = cursor.fetchone()
        if info is not None:
            if info['username'] == username and info['password'] == password:
                # 愈透過session在兩個request中傳遞資訊
                session["status"] = username
                return redirect(url_for('success'))
        else:
            return redirect(url_for('error', message="帳號或密碼輸入錯誤"))


# 成功頁面
# redirect加上參數不能透過post來傳遞，因為會有query string，所以透過session
@app.route("/member")
def success():
    if 'status' not in session:
        return redirect("/")
    else:
        # 取得當前帳號的資訊
        user = session.get('status')
        cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute(
            "SELECT member.username,message.content FROM member inner JOIN message ON member.id = message.member_id")
        info = cur.fetchall()
        # tuple不可更改，故改為list，並用reverse方法讓最晚出現留言較出現在最上面
        info = list(info)
        info.reverse()

        return render_template("success.html", user=user, result=info)


# 失敗頁面+query string
@app.route("/error")
def error():
    message = request.args.get("message")
    return render_template("error.html", result=message)


# 登出後導向首頁
@app.route("/signout")
def signout():
    session.pop('status', None)
    return redirect("/")


# 連結到註冊功能網址
@app.route("/signup", methods=["POST"])
def signup():
    if request.method == 'POST':
        if 'name' in request.form and 'account' in request.form and 'pwd' in request.form:
            name = request.form['name']
            username = request.form['account']
            password = request.form['pwd']
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute(
                "SELECT * FROM member WHERE username=%s", [username])
            info = cur.fetchone()
            if info is not None:
                if info['username'] == username:
                    return redirect(url_for('error', message="帳號已經被註冊"))
            else:
                cur.execute(
                    "INSERT INTO member(name,username,password) VALUES(%s,%s,%s)", (name, username, password))
                # 讓db的異動生效
                db.connection.commit()
                return redirect(url_for('home'))


@app.route("/message", methods=["POST"])
def message():
    comment = request.form['comment']
    user = session.get('status')
    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        "SELECT id FROM member WHERE username=%s;", [user])
    info = cursor.fetchone()
    # 透過session的username，取得紀錄的使⽤者編號memberID
    memberID = (info["id"])

    # 將留言記錄到message資料表
    cursor.execute(
        "INSERT INTO message(member_id,content) VALUES(%s,%s);", (memberID, comment))
    db.connection.commit()
    return redirect(url_for('success'))

app.run(port=3000)
