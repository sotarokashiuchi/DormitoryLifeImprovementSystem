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
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(1, 0, date('2022-08-01'), 0, 1, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(1, 1, date('2022-08-01'), 0, 2, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(2, 0, date('2022-08-01'), 1, 3, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(2, 1, date('2022-08-01'), 1, 4, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(3, 0, date('2022-08-01'), 2, 5, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(3, 1, date('2022-08-01'), 2, 6, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(4, 0, date('2022-08-07'), 0, 1, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(4, 1, date('2022-08-07'), 0, 2, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(5, 0, date('2022-08-07'), 1, 3, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(5, 1, date('2022-08-07'), 1, 4, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(6, 0, date('2022-08-07'), 2, 5, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(6, 1, date('2022-08-07'), 2, 6, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(7, 0, date('2022-08-14'), 0, 1, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(7, 1, date('2022-08-14'), 0, 2, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(8, 0, date('2022-08-14'), 1, 3, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(8, 1, date('2022-08-14'), 1, 4, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(9, 0, date('2022-08-14'), 2, 5, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(9, 1, date('2022-08-14'), 2, 6, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(10, 0, date('2022-08-21'), 0, 1, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(10, 1, date('2022-08-21'), 0, 2, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(11, 0, date('2022-08-21'), 1, 3, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(11, 1, date('2022-08-21'), 1, 4, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(12, 0, date('2022-08-21'), 2, 5, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(12, 1, date('2022-08-21'), 2, 6, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(13, 0, date('2022-08-22'), 0, 1, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(13, 1, date('2022-08-22'), 0, 2, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(14, 0, date('2022-08-22'), 1, 3, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(14, 1, date('2022-08-22'), 1, 4, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(15, 0, date('2022-08-22'), 2, 5, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(15, 1, date('2022-08-22'), 2, 6, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(16, 0, date('2022-08-31'), 0, 1, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(16, 1, date('2022-08-31'), 0, 2, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(17, 0, date('2022-08-31'), 1, 3, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(17, 1, date('2022-08-31'), 1, 4, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(18, 0, date('2022-08-31'), 2, 5, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(18, 1, date('2022-08-31'), 2, 6, 20)")

cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(19, 0, date('2022-09-05'), 0, 1, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(19, 1, date('2022-09-05'), 0, 2, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(20, 0, date('2022-09-05'), 1, 3, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(20, 1, date('2022-09-05'), 1, 4, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(21, 0, date('2022-09-05'), 2, 5, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(21, 1, date('2022-09-05'), 2, 6, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(22, 0, date('2022-09-06'), 0, 1, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(22, 1, date('2022-09-06'), 0, 2, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(23, 0, date('2022-09-06'), 1, 3, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(23, 1, date('2022-09-06'), 1, 4, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(24, 0, date('2022-09-06'), 2, 5, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(24, 1, date('2022-09-06'), 2, 6, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(25, 0, date('2022-09-07'), 0, 1, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(25, 1, date('2022-09-07'), 0, 2, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(26, 0, date('2022-09-07'), 1, 3, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(26, 1, date('2022-09-07'), 1, 4, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(27, 0, date('2022-09-07'), 2, 5, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(27, 1, date('2022-09-07'), 2, 6, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(28, 0, date('2022-09-08'), 0, 1, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(28, 1, date('2022-09-08'), 0, 2, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(29, 0, date('2022-09-08'), 1, 3, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(29, 1, date('2022-09-08'), 1, 4, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(30, 0, date('2022-09-08'), 2, 5, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(30, 1, date('2022-09-08'), 2, 6, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(31, 0, date('2022-09-09'), 0, 1, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(31, 1, date('2022-09-09'), 0, 2, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(32, 0, date('2022-09-09'), 1, 3, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(32, 1, date('2022-09-09'), 1, 4, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(33, 0, date('2022-09-09'), 2, 5, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(33, 1, date('2022-09-09'), 2, 6, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(34, 0, date('2022-09-10'), 0, 1, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(34, 1, date('2022-09-10'), 0, 2, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(35, 0, date('2022-09-10'), 1, 3, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(35, 1, date('2022-09-10'), 1, 4, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(36, 0, date('2022-09-10'), 2, 5, 20)")
cur.execute("INSERT INTO menu(menu_id, sets_id, date, times_id, food_id, minimum_number) VALUES(36, 1, date('2022-09-10'), 2, 6, 20)")

conn.commit()

# user表
cur.execute("INSERT INTO user(user_name, password, permission) VALUES('1', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 1)")
cur.execute("INSERT INTO user(user_name, password, permission) VALUES('2', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 1)")
cur.execute("INSERT INTO user(user_name, password, permission) VALUES('3', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 1)")
cur.execute("INSERT INTO user(user_name, password, permission) VALUES('4', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 1)")
cur.execute("INSERT INTO user(user_name, password, permission) VALUES('s', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 2)")
conn.commit()

cur.close()
conn.close()