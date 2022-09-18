import sqlite3
import datetime
# pairディレクトリに配置した場合
# conn = sqlite3.connect("./../../static/database/TEST.db")
# meet best friendから実行した場合
# conn = sqlite3.connect(f"./static/database/{datetime.datetime.now().day}_{datetime.datetime.now().hour}_{datetime.datetime.now().minute}_{datetime.datetime.now().second}.db")
conn = sqlite3.connect("./static/database/kakaria.db")
cur = conn.cursor()

# 1.ユーザ表作成
# permission 1:一般ユーザ 0:システム管理者 2:寮食管理者
cur.execute(
  "CREATE TABLE user("
    "user_id INTEGER,"
    "user_name STRING NOT NULL,"
    "password STRING NOT NULL,"
    "permission INTEGER NOT NULL,"
    "PRIMARY KEY(user_id)"
  ")"
)
conn.commit

# 2.食品表作成
cur.execute(
  "CREATE TABLE food("
    "food_id INTEGER,"
    "food_name STRING,"
    "PRIMARY KEY(food_id)"
  ")"
)
conn.commit()

# 5.時間帯表
cur.execute(
  "CREATE TABLE times("
    "times_id INTEGER,"
    "time_str STRING,"
    "PRIMARY KEY(times_id)"
  ")"
)
conn.commit()

# times表
cur.execute("INSERT INTO times(times_id, time_str) VALUES(0, '朝')")
cur.execute("INSERT INTO times(times_id, time_str) VALUES(1, '昼')")
cur.execute("INSERT INTO times(times_id, time_str) VALUES(2, '夜')")
conn.commit()


# 5.セット表
cur.execute(
  "CREATE TABLE sets("
    "sets_id INTEGER,"
    "set_str STRING,"
    "PRIMARY KEY(sets_id)"
  ")"
)
conn.commit()

# sets表
cur.execute("INSERT INTO sets(sets_id, set_str) VALUES(0, 'A')")
cur.execute("INSERT INTO sets(sets_id, set_str) VALUES(1, 'B')")
cur.execute("INSERT INTO sets(sets_id, set_str) VALUES(2, 'C')")
cur.execute("INSERT INTO sets(sets_id, set_str) VALUES(3, 'D')")
conn.commit()

# 3.メニュー表作成
cur.execute(
  "CREATE TABLE menu("
    "menu_id INTEGER,"
    "sets_id INTEGER,"
    "date DATE,"
    "times_id INTEGER,"
    "food_id INTEGER,"
    "minimum_number INTEGER,"
    "PRIMARY KEY(menu_id, sets_id),"
    "FOREIGN KEY(sets_id) REFERENCES sets (sets_id)"
    "FOREIGN KEY(times_id) REFERENCES times (times_id)"
    "FOREIGN KEY(food_id) REFERENCES food (food_id)"
  ")"
)
conn.commit()

# 4.予約表作成
# condition 0 = 未入力, 1 = 確定, 2 = 入力済み
cur.execute(
  "CREATE TABLE reservation("
    "menu_id INTEGER,"
    "user_id INTEGER,"
    "condition INTEGER,"
    "answer INTEGER,"
    "PRIMARY KEY(menu_id, user_id),"
    "FOREIGN KEY(menu_id) REFERENCES menu (menu_id),"
    "FOREIGN KEY(user_id) REFERENCES user (user_id)"
  ")"
)
conn.commit()


# 5.セッションID表
cur.execute(
  "CREATE TABLE session("
    "session_id STRING,"
    "user_id INTEGER,"
    "PRIMARY KEY(session_id),"
    "FOREIGN KEY(user_id) REFERENCES user (user_id)"
  ")"
)
conn.commit()

# テスト用データ追加
# food表
cur.execute("INSERT INTO food(food_id, food_name) VALUES(1, 'ごはん')")
cur.execute("INSERT INTO food(food_id, food_name) VALUES(2, 'ぱん')")
cur.execute("INSERT INTO food(food_id, food_name) VALUES(3, '豚肉の炒めもの')")
cur.execute("INSERT INTO food(food_id, food_name) VALUES(4, 'しょうがやき')")
cur.execute("INSERT INTO food(food_id, food_name) VALUES(5, 'カレー')")
cur.execute("INSERT INTO food(food_id, food_name) VALUES(6, 'たまねぎ')")

# menu表
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(1, 0, date('2022-09-06'), 0, 1, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(1, 1, date('2022-09-06'), 0, 2, 4)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(2, 0, date('2022-09-06'), 1, 3, 1)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(2, 1, date('2022-09-06'), 1, 4, 2)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(3, 0, date('2022-09-06'), 2, 5, 2)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(3, 1, date('2022-09-06'), 2, 6, 2)")
# cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(22, 0, date('2022-09-06'), 0, 1, 1)")
# cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(22, 1, date('2022-09-06'), 0, 2, 1)")
# cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(23, 0, date('2022-09-06'), 1, 3, 0)")
# cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(23, 1, date('2022-09-06'), 1, 4, 0)")
# cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(24, 0, date('2022-09-06'), 2, 5, 0)")
# cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(24, 1, date('2022-09-06'), 2, 6, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(4, 0, date('2022-09-07'), 0, 1, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(4, 1, date('2022-09-07'), 0, 2, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(5, 0, date('2022-09-07'), 1, 3, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(5, 1, date('2022-09-07'), 1, 4, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(6, 0, date('2022-09-07'), 2, 5, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(6, 1, date('2022-09-07'), 2, 6, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(7, 0, date('2022-09-08'), 0, 1, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(7, 1, date('2022-09-08'), 0, 2, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(8, 0, date('2022-09-08'), 1, 3, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(8, 1, date('2022-09-08'), 1, 4, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(9, 0, date('2022-09-08'), 2, 5, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(9, 1, date('2022-09-08'), 2, 6, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(10, 0, date('2022-09-09'), 0, 1, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(10, 1, date('2022-09-09'), 0, 2, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(11, 0, date('2022-09-09'), 1, 3, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(11, 1, date('2022-09-09'), 1, 4, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(12, 0, date('2022-09-09'), 2, 5, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(12, 1, date('2022-09-09'), 2, 6, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(13, 0, date('2022-09-10'), 0, 1, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(13, 1, date('2022-09-10'), 0, 2, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(14, 0, date('2022-09-10'), 1, 3, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(14, 1, date('2022-09-10'), 1, 4, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(15, 0, date('2022-09-10'), 2, 5, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(15, 1, date('2022-09-10'), 2, 6, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(16, 0, date('2022-09-11'), 0, 1, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(16, 1, date('2022-09-11'), 0, 2, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(17, 0, date('2022-09-11'), 1, 3, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(17, 1, date('2022-09-11'), 1, 4, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(18, 0, date('2022-09-11'), 2, 5, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(18, 1, date('2022-09-11'), 2, 6, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(19, 0, date('2022-09-12'), 0, 1, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(19, 1, date('2022-09-12'), 0, 2, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(20, 0, date('2022-09-12'), 1, 3, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(20, 1, date('2022-09-12'), 1, 4, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(21, 0, date('2022-09-12'), 2, 5, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(21, 1, date('2022-09-12'), 2, 6, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(22, 0, date('2022-09-13'), 0, 1, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(22, 1, date('2022-09-13'), 0, 2, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(23, 0, date('2022-09-13'), 1, 3, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(23, 1, date('2022-09-13'), 1, 4, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(24, 0, date('2022-09-13'), 2, 5, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(24, 1, date('2022-09-13'), 2, 6, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(25, 0, date('2022-09-14'), 0, 1, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(25, 1, date('2022-09-14'), 0, 2, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(26, 0, date('2022-09-14'), 1, 3, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(26, 1, date('2022-09-14'), 1, 4, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(27, 0, date('2022-09-14'), 2, 5, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(27, 1, date('2022-09-14'), 2, 6, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(28, 0, date('2022-09-15'), 0, 1, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(28, 1, date('2022-09-15'), 0, 2, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(29, 0, date('2022-09-15'), 1, 3, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(29, 1, date('2022-09-15'), 1, 4, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(30, 0, date('2022-09-15'), 2, 5, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(30, 1, date('2022-09-15'), 2, 6, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(31, 0, date('2022-09-16'), 0, 1, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(31, 1, date('2022-09-16'), 0, 2, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(32, 0, date('2022-09-16'), 1, 3, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(32, 1, date('2022-09-16'), 1, 4, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(33, 0, date('2022-09-16'), 2, 5, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(33, 1, date('2022-09-16'), 2, 6, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(34, 0, date('2022-09-17'), 0, 1, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(34, 1, date('2022-09-17'), 0, 2, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(35, 0, date('2022-09-17'), 1, 3, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(35, 1, date('2022-09-17'), 1, 4, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(36, 0, date('2022-09-17'), 2, 5, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(36, 1, date('2022-09-17'), 2, 6, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(37, 0, date('2022-09-18'), 0, 1, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(37, 1, date('2022-09-18'), 0, 2, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(38, 0, date('2022-09-18'), 1, 3, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(38, 1, date('2022-09-18'), 1, 4, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(39, 0, date('2022-09-18'), 2, 5, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(39, 1, date('2022-09-18'), 2, 6, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(40, 0, date('2022-09-19'), 0, 1, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(40, 1, date('2022-09-19'), 0, 2, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(41, 0, date('2022-09-19'), 1, 3, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(41, 1, date('2022-09-19'), 1, 4, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(42, 0, date('2022-09-19'), 2, 5, 0)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(42, 1, date('2022-09-19'), 2, 6, 0)")
conn.commit()

# user表
cur.execute("INSERT INTO user(user_name, password, permission) VALUES('1', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 1)")
cur.execute("INSERT INTO user(user_name, password, permission) VALUES('2', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 1)")
cur.execute("INSERT INTO user(user_name, password, permission) VALUES('3', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 1)")
cur.execute("INSERT INTO user(user_name, password, permission) VALUES('4', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 1)")
cur.execute("INSERT INTO user(user_name, password, permission) VALUES('s', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 2)")
conn.commit()

# 5.更新処理
cur.execute(
  "CREATE TABLE log("
    "date DATE,"
    "PRIMARY KEY(date)"
  ")"
)
conn.commit()

# 5.お風呂混雑状況
# condition 0 = 未入浴, 1 = 入浴中, 2 = 入浴済み
cur.execute(
  "CREATE TABLE bath("
    "date DATE,"
    "user_id INTEGER,"
    "time TIME,"
    "condition INTEGER,"
    "TTL INTEGER,"
    "PRIMARY KEY(date, user_id)"
  ")"
)
conn.commit()

cur.close()
conn.close()


today = datetime.date.today()
  # メンテナンス時間を3~4時
  # if 3 <= now.hour < 4 and 1 == 1:# その日の一回だけ実行
if True:
  # 3週間先のデータの追加
  if True:
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
    cur.execute(SQL, (today, today + (datetime.timedelta(days=18))))
    menu_list = cur.fetchall()

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

    for user in user_list:
      conn = sqlite3.connect("./static/database/kakaria.db")
      cur = conn.cursor()
      # [menu_idの取得]
      cur.execute("INSERT INTO bath(date, user_id, condition, TTL) VALUES(date(?), ?, 0, 5)", (today, user[0]))
      conn.commit()
      cur.close()
      conn.close()

