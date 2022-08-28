# flaskのインポート
import calendar
import hashlib
import random
from flask import Flask, make_response, redirect, render_template, request, session, url_for
import sqlite3
import datetime

# グローバル変数
YEAR = 2022

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

  if (authentication_session())[0] == -1:
    # セッション認証非完了
    return redirect(url_for('login'))
  else:
    # セッション認証完了
    user_id = authentication_session()[0]
    # SQL操作 [メニューの取得]
    today = datetime.date.today()
    conn = sqlite3.connect("./static/database/kakaria.db")
    cur = conn.cursor()
    SQL='''
    SELECT times.time_str, sets.set_str, food.food_name
    FROM reservation 
      INNER JOIN menu ON reservation.menu_id = menu.menu_id
                    AND  reservation.answer = menu.sets_id
      INNER JOIN sets ON reservation.answer = sets.sets_id
      INNER JOIN times ON menu.times_id = times.times_id
      INNER JOIN food ON menu.food_id = food.food_id
    WHERE reservation.user_id = ? AND menu.date = date(?)
    '''
    cur.execute(SQL, (user_id, today))
    order_list = cur.fetchall()
    print(f"orderlist = {order_list}")
    cur.close()
    conn.close()
    response = make_response(render_template("./index.html", order_list=order_list, today=str(today)))
    return response

@app.route('/ryosyoku_order')
def ryosyoku_order():
  if (authentication_session())[0] != -1:
    # セッション認証完了
    response = make_response(render_template("./ryosyoku_order.html"))
    return response
  else:
    # セッション認証非完了
    return redirect(url_for('login'))

@app.route('/ryosyoku_order/week', methods=["POST", "GET"])
def week():
  if (authentication_session())[0] == -1:
    # セッション認証非完了
    return redirect(url_for('login'))
  # セッション認証完了
  user_id = (authentication_session())[0]
  
  key = request.args.get("key")
  if key != '1' and key != '2':
    # week1,2以外にアクセス
    return redirect(url_for('ryosyoku_order'))

  if request.method == "GET":
    # GET
    # SQL操作
    today = datetime.date.today()
    monday = today - datetime.timedelta(days=today.weekday())
    conn = sqlite3.connect("./static/database/kakaria.db")
    cur = conn.cursor()
    # [メニューの取得]
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

    menu_answer_list = []
    for menu in menu_list:
      # 予約状況の取得
      SQL = '''
      SELECT *
      FROM reservation
        INNER JOIN sets ON reservation.answer = sets.sets_id
      WHERE menu_id = ? AND user_id = ? AND condition = 0 AND sets.set_str = ?
      '''
      cur.execute(SQL, (menu[0], user_id, menu[1]))
      answer = cur.fetchone()
      if answer != None:
        menu_answer_list.append((menu[0], menu[1], menu[2], menu[3], menu[4], "checked"))
      else:
        menu_answer_list.append((menu[0], menu[1], menu[2], menu[3], menu[4], ""))    
      
    cur.close()
    conn.close()
    print(f"menu_anserw_list={menu_answer_list}")
    response = make_response(render_template("./week.html", menu_answer_list=menu_answer_list, key=key))
    return response
  else:
    # POST
    # SQL操作 [メニューの取得]
    today = datetime.date.today()
    monday = today - datetime.timedelta(days=today.weekday())
    conn = sqlite3.connect("./static/database/kakaria.db")
    cur = conn.cursor()
    SQL = '''
    SELECT DISTINCT menu.menu_id 
    FROM menu 
    WHERE date BETWEEN date(?) AND date(?)
    '''
    cur.execute(SQL, (monday + (datetime.timedelta(days=7*(int(key)-1))), monday + (datetime.timedelta(days=7*(int(key)-1) + 6))))
    print(monday + (datetime.timedelta(days=7*(int(key)-1) + 6)))
    menu_id_list = cur.fetchall()
    cur.close()
    conn.close()
    print(f"fetch_menu={menu_id_list}", end="\n")
    for menu_id in menu_id_list:
      # POSTを受け取る
      set = request.form[str(menu_id[0])]

      # SQL操作 []
      conn = sqlite3.connect("./static/database/kakaria.db")
      cur = conn.cursor()
      cur.execute("SELECT sets_id FROM sets WHERE set_str = ?", (set, ))
      set_id = cur.fetchone()

      # 既にデータベースに登録されているか確認
      cur.execute("SELECT * FROM reservation WHERE menu_id = ? AND user_id = ?", (int(menu_id[0]), user_id))
      if cur.fetchone() == None:
        # 未登録
        cur.execute("INSERT INTO reservation(menu_id, user_id, condition, answer) VALUES(?, ?, 0, ?)", (int(menu_id[0]), user_id, int(set_id[0])))
      else:
        # 登録済み
        SQL='''
        UPDATE reservation 
        SET menu_id = ?,
            user_id = ?,
            condition = 0,
            answer = ?
        WHERE menu_id = ? AND user_id = ?
        '''
        cur.execute(SQL, (int(menu_id[0]), user_id, int(set_id[0]), int(menu_id[0]), user_id))
      conn.commit()
      cur.close()
      conn.close()
    return redirect(url_for('ryosyoku_order'))
  

@app.route('/ryosyoku_order/control/result', methods=["POST", "GET"])
def control_result():
  if (authentication_session())[1] == 2:
    # 寮食管理者認証完了
    # SQL操作 [メニューの取得]
    conn = sqlite3.connect("./static/database/kakaria.db")
    cur = conn.cursor()
    SQL='''
    SELECT reservation.menu_id, menu.date, times.time_str, sets.set_str, food.food_name, COUNT(*)
    FROM reservation 
      INNER JOIN menu ON reservation.menu_id = menu.menu_id
                    AND  reservation.answer = menu.sets_id
      INNER JOIN sets ON reservation.answer = sets.sets_id
      INNER JOIN times ON menu.times_id = times.times_id
      INNER JOIN food ON menu.food_id = food.food_id
    GROUP BY reservation.menu_id, menu.date, times.time_str, sets.set_str, food.food_name
    '''
    # WHERE date BETWEEN date(?) AND date(?)
    cur.execute(SQL)
    fetch_reservation = cur.fetchall()
    cur.close()
    conn.close()
    response = make_response(render_template("./control-result.html", reservation_list=fetch_reservation))
    return response
  else:
    return redirect(url_for('login'))


@app.route('/ryosyoku_order/control/input', methods=["POST", "GET"])
def control_input():
  if (authentication_session())[1] == 2:
    # 寮食管理者認証完了
    response = make_response(render_template("./control-input.html"))
    return response
  else:
    return redirect(url_for('login'))

@app.route('/ryosyoku_order/control/input/month', methods=["POST", "GET"])
def month():
  if (authentication_session())[1] != 2:
    # セッション認証非完了
    return redirect(url_for('login'))
  # セッション認証完了
  
  key = request.args.get("key")
  if not(1 <= int(key) <=12) :
    # 1~12月以外にアクセス
    return redirect(url_for('control_input'))

  if request.method == "GET":
    # GET
    max_day = calendar.monthrange(YEAR, int(key))[1]
    menu_list = []
    # SQL操作 [menu_idの最大値を取得]
    conn = sqlite3.connect("./static/database/kakaria.db")
    cur = conn.cursor()
    for count in range(max_day):
      for time in ["朝", "昼", "夜"]:
        SQL = '''
        SELECT menu.sets_id, food.food_name
        FROM menu
          INNER JOIN food ON menu.food_id = food.food_id
          INNER JOIN times ON menu.times_id = times.times_id
        WHERE menu.date = date(?)
          AND times.time_str = ?
        ORDER BY menu.sets_id ASC
        '''
        cur.execute(SQL, (datetime.date(YEAR, int(key), count+1), time))
        food_names = cur.fetchall()
        print(f"food_names={food_names}")
        food_name_list = ["", ""]
        if food_names != None:
          for set, food_name in food_names:
            if set == 0:
              food_name_list[0] = food_name
            elif set == 1:
              food_name_list[1] = food_name
            else:
              continue
        menu_list.append((int(key), count + 1, time, (food_name_list[0], food_name_list[1])))
    cur.close()
    conn.close()
    print(f"menu_list{menu_list}")
    response = make_response(render_template("./month.html", menu_list=menu_list, key=key))
    return response
  else:
    # POST
    max_day = calendar.monthrange(YEAR, int(key))[1]
    menu_list = []
    times = ['朝', '昼', '夜']
    sets = ['A', 'B']
    # POSTを受け取る
    for day in range(max_day):
      for time in times:
        for set in sets:
          # 書式 {{month}}:{{day}}:{{time}}:A:name
          food_name = request.form[f"{key}:{day+1}:{time}:{set}:name"]
          number = request.form[f"{key}:{day+1}:{time}:{set}:number"]
          if food_name != "":
            if number == "":
              number = '0'
            menu_list.append((f"{YEAR}-{int(key):02}-{int(day+1):02}", time, set, food_name, number))
    print(menu_list)
    
    # SQL操作 [menu_idの最大値を取得]
    conn = sqlite3.connect("./static/database/kakaria.db")
    cur = conn.cursor()
    cur.execute("SELECT MAX(menu_id) FROM menu")
    max_menu_id = int(cur.fetchone()[0])
    cur.close()
    conn.close()

    old_date = ""
    old_time = 0
    for date, time, set, food_name, minimum_number in menu_list:
      conn = sqlite3.connect("./static/database/kakaria.db")
      cur = conn.cursor()
      # SQL操作 [メニューに登録]
      cur.execute("SELECT sets_id FROM sets WHERE set_str = ?", (set, ))
      set_id = cur.fetchone()
      cur.execute("SELECT times_id FROM times WHERE time_str = ?", (time, ))
      time_id = cur.fetchone()
      cur.execute("SELECT food_id FROM food WHERE food_name = ?", (food_name, ))
      food_id = cur.fetchone()
      if food_id == None:
        cur.execute("INSERT INTO food(food_name) VALUES(?)", (food_name, ))
        conn.commit()
        cur.execute("SELECT food_id FROM food WHERE food_name = ?", (food_name, ))
        food_id = cur.fetchone()
      
      # 未登録か検索
      cur.execute("SELECT * FROM menu WHERE date = date(?) AND times_id = ? AND sets_id = ?", (date, time_id[0], set_id[0]))
      if cur.fetchone() != None:
        # メニューを更新
        # SQL文
        SQL='''
        UPDATE menu
        SET food_id = ?,
            minimum_number = ? 
        WHERE date = date(?) AND times_id = ? AND sets_id = ?
        '''
        cur.execute(SQL, (food_id[0], minimum_number, date, time_id[0], set_id[0]))
        conn.commit()
        continue
      else:
        if old_date != date or old_time != time_id:
          # menu_idをインクリメント
          max_menu_id += 1
        cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(?, ?, date(?), ?, ?, ?)", (max_menu_id, set_id[0], date, time_id[0], food_id[0], minimum_number))
      conn.commit()
      cur.close()
      conn.close()
      old_date = date
      old_time = time_id
    return redirect(url_for('control_input'))

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
      response = None
      if int(fetch_user[3]) == 2:
        # 寮食の管理者
        # リダイレクト 設定
        response = make_response(redirect(url_for('control_result')))
      if int(fetch_user[3]) == 1:
        # 一般ユーザ
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
戻り値[0]
  -1:認証失敗
   x:user_id
戻り値[1]
   1:一般ユーザ権限
'''
def authentication_session():
  # cookieの取得
  cookie_sessid = request.cookies.get("SESSID")

  # SQL操作[セッションIDの検索]
  conn = sqlite3.connect("./static/database/kakaria.db")
  cur = conn.cursor()
  cur.execute("SELECT user_id FROM session WHERE session_id == ?", (cookie_sessid, ))
  fetch_session = cur.fetchone()
  cur.close()
  conn.close()

  if fetch_session == None:
    # セッション認証非完了
    return (-1, -1)
  else:
    # セッション認証完了
    # SQL操作[セッションIDの検索]
    conn = sqlite3.connect("./static/database/kakaria.db")
    cur = conn.cursor()
    cur.execute("SELECT permission FROM user WHERE user_id == ?", (int(fetch_session[0]), ))
    fetch_permission = cur.fetchone()
    cur.close()
    conn.close()
    return (int(fetch_session[0]), int(fetch_permission[0]))

if __name__ == "__main__":
  app.run(debug=True)