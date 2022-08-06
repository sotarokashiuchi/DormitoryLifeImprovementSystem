# flaskのインポート
from ast import And
import hashlib
import random
from tkinter import Y
from flask import Flask, make_response, redirect, render_template, request, session, url_for
import sqlite3
import datetime

# flaskクラスのインスタンスを作成
app = Flask(__name__)

# routeデコレータを使用し、どのURLが関数の引き金になるべきかをFlaskに伝える
@app.route('/')
def index():
  ##レスポンスデータ
  # HTMLなどのボディーデータを指定
  # return "Hello World"
  # JSONを指定することもできる
  # Jinja2と呼ばれるテンプレートエンジンを使用して
  # 引数のテンプレートファイル内の文字列の置き換えなどを行った後の文字列を返す
  # return render_template("index.html")

  if authentication_session() == 0:
    # セッション認証完了
    response = make_response(render_template("./index.html"))
    return response
  else:
    # セッション認証非完了
    return redirect(url_for('login'))

@app.route('/ryosyoku_order')
def ryosyoku_order():
  if authentication_session() == 0:
    # セッション認証完了
    response = make_response(render_template("./ryosyoku_order.html"))
    return response
  else:
    # セッション認証非完了
    return redirect(url_for('login'))

@app.route('/ryosyoku_order/week', methods=["POST", "GET"])
def week():
  # if authentication_session() != 0:
  #   # セッション認証非完了
  #   return redirect(url_for('login'))
  # セッション認証完了
  key = request.args.get("key")
  today = datetime.date.today()
  print(today)
  print(today.weekday())
  monday = today - datetime.timedelta(days=today.weekday())
  print(monday)
  if key == '1' or key == '2':
    # week1,2
    # SQL操作 [メニューの取得]
    conn = sqlite3.connect("./static/database/kakaria.db")
    cur = conn.cursor()
    SQL = '''
    SELECT menu.menu_id, sets.set_str, menu.date, times.time_str, food.food_name
    FROM menu 
      INNER JOIN sets ON menu.sets_id = sets.sets_id
      INNER JOIN times ON menu.times_id = times.times_id
      INNER JOIN food ON menu.food_id = food.food_id
    WHERE date BETWEEN date(?) AND date(?)
    '''
    cur.execute(SQL, (monday + (datetime.timedelta(days=7*(int(key)-1))), monday + (datetime.timedelta(days=7*(int(key)-1) + 6))))
    print(monday + (datetime.timedelta(days=7*(int(key)-1) + 6)))
    menu_list = cur.fetchall()
    cur.close()
    conn.close()
    print(f"fetch_menu={menu_list}")
  response = make_response(render_template("./week.html", menu_list=menu_list))
  return response


@app.route('/ryosyoku_feeling')
def ryosyoku_feeling():
  response = make_response(render_template("./ryosyoku_feeling.html"))
  return response

@app.route('/bath')
def bath():
  response = make_response(render_template("./bath.html"))
  return response

@app.route('/login', methods=["POST", "GET"])
def login():
  if request.method == "GET":
    # GET
    response = make_response(render_template("./login.html", condition=0))
    return response
  else:
    # POST
    user_name = request.form["user_name"]
    password = request.form["password"]

    # SQL操作
    conn = sqlite3.connect("./static/database/kakaria.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE user_name == ?", (user_name, ))
    fetch_user = cur.fetchone()
    cur.close()
    conn.close()
    
    if (fetch_user == None) or (str(fetch_user[2]) != password_hash(str(password))):
      # 入力ミス
      response = make_response(render_template("./login.html", condition=1))
      return response
    else:
      # 認証成功
      # リダイレクト 設定
      response = make_response(redirect(url_for('index')))
      # cookie 設定
      max_time = 30 * (60 * 60 * 24)
      expires = int(datetime.datetime.now().timestamp()) + max_time
      sesssid = create_sessid(str(fetch_user[0]))
      response.set_cookie("SESSID", value=sesssid, expires=expires)
      return response

@app.route('/sinup', methods=["POST", "GET"])
def sinup():
  if request.method == "GET":
    # GET
    response = make_response(render_template("./sinup.html"))
    return response
  else:
    # POST
    user_name = request.form["user_name"]
    password = request.form["password"]

    # SQL操作
    conn = sqlite3.connect("./static/database/kakaria.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE user_name == ?", (user_name, ))
    fetch_user = cur.fetchone()
    cur.close()
    conn.close()
    if fetch_user != None:
      # すでに同じユーザ名が登録されている場合
      response = make_response(render_template("./login.html", condition=1))
      return response
    else:
      # パスワードのハッシュ化
      password_sh = password_hash(str(password))
      # SQL操作
      conn = sqlite3.connect("./static/database/kakaria.db")
      cur = conn.cursor()
      cur.execute("INSERT INTO user(user_name, password, permission) VALUES(?, ?, 1)", (user_name, password_sh))
      conn.commit()
      cur.close()
      conn.close()
      # 新規会員登録完了
      return redirect(url_for('sinup_complete'))

@app.route('/change_password', methods=["POST", "GET"])
def change_password():
  if request.method == "GET":
    # GET
    response = make_response(render_template("./change_password.html", condition=0))
    return response
  else:
    # POST
    user_name = request.form["user_name"]
    old_password = request.form["old_password"]
    new_password = request.form["new_password"]

    # SQL操作
    conn = sqlite3.connect("./static/database/kakaria.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE user_name == ? AND password == ?", (user_name, password_hash(str(old_password))))
    fetch_user = cur.fetchone()
    cur.close()
    conn.close()

    if fetch_user == None:
      # 入力ミス
      response = make_response(render_template("./change_password.html", condition=1))
      return response
    else:
      # パスワードの変更
      # SQL操作
      conn = sqlite3.connect("./static/database/kakaria.db")
      cur = conn.cursor()
      cur.execute("UPDATE user SET password = ? WHERE user_name == ? AND password == ?", (password_hash(str(new_password)), user_name, password_hash(str(old_password))))
      cur.close()
      conn.commit()
      conn.close()
      return redirect(url_for('index'))

@app.route('/sinup_complete')
def sinup_complete():
  response = make_response(render_template("./sinup_complete.html"))
  return response


# パスワードのハッシュ化
def password_hash(password):
  print("password_hash()")
  # .encode()でbyte列に変更 .hexdigest()で16進数で保存
  password_sh = hashlib.sha256(password.encode()).hexdigest()
  print(f"\treturn {password_sh=}")
  return password_sh

# セッションIDの生成
def create_sessid(user_id):
  print("create_sessid()")
  while True:
    sessid = str(user_id) + str(random.uniform(-100000, 100000)) + str(datetime.datetime.now())
    sessid = hashlib.sha256(sessid.encode()).hexdigest()

    # SQL操作
    conn = sqlite3.connect("./static/database/kakaria.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM session WHERE session_id == ?", (sessid, ))
    fetch_session = cur.fetchone()
    cur.close()
    conn.close()
    if fetch_session == None:
      # 一意制約に違反していない
      break
  
  # SQL操作 [セッションID追加]
  conn = sqlite3.connect("./static/database/kakaria.db")
  cur = conn.cursor()
  cur.execute("INSERT INTO session(session_id, user_id) VALUES(?, ?)", (str(sessid), user_id))
  conn.commit()
  cur.close()
  conn.close()
  
  print(f"\treturn {sessid=}")
  return sessid

# セッション認証
'''
戻り値0:認証成功
戻り値1:認証失敗
'''
def authentication_session():
  # cookieの取得
  cookie_sessid = request.cookies.get("SESSID")

  # SQL操作[セッションIDの検索]
  conn = sqlite3.connect("./static/database/kakaria.db")
  cur = conn.cursor()
  cur.execute("SELECT * FROM session WHERE session_id == ?", (cookie_sessid, ))
  fetch_session = cur.fetchone()
  cur.close()
  conn.close()

  if fetch_session == None:
    # セッション認証非完了
    return 1
  else:
    # セッション認証完了
    return 0

if __name__ == "__main__":
  app.run(debug=True)