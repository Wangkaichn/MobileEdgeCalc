# 本地查询
# 此表用于保存 MEC 服务器的所有信息
# columns
#  *****  id INT NOT NULL AUTO_INCREMENT  *****
#  *****  x VARCHAR(20) NOT NULL          *****
#  *****  y VARCHAR(20) NOT NULL          *****
#  *****  cf VARCHAR(20) NOT NULL         *****
#  *****  status INT NOT NULL             *****

HOST = 'localhost'
PORT = 3306
DATABASE = 'mec'
USER = 'root'
PASSWORD = 'Wo123456'

def get_db():
  db = pymysql.connect(
    host = HOST,
    port = PORT,
    db = DATABASE,
    user = USER,
    password = PASSWORD
  )
  return db

def close_db(db):
  db.close()

def read(sql):
  db = get_db()
  cursor = db.cursor()
  res = cursor.fetchall()
  close_db(db)
  return res

a = read('select * from mec_info')
print(a)