import pymysql

HOST = 'localhost'
PORT = 3306
DATABASE = 'mec'
USER = 'root'
PASSWORD = 'Wo123456'

def get_connection():
  conn = pymysql.connect(host=HOST, port=PORT, db=DATABASE, user=USER, password=PASSWORD)
  return conn

def check_it():
  conn = get_connection()
  # 使用 cursor() 方法创建一个 dict 格式的游标对象 cursor
  cursor = conn.cursor(pymysql.cursors.DictCursor)
  # 使用 execute()  方法执行 SQL 查询
  cursor.execute("select * from test")
  # 使用 fetchone() 方法获取单条数据.
  data = cursor.fetchone()
  print("-- 当前数据: ", data)
  # 关闭数据库连接
  cursor.close()
  conn.close()


if __name__ == '__main__':
    check_it()