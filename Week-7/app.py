# 載入flask物件
from curses.ascii import isdigit
from pickle import TRUE
from sqlite3 import Cursor
from unittest import result
from flask import Flask, request, redirect, render_template, url_for, session, jsonify
import mysql.connector

app = Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)

dylan_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="connectionPool",
    pool_size=5,
    pool_reset_session=True,
    host='localhost',
    database='website',
    user='root',
    password='')


# 如果沒有設定，app.secret_key，則Flask將不允許您設定或訪問 session 字典。
app.secret_key = "my secret key"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if 'account' in request.form and 'pwd' in request.form:
        username = request.form['account']
        password = request.form['pwd']
        # 隨便取一個連線來串聯資料庫
        mydb = dylan_pool.get_connection()
        cursor = mydb.cursor()
        cursor.execute(
            "SELECT * FROM member WHERE username=%s AND password=%s", (username, password))
        info = cursor.fetchone()
        if info is not None:
            if info[2] == username and info[3] == password:
                # 愈透過session在兩個request中傳遞資訊
                session["status"] = username
                return redirect(url_for('success'))
        else:
            return redirect(url_for('error', message="帳號或密碼輸入錯誤"))
        # 釋放連線
        cursor.close()
        mydb.close()


# 成功頁面
# redirect加上參數不能透過post來傳遞，因為會有query string，所以透過session
@app.route("/member")
def success():
    if 'status' not in session:
        return redirect("/")
    else:
        # 取得當前帳號的資訊
        user = session.get('status')
        mydb = dylan_pool.get_connection()
        cur = mydb.cursor()
        cur.execute(
            "SELECT member.username,message.content FROM member inner JOIN message ON member.id = message.member_id")
        info = cur.fetchall()
        info.reverse()
        mydb.close()
        cur.close()

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
            mydb = dylan_pool.get_connection()
            cur = mydb.cursor()
            cur.execute(
                "SELECT * FROM member WHERE username=%s", [username])
            info = cur.fetchone()
            if info is not None:
                if info[2] == username:
                    return redirect(url_for('error', message="帳號已經被註冊"))
            else:

                cur.execute(
                    "INSERT INTO member(name,username,password) VALUES(%s,%s,%s)", (name, username, password))
                # 讓db的異動生效
                mydb.commit()
                return redirect(url_for('home'))
            cur.close()
            mydb.close()


@app.route("/message", methods=["POST"])
def message():
    comment = request.form['comment']
    user = session.get('status')
    mydb = dylan_pool.get_connection()
    cursor = mydb.cursor()
    cursor.execute(
        "SELECT id FROM member WHERE username=%s;", [user])
    info = cursor.fetchone()
    # 透過session的username，取得紀錄的使⽤者編號memberID
    memberID = (info[0])
    # 將留言記錄到message資料表
    cursor.execute(
        "INSERT INTO message(member_id,content) VALUES(%s,%s);", (memberID, comment))
    mydb.commit()
    cursor.close()
    mydb.close()
    return redirect(url_for('success'))

# 查詢會籍資料API，修改名稱的API
@app.route("/api/member", methods=["GET", "PATCH"])
def apiMember():
    if request.method == "GET":
        memberData = {}
        # 如果有任何錯誤回傳null
        try:
            # 會員沒有登入回傳null
            if 'status' not in session:
                return jsonify({'data': None})
            else:
                username = request.args.get("username")
                mydb = dylan_pool.get_connection()
                # 到資料庫去找該username的資料
                apiMemberCursor = mydb.cursor()
                apiMemberCursor.execute(
                    "SELECT id, name, username FROM member WHERE username=%s;", [username])
                info = apiMemberCursor.fetchone()
                field_names = [i[0] for i in apiMemberCursor.description]
                # 在字典裏面新增key and values
                for i in range(3):
                    memberData[field_names[i]] = info[i]
        except:
            return jsonify({'data': None})
        finally:
            apiMemberCursor.close()
            mydb.close()
        return jsonify({'data': memberData})
    elif request.method == "PATCH":
        try:
            if 'status' not in session:
                return jsonify({'test': True})
            else:
                # 更新自己的姓名，先取得自己的會員帳號
                user = session.get('status')
                # 使用者自己輸入要改的姓名
                newName = request.get_json()["name"]
                mydb = dylan_pool.get_connection()
                updateCursor = mydb.cursor()
                updateCursor.execute(
                    "UPDATE member SET name=%s WHERE username=%s;", (newName, user))
                mydb.commit()

                return jsonify({'OK': True})
        except:
            return jsonify({'error': True})
        finally:
            updateCursor.close()
            mydb.close()


app.run(port=3000)
