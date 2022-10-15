# flaskのインポート
import calendar
import hashlib
import random
from traceback import print_tb
from flask import Flask, make_response, redirect, render_template, request, session, url_for
import sqlite3
import datetime

# グローバル変数
# 現在の西暦を指定
YEAR = 2022
# 寮食予約システム 予約受付終了時間(日)
UPDATE = 3
# お風呂の入浴時間(分)
BATH_MAX = 20
TTL = 5

# flaskクラスのインスタンスを作成
app = Flask(__name__)

# routeデコレータを使用し、どのURLが関数の引き金になるべきかをFlaskに伝える
# トップページ
@app.route('/')
def index():
  ##レスポンスデータ
  # HTMLなどのボディーデータを指定
  # return "Hello World"
  # JSONを指定することもできる
  # Jinja2と呼ばれるテンプレートエンジンを使用して
  # 引数のテンプレートファイル内の文字列の置き換えなどを行った後の文字列を返す
  # return render_template("index.html")

  # セッション認証
  if authentication_redirect() != None:
    # 認証拒否
    return authentication_redirect()
    
  user_id = authentication_session()[0]
  today = datetime.date.today()
  conn = sqlite3.connect("./static/database/kakaria.db")
  cur = conn.cursor()
  
  # [本日の予約済みメニューを取得]
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

# 寮食予約システム > トップ
@app.route('/ryosyoku_order')
def ryosyoku_order():
  # セッション認証
  if authentication_redirect() != None:
    # 認証拒否
    return authentication_redirect()

  response = make_response(render_template("./ryosyoku_order.html"))
  return response

# 寮食予約システム > 入力ページ
@app.route('/ryosyoku_order/week', methods=["POST", "GET"])
def week():
  # セッション認証
  if authentication_redirect() != None:
    return authentication_redirect()
  user_id = (authentication_session())[0]
  
  # クエリストリング取得
  key = request.args.get("key")
  if key != '1' and key != '2':
    # week1,2以外にアクセス
    return redirect(url_for('ryosyoku_order'))

  if request.method == "GET":
    # GET
    today = datetime.date.today()
    monday = today - datetime.timedelta(days=today.weekday())
    start_day = [monday.month, monday.day]
    end_day = [(monday + (datetime.timedelta(days=6))).month, (monday + (datetime.timedelta(days=6))).day]
    print(start_day)
    conn = sqlite3.connect("./static/database/kakaria.db")
    cur = conn.cursor()
    
    # [該当メニューの取得]
    SQL = '''
    SELECT menu.menu_id, sets.set_str, menu.date, times.time_str, food.food_name
    FROM menu 
      INNER JOIN sets ON menu.sets_id = sets.sets_id
      INNER JOIN times ON menu.times_id = times.times_id
      INNER JOIN food ON menu.food_id = food.food_id
    WHERE date BETWEEN date(?) AND date(?)
      AND menu.menu_id IN (
        SELECT DISTINCT menu_id
        FROM reservation
        WHERE user_id = ?
          AND condition <> 1
      )
    ORDER BY menu.date ASC, menu.times_id ASC, menu.sets_id ASC
    '''
    cur.execute(SQL, (monday + (datetime.timedelta(days=7*(int(key)-1))), monday + (datetime.timedelta(days=7*(int(key)-1) + 6)), user_id))
    print(monday + (datetime.timedelta(days=7*(int(key)-1) + 6)))
    menu_list = cur.fetchall()

    menu_answer_list = []
    for menu in menu_list:
      # [現在の予約状況を取得]
      SQL = '''
      SELECT *
      FROM reservation
        INNER JOIN sets ON reservation.answer = sets.sets_id
      WHERE menu_id = ? AND user_id = ? AND sets.set_str = ?
      '''
      cur.execute(SQL, (menu[0], user_id, menu[1]))
      answer = cur.fetchone()
      
      # フォーマットに整える
      if answer != None:
        menu_answer_list.append((menu[0], menu[1], menu[2], menu[3], menu[4], "checked"))
      else:
        menu_answer_list.append((menu[0], menu[1], menu[2], menu[3], menu[4], ""))
      
    cur.close()
    conn.close()
    print(f"menu_anserw_list={menu_answer_list}")
    response = make_response(render_template("./week.html", menu_answer_list=menu_answer_list, key=key, start_day=start_day, end_day=end_day))
    return response
  else:
    # POST
    # SQL操作 [メニューの取得]
    today = datetime.date.today()
    monday = today - datetime.timedelta(days=today.weekday())
    conn = sqlite3.connect("./static/database/kakaria.db")
    cur = conn.cursor()
    
    # [該当メニューの取得]
    SQL = '''
      SELECT DISTINCT menu_id
      FROM reservation
      WHERE user_id = ?
        AND condition <> 1
        AND menu_id IN (
          SELECT DISTINCT menu.menu_id 
          FROM menu 
          WHERE date BETWEEN date(?) AND date(?)
        )
      
    '''
    cur.execute(SQL, (user_id, monday + (datetime.timedelta(days=7*(int(key)-1))), monday + (datetime.timedelta(days=7*(int(key)-1) + 6))))
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
        cur.execute("INSERT INTO reservation(menu_id, user_id, condition, answer) VALUES(?, ?, 2, ?)", (int(menu_id[0]), user_id, int(set_id[0])))
        conn.commit()
      else:
        # 登録済み
        SQL='''
        UPDATE reservation 
        SET condition = 2,
            answer = ?
        WHERE menu_id = ? AND user_id = ?
        '''
        cur.execute(SQL, (int(set_id[0]), int(menu_id[0]), user_id))
        conn.commit()
      # 最小個数成立確認
      # [未入力者数]
      SQL = '''
      SELECT COUNT(*)
      FROM reservation
      WHERE menu_id = ?
        AND condition = 0
      '''
      cur.execute(SQL, (menu_id[0], ))
      notcomplete_people = cur.fetchone()
      print(f"未入力者数合計 notcomplete_people = {notcomplete_people}")

      # [セット別入力者数]
      SQL = '''
      SELECT answer, COUNT(*)
      FROM reservation
      WHERE condition = 2
      GROUP BY menu_id, answer
        HAVING  menu_id = ?
      '''
      cur.execute(SQL, (menu_id[0], ))
      complete_peoples = cur.fetchall()
      print(f"セット別入力者数 complete_peoples = {complete_peoples}")

      # [セット別最小個数] // 昇順にしなダメ？
      SQL = '''
      SELECT sets_id, minimum_number
      FROM menu
      WHERE menu_id = ?
      '''
      cur.execute(SQL, (menu_id[0], ))
      minimum_numbers = cur.fetchall()
      print(f"minimum_numbers = {minimum_numbers}")

      # minimum_numbers.append((-1, -1))
      # complete_peoples.append((-1, -1))
      complete_people = 0
      minimum_number = 0
      people_count = 0
      # complete_peoples_index = 0
      
      minimum_number_list = []
      for minimum_number_set, minimum_number in minimum_numbers:
        minimum_number_list.append(minimum_number_set)
      minimum_number_list.sort()
      
      complete_people_list = []
      for complete_people_set, complete_people in complete_peoples:
        complete_people_list.append(complete_people_set)

      for index in minimum_number_list:
        if not(index in complete_people_list):
          complete_peoples.append((index, 0))
      complete_peoples.sort()

      for count, minimum_number_t in enumerate(minimum_numbers):
        minimum_number = minimum_number_t[1]
        complete_people = complete_peoples[count][1]
        
        if complete_people < minimum_number:
          print(f"A menu_id = {menu_id[0]}")
          # 入力者が最小個数に達していない
          people_count += minimum_number - complete_people
          print(f"people_count = {people_count}")
      if people_count != 0 and people_count == notcomplete_people[0]:
        print("B")
        # 不足最小個数と未入力者が釣り合う(確定する時)
        # [データ更新]
        SQL = '''
          SELECT user_id
          FROM reservation
          WHERE menu_id = ?
            AND condition = 0
        '''
        cur.execute(SQL, (menu_id[0], ))
        user_id_lists = cur.fetchall()
        print(f"user_id_lists = {user_id_lists}")

        for count, complete_people in enumerate(complete_peoples):
          while minimum_numbers[count][0] != complete_people[0]:
            count += 1
          minimum_number = minimum_numbers[count][1]
          if complete_people[1] < minimum_number:
            print("C")
            # 入力者が最小個数に達していない
            for _ in range(minimum_number - complete_people[1]):
              SQL = '''
                UPDATE reservation
                SET condition = 1,
                    answer = ?
                WHERE menu_id = ?
                  AND user_id = ?
              '''
              user_id_list = user_id_lists.pop()
              print(f"user_id_list = {user_id_list}")
              cur.execute(SQL, (complete_people[0], menu_id[0], user_id_list[0]))
              conn.commit()
        
        # conditionを1に変更
        SQL = '''
          UPDATE reservation
          SET condition = 1
          WHERE menu_id = ?
        '''
        cur.execute(SQL, (menu_id[0], ))
        conn.commit()
      
      # 全入力者確認
      SQL = '''
      SELECT COUNT(*)
      FROM reservation
      WHERE menu_id = ?
        AND condition = 0
      '''
      cur.execute(SQL, (menu_id[0], ))
      notinput_f = cur.fetchone()
      print(notinput_f)
      if notinput_f[0] == 0:
        SQL = '''
          UPDATE reservation
          SET condition = 1
          WHERE menu_id = ?
        '''
        cur.execute(SQL, (menu_id[0], ))
        conn.commit()

      cur.close()
      conn.close()
    return redirect(url_for('order_complete'))

# 寮食予約システム > 入力完了ページ
@app.route('/ryosyoku_order/order_complete')
def order_complete():
  # セッション認証
  if authentication_redirect() != None:
    # 認証拒否
    return authentication_redirect()

  response = make_response(render_template("./order_complete.html"))
  return response

# 寮食予約システム > 管理者ページ > 入力結果
@app.route('/ryosyoku_order/control/result', methods=["POST", "GET"])
def control_result():
  if (authentication_session())[1] != 2:
    # セッション認証非完了
    return redirect(url_for('login'))
  # セッション認証完了
  # SQL操作 [メニューの取得]
  conn = sqlite3.connect("./static/database/kakaria.db")
  cur = conn.cursor()
  SQL = '''
  SELECT menu.menu_id, menu.date, times.time_str, sets.set_str, food.food_name, COUNT(*)
  FROM menu
    LEFT OUTER JOIN reservation ON menu.menu_id = reservation.menu_id
                               AND menu.sets_id = reservation.answer
    INNER JOIN sets ON menu.sets_id = sets.sets_id
    INNER JOIN times ON menu.times_id = times.times_id
    INNER JOIN food ON menu.food_id = food.food_id
  WHERE reservation.condition <> 0 OR reservation.condition IS NULL
  GROUP BY menu.menu_id, menu.sets_id, menu.date, times.time_str, sets.set_str, food.food_name
  '''
  SQL = '''
  SELECT menu_id, sets_id
  FROM menu
  WHERE date BETWEEN date("2022-10-01") AND date("2022-12-01")
  '''
  cur.execute(SQL)
  fetch_reservation = cur.fetchall()

  reservation_list = []
  old_menu = None
  first_menu = None
  print(f"fetch_reservation = {fetch_reservation}")
  for menu_id, set_id in fetch_reservation:
    SQL = '''
    SELECT sets.set_str, food.food_name, COUNT(*)
    FROM menu
      INNER JOIN reservation ON menu.menu_id = reservation.menu_id
                            AND menu.sets_id = reservation.answer
      INNER JOIN sets ON menu.sets_id = sets.sets_id
      INNER JOIN food ON menu.food_id = food.food_id
    WHERE reservation.condition <> 0
      AND reservation.menu_id = ?
      AND reservation.answer = ?
    GROUP BY menu.menu_id, menu.sets_id, food.food_name
    '''
    cur.execute(SQL, (menu_id, set_id))
    count_people = cur.fetchone()
    print(f"count_people = {count_people}")
    if old_menu == menu_id:
      # 同じ日付
      # SQL操作 [メニューの取得]
      conn = sqlite3.connect("./static/database/kakaria.db")
      cur = conn.cursor()
      # 
      SQL='''
      SELECT COUNT(*)
      FROM reservation 
      WHERE menu_id == ?
        AND condition == 0
      '''
      cur.execute(SQL, (menu_id, ))
      not_write = cur.fetchone()[0]
      
      # 
      SQL = '''
      SELECT DISTINCT menu.date, times.time_str
      FROM menu
        INNER JOIN times ON menu.times_id = times.times_id
      WHERE menu.menu_id = ?
      '''
      cur.execute(SQL, (menu_id, ))
      date_time = cur.fetchone()
      #   {% for date, time, set, food_name, people_count, not_write in reservation_list %}
      if count_people != None:
        reservation_list.append((date_time[0], date_time[1], (first_menu[0], count_people[0]), (first_menu[1], count_people[1]), (first_menu[2], count_people[2]), not_write))
      else:
        reservation_list.append((date_time[0], date_time[1], (first_menu[0], ""), (first_menu[1], ""), (first_menu[2], ""), not_write))
    else:
      # 新しい日付
      if count_people != None:
        first_menu = [count_people[0], count_people[1], count_people[2]]
      else:
        first_menu = ["", "", ""]
    old_menu = menu_id
  print(f"reservation_list = {reservation_list}")
  cur.close()
  conn.close()
  response = make_response(render_template("./control-result.html", reservation_list=reservation_list))
  return response

# 寮食予約システム > 管理者 > 献立トップページ
@app.route('/ryosyoku_order/control/input', methods=["POST", "GET"])
def control_input():
  if (authentication_session())[1] != 2:
    # セッション認証非完了
    return redirect(url_for('login'))
  # セッション認証完了
  response = make_response(render_template("./control-input.html"))
  return response

# 寮食予約システム > 管理者 > 献立入力ページ
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

  week = calendar.monthrange(YEAR, int(key))[0]
  max_day = calendar.monthrange(YEAR, int(key))[1]
  # day_list = [day + 1 for day in range(max_day)]
  day_list = []
  for day in range(max_day):
    if week == 5 or week == 6:
      # day_list.remove(day+1)
      week = (week + 1) % 7
      continue
    day_list.append((day+1, week))
    week = (week + 1) % 7
  print(day_list)

  if request.method == "GET":
    # GET
    menu_list = []
    # SQL操作 [menu_idの最大値を取得]
    conn = sqlite3.connect("./static/database/kakaria.db")
    cur = conn.cursor()
    for day, week in day_list:
      for time in ["昼", "夜"]:
        SQL = '''
        SELECT menu.sets_id, food.food_name, menu.minimum_number
        FROM menu
          INNER JOIN food ON menu.food_id = food.food_id
          INNER JOIN times ON menu.times_id = times.times_id
        WHERE menu.date = date(?)
          AND times.time_str = ?
        ORDER BY menu.sets_id ASC
        '''
        cur.execute(SQL, (datetime.date(YEAR, int(key), day), time))
        food_names = cur.fetchall()
        print(f"food_names={food_names}")
        food_name_list = ["", ""]
        minimum_number_list = [0, 0]
        if food_names != None:
          for set, food_name, minimum_number in food_names:
            if set == 0:
              food_name_list[0] = food_name
              minimum_number_list[0] = minimum_number
            elif set == 1:
              food_name_list[1] = food_name
              minimum_number_list[1] = minimum_number
            else:
              continue
        if week == 4 and time == "夜":
          continue
        menu_list.append((int(key), day, week_str(week), time, (food_name_list[0], food_name_list[1]), (minimum_number_list[0], minimum_number_list[1])))
    cur.close()
    conn.close()
    print(f"menu_list{menu_list}")
    response = make_response(render_template("./month.html", menu_list=menu_list, key=key))
    return response
  else:
    # POST
    # change 一度入力してしまうと、空白の状態にできない。
    menu_list = []
    times = ['朝', '昼', '夜']
    sets = ['A', 'B']
    # POSTを受け取る
    for day, week in day_list:
      for time in times:
        for set in sets:
          if week == 4 and time == "夜":
            continue
          if time == "朝":
            if set == "A":
              menu_list.append((f"{YEAR}-{int(key):02}-{int(day):02}", time, set, "ご飯", 0))
            else:
              menu_list.append((f"{YEAR}-{int(key):02}-{int(day):02}", time, set, "パン", 0))
            continue
          # 書式 {{month}}:{{day}}:{{time}}:A:name
          food_name = request.form[f"{key}:{day}:{time}:{set}:name"]
          number = request.form[f"{key}:{day}:{time}:{set}:number"]
          if food_name != "":
            if number == "":
              number = 0
            menu_list.append((f"{YEAR}-{int(key):02}-{int(day):02}", time, set, food_name, number))
    print(menu_list)
    
    # SQL操作 [menu_idの最大値を取得]
    conn = sqlite3.connect("./static/database/kakaria.db")
    cur = conn.cursor()
    ##### error
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

# 寮食感想入力ページ
@app.route('/ryosyoku_feeling')
def ryosyoku_feeling():
  # セッション認証
  if authentication_redirect() != None:
    return authentication_redirect()

  response = make_response(render_template("./ryosyoku_feeling.html"))
  return response

# お風呂混雑状況システム
@app.route('/bath', methods=["GET", "POST"])
def bath():
  # セッション認証
  if authentication_redirect() != None:
    # 認証拒否
    return authentication_redirect()

  user_id = authentication_session()[0]
  today = datetime.date.today()
  now = datetime.datetime.now()
  time = f"{now.hour:02}:{now.minute:02}:{now.second:02}"

  if request.method == "GET":
    # 定義
    people_list = []
    today_list = []
    average_list = []
    conn = sqlite3.connect("./static/database/kakaria.db")
    cur = conn.cursor()

    # 入浴状況を取得
    SQL='''
    SELECT COUNT(*)
    FROM bath
    WHERE date = date(?)
      AND user_id = ?
      AND condition = 0
    '''
    cur.execute(SQL, (today, user_id))
    bath_switch = cur.fetchone()
    print(f"bath_switch = {bath_switch}")

    # 入浴状況ごとに集計
    for condition in range(3):
      SQL='''
      SELECT COUNT(*)
      FROM bath
      WHERE date = date(?)
        AND condition = ?
      '''
      cur.execute(SQL, (today, condition))
      people_list.append(cur.fetchone()[0])
    print(f"people_list = {people_list}")

    # 母数を計算
    SQL = '''
      SELECT COUNT(*)
      FROM (
        SELECT DISTINCT date
        FROM bath
      )
    '''
    cur.execute(SQL)
    all_date = cur.fetchone()[0]
    print(all_date)

    # グラフの作成
    start_time = datetime.datetime(YEAR, 1, 1, 17, 0, 0, 0)
    for _ in range(15):
      # 集計時刻を取得
      goal_time = start_time +  datetime.timedelta(minutes=19, seconds=59)
      point_time = f"{start_time.hour:02}:{start_time.minute:02}:{start_time.second:02}"
      point_stop_time = f"{goal_time.hour:02}:{goal_time.minute:02}:{goal_time.second:02}"
      print(f"point_time = {point_time}, point_stop_time = {point_stop_time}")
      
      # 本日の推移
      SQL='''
      SELECT COUNT(*)
      FROM bath
      WHERE date = date(?)
        AND condition <> 0
        AND time BETWEEN time(?) AND time(?)
      '''
      cur.execute(SQL, (today, point_time, point_stop_time))
      percent = ((cur.fetchone()[0]) / BATH_MAX * 100)
      color = None
      if percent < 80:
        # 青
        color = "rgb(26,115,232)"
      elif 80 <= percent < 100:
        # 黄
        color = "rgb(255,209,0)"
      elif 100 <= percent:
        # 赤
        color = "rgb(255,39,1)"
        percent = 100
      today_list.append((percent, color))
      
      # 平均の推移
      SQL='''
      SELECT COUNT(*)
      FROM bath
      WHERE condition <> 0
        AND time BETWEEN time(?) AND time(?)
      '''
      cur.execute(SQL, (point_time, point_stop_time))
      percent = (cur.fetchone()[0]) / all_date / BATH_MAX * 100
      color = None
      if percent < 80:
        # 青
        color = "rgb(26,115,232)"
      elif 80 <= percent < 100:
        # 黄
        color = "rgb(255,209,0)"
      elif 100 <= percent:
        # 赤
        color = "rgb(255,39,1)"
        percent = 100
      average_list.append((percent, color))

      # 更新処理
      start_time += datetime.timedelta(minutes=20)
    print(f"today_list = {today_list}")

    cur.close()
    conn.close()
    response = make_response(render_template("./bath.html", bath_switch=bath_switch[0], people_list=people_list, today_list=today_list, average_list=average_list))
    return response
  else:
    bath_switch = request.form["bath_switch"]

    conn = sqlite3.connect("./static/database/kakaria.db")
    cur = conn.cursor()
    SQL='''
    UPDATE bath
    SET condition = 1,
        time = time(?)
    WHERE date = date(?)
      AND user_id = ?
    '''
    print(f"time = {time}")
    cur.execute(SQL, (time, today, user_id))
    conn.commit()
    cur.close()
    conn.close()
    
    response = make_response(redirect(url_for('bath')))
    return response

# ログインページ
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

# サインインページ
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
    today = datetime.date.today()
    conn = sqlite3.connect("./static/database/kakaria.db")
    cur = conn.cursor()

    # ユーザ名の一意性の確保
    cur.execute("SELECT * FROM user WHERE user_name == ?", (user_name, ))
    fetch_user = cur.fetchone()
    if fetch_user != None:
      # すでに同じユーザ名が登録されている場合
      response = make_response(render_template("./sinup.html", condition=1))
      return response
    
    # ユーザの追加
    password_sh = password_hash(str(password))
    cur.execute("INSERT INTO user(user_name, password, permission) VALUES(?, ?, 1)", (user_name, password_sh))
    conn.commit()
    
    # 新規ユーザのreservatioレコードを追加
    # [menu_idの取得]
    SQL = '''
    SELECT menu_id, MIN(sets_id)
    FROM menu 
    WHERE date BETWEEN date(?) AND date(?)
    GROUP BY menu_id
    '''
    cur.execute(SQL, (today, today + (datetime.timedelta(days=7+(6-today.weekday())))))
    menu_list = cur.fetchall()

    # [user_idの取得]
    SQL = '''
    SELECT user_id
    FROM user
    WHERE user_name = ?
    '''
    cur.execute(SQL, (user_name))
    user_id = cur.fetchone()[0]
    print(f"menu_list = {menu_list}")
    print(f"user_id = {user_id}")

    # [reservationにレコードを追加]
    for menu, set in menu_list:
      cur.execute("INSERT INTO reservation(menu_id, user_id, condition, answer) VALUES(?, ?, 0, ?)", (menu, user_id, set))
      conn.commit()
    
    # reservationの確定更新処理
    # [予約日時が過ぎたレコードを更新]
    SQL = '''
      UPDATE reservation
      SET condition = 1
      WHERE menu_id IN(
        SELECT DISTINCT menu_id
        FROM menu
        WHERE menu.date BETWEEN date(2020-04-01) AND date(?)
      )
    '''
    cur.execute(SQL, (today + (datetime.timedelta(days=2)), ))
    conn.commit()
    
    cur.close()
    conn.close()
    # 新規会員登録完了
    return redirect(url_for('sinup_complete'))

# パスワード変更ページ
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

# 新規登録完了ページ
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

# バッチ処理
# @app.route('/startup', methods=["HEAD"])
@app.route('/startup')
def startup():
  now = datetime.datetime.now()
  today = datetime.date.today()

  # SQL操作
  conn = sqlite3.connect("./static/database/kakaria.db")
  cur = conn.cursor()
  SQL = '''
  SELECT COUNT(*)
  FROM log
  WHERE date = date(?)
  '''
  cur.execute(SQL, (today, ))
  log_f = cur.fetchone()
  print(f"log = {log_f}")

  # TTLの更新
  for TTL_count in range(TTL):
    SQL = '''
    UPDATE bath
    SET TTL = ?
    WHERE date = date(?)
      AND condition = 1
      AND TTL = ?
    '''
    cur.execute(SQL, (TTL_count, today, TTL_count+1))
    conn.commit()

  SQL = '''
  UPDATE bath
  SET condition = 2
  WHERE date = date(?)
    AND condition = 1
    AND TTL = ?
  '''
  cur.execute(SQL, (today, 0))
  conn.commit()
  cur.close()
  conn.close()


  # メンテナンス時間を3~4時
  if 3 <= now.hour < 4 and log_f[0] == 0:# その日の一回だけ実行
    conn = sqlite3.connect("./static/database/kakaria.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO log(date) VALUES(date(?))", (today, ))
    conn.commit()

    # [user_idの取得]
    SQL = '''
    SELECT user_id
    FROM user
    WHERE permission = 1
    '''
    cur.execute(SQL)
    user_list = cur.fetchall()

    cur.close()
    conn.close()

    for user in user_list:
      conn = sqlite3.connect("./static/database/kakaria.db")
      cur = conn.cursor()
      # [bathデータの追加]
      cur.execute("INSERT INTO bath(date, user_id, condition, TTL) VALUES(date(?), ?, 0, ?)", (today, user[0], TTL))
      conn.commit()
      cur.close()
      conn.close()

    # 3週間先のデータの追加
    if today.weekday() == 0:
      # 月曜日の場合
      conn = sqlite3.connect("./static/database/kakaria.db")
      cur = conn.cursor()

      # [menu_idの取得]
      SQL = '''
      SELECT menu_id, MIN(sets_id)
      FROM menu 
      WHERE date BETWEEN date(?) AND date(?)
      GROUP BY menu_id
      '''
      cur.execute(SQL, (today, today + (datetime.timedelta(days=6))))
      menu_list = cur.fetchall()

      cur.close()
      conn.close()
      print(menu_list)
      print(user_list)

      for menu, set in menu_list:
        for user in user_list:
          conn = sqlite3.connect("./static/database/kakaria.db")
          cur = conn.cursor()
          # [menu_idの取得]
          cur.execute("INSERT INTO reservation(menu_id, user_id, condition, answer) VALUES(?, ?, 0, ?)", (menu, user[0], set))
          conn.commit()
          cur.close()
          conn.close()

    # 未入力者の確定処理
    conn = sqlite3.connect("./static/database/kakaria.db")
    cur = conn.cursor()

    # [menu_idの取得]
    SQL = '''
      UPDATE reservation
      SET condition = 1
      WHERE menu_id IN(
        SELECT menu_id
        FROM menu 
        WHERE date = date(?)
        GROUP BY menu_id
      )
    '''
    cur.execute(SQL, (today + (datetime.timedelta(days=UPDATE-1)), ))
    conn.commit()
    cur.close()
    conn.close()

  return redirect(url_for('index'))
  
# week数値を文字列に
def week_str(week):
  week_list = ["月", "火", "水", "木", "金", "土", "日"]
  return week_list[week]


# 未ログインユーザ & 権限ごとにリダイレクト
def authentication_redirect():
  session_list = authentication_session()
  if session_list[0] == -1:
    # セッション認証非完了
    print("ログインしていない")
    return make_response(redirect(url_for('login')))
  if session_list[1] == 2:
    # 管理者ユーザ
    print("管理者ユーザです。")
    return make_response(redirect(url_for('control_result')))
  return None

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