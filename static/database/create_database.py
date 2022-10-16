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

# 3.時間帯表
cur.execute(
  "CREATE TABLE times("
    "times_id INTEGER,"
    "time_str STRING,"
    "PRIMARY KEY(times_id)"
  ")"
)
conn.commit()

# 4.times表
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

# 6.sets表
cur.execute("INSERT INTO sets(sets_id, set_str) VALUES(0, 'A')")
cur.execute("INSERT INTO sets(sets_id, set_str) VALUES(1, 'B')")
cur.execute("INSERT INTO sets(sets_id, set_str) VALUES(2, 'C')")
cur.execute("INSERT INTO sets(sets_id, set_str) VALUES(3, 'D')")
conn.commit()

# 7.メニュー表作成
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

# 8.予約表作成
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


# 9.セッションID表
cur.execute(
  "CREATE TABLE session("
    "session_id STRING,"
    "user_id INTEGER,"
    "PRIMARY KEY(session_id),"
    "FOREIGN KEY(user_id) REFERENCES user (user_id)"
  ")"
)
conn.commit()

# 10.更新処理
cur.execute(
  "CREATE TABLE log("
    "date DATE,"
    "PRIMARY KEY(date)"
  ")"
)
conn.commit()

# 11.お風呂混雑状況
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
