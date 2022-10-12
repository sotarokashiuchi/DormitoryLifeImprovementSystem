import sqlite3
import datetime
# pairディレクトリに配置した場合
# conn = sqlite3.connect('./../../static/database/TEST.db')
# meet best friendから実行した場合
# conn = sqlite3.connect(f'./static/database/{datetime.datetime.now().day}_{datetime.datetime.now().hour}_{datetime.datetime.now().minute}_{datetime.datetime.now().second}.db')
conn = sqlite3.connect('./static/database/kakaria.db')
cur = conn.cursor()

cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('1', 'test')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('2', 'ご飯')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('3', 'パン')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('4', 'a')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('5', '豚肉のおろしポン酢がけ')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('6', '豚肉のチーズマヨ焼き')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('7', '肉豆腐')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('8', '牛肉の甘辛炒め')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('9', 'サバの味噌煮')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('10', '鶏肉の竜田揚げ')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('11', 'ヒレカツ')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('12', 'ポークカレー')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('13', '肉団子の野菜トマトソース')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('14', 'プルコギ')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('15', 'エビフライ&カニクリームコロッケ')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('16', '鶏白湯ラーメン')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('17', '豚肉のレモンペッパーソテー')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('18', 'ポークソテー明太ホワイトソース')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('19', '牛肉と茄子の味噌炒め')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('20', 'ビーフカツ おろしソース')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('21', 'ポークソテーデミソースがけ')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('22', '豚肉スタミナ丼')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('23', '肉じゃが')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('24', 'ハンバーグ トマトソース')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('25', 'サーモンフライ')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('26', '照り焼きチキン')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('27', '豚肉のカレー炒め')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('28', '豚カツ')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('29', '牛肉のガリバタ炒め')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('30', 'メンチカツ&紫芋コロッケ')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('31', '白身魚の甘酢あんかけ')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('32', 'チキンソテー マヨマスター')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('33', '八宝菜')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('34', '豚肉のソテー オニオンソース')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('35', '豚肉のソテー トマトソース')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('36', '豚汁うどん')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('37', 'ロールキャベツ')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('38', '牛肉チャプチェ')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('39', '白身魚フライ&イカフライ')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('40', '鶏肉の香草パン粉焼き')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('41', '豚肉の柳川風')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('42', '豚肉の味噌漬け焼き')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('43', 'ミンチカツ')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('44', 'ビーフカレー')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('45', 'エビカツ')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('46', '鶏肉の塩麹焼き')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('47', '酢豚')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('48', '豚肉のソテー ステーキソース')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('49', '麻婆豆腐')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('50', '牛肉コロッケ&かぼちゃコロッケ')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('51', 'カレイの揚げ煮')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('52', '鶏肉の甘辛チーズ焼き')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('53', '白身魚のムニエル タルタルソース')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('54', '親子丼')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('55', '豚肉の香草チーズ焼き')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('56', '豚キムチ')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('57', 'ハンバーグ おろしソース')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('58', 'きのこミートスパゲティ')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('59', 'アジの南蛮漬け')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('60', '鶏肉のネギマヨ焼き')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('61', 'ポークピカタ')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('62', '豚肉の旨辛炒め')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('63', '肉団子の黒酢炒め')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('64', '牛肉ともやしのピリ辛炒め')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('65', 'ぶりの山椒焼き')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('66', 'チーズダッカルビ')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('67', '特別食')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('68', '牛肉とレンコンのバター醤油ソテー')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('69', '肉じゃがコロッケ&カレーコロッケ')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('70', 'すき焼き煮')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('71', '牛カルビ丼')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('72', 'さわらの蒲焼き')")
cur.execute("INSERT INTO 'main'.'food' ('food_id', 'food_name') VALUES ('73', 'ささみチーズフライ')")

conn.commit()


cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('1', '1', '2021-01-01', '', '1', '')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('2', '0', '2022-10-03', '0', '2', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('2', '1', '2022-10-03', '0', '3', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('4', '0', '2022-10-03', '2', '5', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('4', '1', '2022-10-03', '2', '6', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('5', '0', '2022-10-04', '0', '2', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('5', '1', '2022-10-04', '0', '3', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('6', '0', '2022-10-04', '1', '7', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('6', '1', '2022-10-04', '1', '8', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('7', '0', '2022-10-04', '2', '9', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('7', '1', '2022-10-04', '2', '10', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('8', '0', '2022-10-05', '0', '2', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('8', '1', '2022-10-05', '0', '3', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('9', '0', '2022-10-05', '1', '11', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('9', '1', '2022-10-05', '1', '12', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('10', '0', '2022-10-05', '2', '13', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('10', '1', '2022-10-05', '2', '14', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('11', '0', '2022-10-06', '0', '2', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('11', '1', '2022-10-06', '0', '3', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('12', '0', '2022-10-06', '1', '15', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('12', '1', '2022-10-06', '1', '16', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('13', '0', '2022-10-06', '2', '17', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('13', '1', '2022-10-06', '2', '18', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('14', '0', '2022-10-07', '0', '2', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('14', '1', '2022-10-07', '0', '3', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('15', '0', '2022-10-07', '1', '19', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('15', '1', '2022-10-07', '1', '20', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('16', '0', '2022-10-10', '0', '2', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('16', '1', '2022-10-10', '0', '3', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('19', '0', '2022-10-11', '0', '2', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('19', '1', '2022-10-11', '0', '3', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('20', '0', '2022-10-11', '1', '21', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('20', '1', '2022-10-11', '1', '22', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('21', '0', '2022-10-11', '2', '23', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('21', '1', '2022-10-11', '2', '24', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('22', '0', '2022-10-12', '0', '2', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('22', '1', '2022-10-12', '0', '3', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('23', '0', '2022-10-12', '1', '25', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('23', '1', '2022-10-12', '1', '26', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('24', '0', '2022-10-12', '2', '27', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('24', '1', '2022-10-12', '2', '28', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('25', '0', '2022-10-13', '0', '2', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('25', '1', '2022-10-13', '0', '3', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('26', '0', '2022-10-13', '1', '29', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('26', '1', '2022-10-13', '1', '30', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('27', '0', '2022-10-13', '2', '31', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('27', '1', '2022-10-13', '2', '32', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('28', '0', '2022-10-14', '0', '2', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('28', '1', '2022-10-14', '0', '3', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('29', '0', '2022-10-14', '1', '33', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('29', '1', '2022-10-14', '1', '34', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('30', '0', '2022-10-17', '0', '2', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('30', '1', '2022-10-17', '0', '3', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('31', '0', '2022-10-17', '1', '35', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('31', '1', '2022-10-17', '1', '36', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('32', '0', '2022-10-17', '2', '37', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('32', '1', '2022-10-17', '2', '38', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('33', '0', '2022-10-18', '0', '2', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('33', '1', '2022-10-18', '0', '3', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('34', '0', '2022-10-18', '1', '39', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('34', '1', '2022-10-18', '1', '40', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('35', '0', '2022-10-18', '2', '41', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('35', '1', '2022-10-18', '2', '42', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('36', '0', '2022-10-19', '0', '2', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('36', '1', '2022-10-19', '0', '3', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('37', '0', '2022-10-19', '1', '43', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('37', '1', '2022-10-19', '1', '44', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('38', '0', '2022-10-19', '2', '45', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('38', '1', '2022-10-19', '2', '46', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('39', '0', '2022-10-20', '0', '2', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('39', '1', '2022-10-20', '0', '3', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('40', '0', '2022-10-20', '1', '47', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('40', '1', '2022-10-20', '1', '48', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('41', '0', '2022-10-20', '2', '49', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('41', '1', '2022-10-20', '2', '50', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('42', '0', '2022-10-21', '0', '2', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('42', '1', '2022-10-21', '0', '3', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('43', '0', '2022-10-21', '1', '51', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('43', '1', '2022-10-21', '1', '52', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('44', '0', '2022-10-24', '0', '2', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('44', '1', '2022-10-24', '0', '3', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('45', '0', '2022-10-24', '1', '53', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('45', '1', '2022-10-24', '1', '54', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('46', '0', '2022-10-24', '2', '55', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('46', '1', '2022-10-24', '2', '56', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('47', '0', '2022-10-25', '0', '2', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('47', '1', '2022-10-25', '0', '3', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('48', '0', '2022-10-25', '1', '57', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('48', '1', '2022-10-25', '1', '58', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('49', '0', '2022-10-25', '2', '59', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('49', '1', '2022-10-25', '2', '60', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('50', '0', '2022-10-26', '0', '2', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('50', '1', '2022-10-26', '0', '3', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('51', '0', '2022-10-26', '1', '61', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('51', '1', '2022-10-26', '1', '62', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('52', '0', '2022-10-26', '2', '63', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('52', '1', '2022-10-26', '2', '64', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('53', '0', '2022-10-27', '0', '2', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('53', '1', '2022-10-27', '0', '3', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('54', '0', '2022-10-27', '1', '65', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('54', '1', '2022-10-27', '1', '66', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('55', '0', '2022-10-27', '2', '67', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('56', '0', '2022-10-28', '0', '2', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('56', '1', '2022-10-28', '0', '3', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('57', '0', '2022-10-28', '1', '68', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('57', '1', '2022-10-28', '1', '69', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('58', '0', '2022-10-31', '0', '2', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('58', '1', '2022-10-31', '0', '3', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('59', '0', '2022-10-31', '1', '70', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('59', '1', '2022-10-31', '1', '71', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('60', '0', '2022-10-31', '2', '72', '0')")
cur.execute("INSERT INTO 'main'.'menu' ('menu_id', 'sets_id', 'date', 'times_id', 'food_id', 'minimum_number') VALUES ('60', '1', '2022-10-31', '2', '73', '0')")

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

# conn = sqlite3.connect("./static/database/kakaria.db")
# cur = conn.cursor()
# # [入力確定のみ更新]
# SQL = '''
#   UPDATE reservation
#   SET 
# '''
# cur.execute("INSERT INTO reservation(menu_id, user_id, condition, answer) VALUES(?, ?, 0, ?)", (menu, user[0], set))
# conn.commit()
# cur.close()
# conn.close()