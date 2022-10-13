# 載入flask物件
from unittest import result
from flask import Flask, request, redirect, render_template, url_for, session

app = Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
)

# 如果沒有設定，app.secret_key，則Flask將不允許您設定或訪問 session 字典。
app.secret_key = "my secret key"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signin", methods=["POST"])
def signin():
    if request.form["account"] == "test" and request.form["pwd"] == "test":
        session["status"] = "login"
        return redirect("member")
    elif request.form["account"] == "" or request.form["pwd"] == "":
        return redirect(url_for('error', message="請輸入帳號、密碼"))
    elif request.form["account"] != "test" or request.form["pwd"] != "test":
        return redirect(url_for('error', message="帳號、或密碼輸入錯誤"))


# 成功頁面
@app.route("/member")
def success():
    if 'status' not in session:
        return redirect("/")
    else:
        return render_template("success.html")

# 失敗頁面+query string
@app.route("/error")
def error():
    message = request.args.get("message")
    return render_template("error.html", result=message)

# 登出後導向首頁
@app.route("/signout")
def signout():
    session.pop('status', None)
    # session['status'] = None
    # session.clear()
    return redirect("/")

# 嘗試過使用post方法，接著用request.form來抓到原輸入字串，但沒辦法帶回url => 可以在思考怎麼做
# 故嘗試透顧js函數直接更改url，接著再用query string的方式帶到其他partial template
@app.route("/square/<value>")
def square(value):
    result = int(value) ** 2
    return render_template("square.html", result=result)

app.run(port=3000)
