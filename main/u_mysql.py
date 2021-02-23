# -*- coding: UTF-8 -*-

import pymysql

HOST = '192.168.1.104'
PORT = 3306
USER = 'root'
PASSWORD = 'Wo123456'
DATABASE = 'mec'
ALL_TABLES_NAME = ['mec_info', 'task_info']

def get_handle():
  db = pymysql.connect(
    host = HOST,
    port = PORT,
    user = USER,
    passwd = PASSWORD,
    db = DATABASE,
    charset = 'utf8'
  )
  cursor = db.cursor()
  return (db, cursor)

def close(db):
  db.close()

def execute_sql(db, cursor, sql):
  cursor.execute(sql)
  db.commit()

def read(cursor, sql, fetch_one = False):
  cursor.execute(sql)
  if not fetch_one:
    res = cursor.fetchall()
  else:
    res = cursor.fetchone()
  return res

def clean_table(db, cursor, table_name):
  sql = "DELETE FROM %s" % (table_name)
  cursor.execute(sql)
  db.commit()

def clean_history(table_info_arrow = []):
  db, cursor = get_handle()
  for current_table_name in ALL_TABLES_NAME:
    clean_table(db, cursor, current_table_name)
  close(db)
  print('已清空所有数据表......')