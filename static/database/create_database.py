import sqlite3
import datetime
# pairディレクトリに配置した場合
# conn = sqlite3.connect("./../../static/database/TEST.db")
# meet best friendから実行した場合
# conn = sqlite3.connect(f"./static/database/{datetime.datetime.now().day}_{datetime.datetime.now().hour}_{datetime.datetime.now().minute}_{datetime.datetime.now().second}.db")
conn = sqlite3.connect("./static/database/kakaria.db")
cur = conn.cursor()

# 1.ユーザ表作成
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
cur.execute(
  "CREATE TABLE reservation("
    "menu_id INTEGER,"
    "user_id INTEGER,"
    "conditon INTEGER,"
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
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(1, 0, date('2022-08-01'), 0, 1, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(1, 1, date('2022-08-01'), 0, 2, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(2, 0, date('2022-08-01'), 1, 3, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(2, 1, date('2022-08-01'), 1, 4, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(3, 0, date('2022-08-01'), 2, 5, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(3, 1, date('2022-08-01'), 2, 6, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(4, 0, date('2022-08-02'), 1, 1, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(4, 1, date('2022-08-02'), 1, 2, 20)")
conn.commit()

# 表
# cur.execute("INSERT INTO user(user_name, password, permission) VALUES('樫内蒼太朗', '432', 1)")
conn.commit()

cur.close()
conn.close()