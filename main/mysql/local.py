# 本地查询
# 此表用于保存 MEC 服务器的所有信息
# columns
#  *****  id INT NOT NULL AUTO_INCREMENT  *****
#  *****  x VARCHAR(20) NOT NULL          *****
#  *****  y VARCHAR(20) NOT NULL          *****
#  *****  cf VARCHAR(20) NOT NULL         *****
#  *****  status INT NOT NULL             *****

import pymysql

HOST = '192.168.1.104'
PORT = 3306
DATABASE = 'mec'
USER = 'root'
PASSWORD = 'Wo123456'

def get_db():
  db = pymysql.connect(
    host = HOST,
    port = PORT,
    user = USER,
    passwd = PASSWORD,
    db = DATABASE,
    charset = 'utf8'
  )
  return db

def close_db(db):
  db.close()

def read(sql):
  db = get_db()
  print('--------------------')
  cursor = db.cursor()
  cursor.execute(sql)
  res = cursor.fetchall()
  close_db(db)
  return res

a = read('select * from mec_info')
print(a)