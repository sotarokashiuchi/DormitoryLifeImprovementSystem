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

# 3.メニュー表作成
cur.execute(
  "CREATE TABLE menu("
    "menu_id INTEGER,"
    "set_id INTEGER,"
    "date DATE,"
    "time INTEGER,"
    "food_id INTEGER,"
    "minimum_number INTEGER,"
    "PRIMARY KEY(menu_id, set_id),"
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
cur.execute("INSERT INTO user(user_name, password, permission) VALUES('樫内蒼太朗', '432', 1)")
cur.execute("INSERT INTO user(user_name, password, permission) VALUES('平木', '543', 1)")
cur.execute("INSERT INTO user(user_name, password, permission) VALUES('嶋', '654', 1)")
conn.commit()

# cur.execute("INSERT INTO project(info) VALUES('テスト用プロジェクト->寮部屋替えプロジェクト')")
# cur.execute("INSERT INTO project(info) VALUES('テスト用プロジェクト->ペア決め')")
# conn.commit()

# cur.execute("INSERT INTO project_control(project_id, user_id) VALUES(1, 1)")
# conn.commit()

# cur.execute("INSERT INTO form(project_id, form_id, format, question) VALUES(1, 1, 1, '1-1-1あなたは部屋をきれいにしますか？')")
# cur.execute("INSERT INTO form(project_id, form_id, format, question) VALUES(1, 3, 2, '1-3-2あなたは同室の人とたくさん話したいですか？')")
# cur.execute("INSERT INTO form(project_id, form_id, format, question) VALUES(1, 2, 2, '1-2-2あなたは同室の人とたくさん話したいよね？')")
# cur.execute("INSERT INTO form(project_id, form_id, format, question) VALUES(1, 5, 1, '1-5-1あなたは部屋をきれいに')")
# cur.execute("INSERT INTO form(project_id, form_id, format, question) VALUES(1, 4, 2, '1-4-2あなたは一人部屋になりたいですか？')")
# cur.execute("INSERT INTO form(project_id, form_id, format, question) VALUES(2, 1, 1, '2-1-1')")
# conn.commit()


cur.close()
conn.close()