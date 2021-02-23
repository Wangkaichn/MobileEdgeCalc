# -*- coding: UTF-8 -*-
# 相对于 MEP , MEC 为客户端
# 单个树莓派 ==> 固定的 Host & Port
# 单个 TCP 会话 ==> 单个 MEC Server 集群
# 单个 Thread  ==> 单个 MEC Server

from u_thread import Thread, GetAliveThreadInfo
from u_queue import Queue
import u_tcp_client as TcpClient
import u_mysql as Mysql
import u_time as Time
import random

CURRENT_HOST = '127.0.0.1'
# CURRENT_HOST = '192.168.1.104'

def get_all_mec_info():
  CURRENT_HOST = '192.168.1.104'
  db, cursor = Mysql.get_handle()
  sql = "SELECT * FROM mec_info WHERE host='%s'" % CURRENT_HOST
  all_mec_info = Mysql.read(cursor, sql)
  Mysql.close(db)
  return all_mec_info

def get_current_port(all_mec_info):
  CURRENT_PORT = all_mec_info[0][6]
  return CURRENT_PORT

def start_multiple_thread(threads_info = []):
  if not len(threads_info):
    return
  thread_handle = Thread()
  thread_handle.CreateMultipleThread(threads_info)
  thread_handle.StartAllThreads()

def update_mec_info(thread_id, field, value):
  db, cursor = Mysql.get_handle()
  sql = """
          UPDATE mec_info SET %s = %d WHERE thread_id = '%s'
        """ % (field, value, thread_id)
  Mysql.execute_sql(db, cursor, sql)
  Mysql.close(db)
def update_task_info(task_id, field, value):
  db, cursor = Mysql.get_handle()
  sql = """
          UPDATE task_info SET %s = %s WHERE id = '%s'
        """ % (field, value, task_id)
  Mysql.execute_sql(db, cursor, sql)
  Mysql.close(db)

def execute_task(arguments):
  client_handle, current_task_id, current_thread_id, current_delay_time = arguments
  current_delay_time = float(current_delay_time)
  local_time = Time.GetLocalTime()
  update_task_info(current_task_id, 'redirected_time', local_time)
  Time.Sleep(current_delay_time)
  start_task_threads(client_handle)
  update_mec_info(current_thread_id, 'status', 1)
  local_time = Time.GetLocalTime()
  update_task_info(current_task_id, 'end_time', local_time)
  print('current_thread_id: ', current_thread_id, ' ---- end')
  print('~~~~~ 当前存活线程数: %d' % (len(GetAliveThreadInfo())))

# TCP 会话得到字符串格式任务信息
# "'thread_id_1105.000,0.19785874504546652;thread_id_1093.000,0.07543144747768937;'"
def deal_with_recv_info(recv_content_str, client_handle):
  recv_content_str = recv_content_str.replace("'", '')[:-1]
  recv_content_arrow = recv_content_str.split(';')
  recv_content_arrow_count = len(recv_content_arrow)
  for index in range(recv_content_arrow_count):
    [current_task_id, current_thread_id, current_delay_time] = recv_content_arrow[index].split(',')
    recv_content_arrow[index] = ((client_handle, current_task_id, current_thread_id, current_delay_time), execute_task)
  return recv_content_arrow

def start_task_threads(client_handle):
  # recv_content = TcpClient.RecvFromServer(client_handle)
  # print('recv_content: ', recv_content)
  # TcpClient.SendToServer(client_handle, 'next')
  # all_task_info = deal_with_recv_info(recv_content, client_handle)
  # print('all_task_info: ', all_task_info)
  try:
    recv_content = TcpClient.RecvFromServer(client_handle)
    print('recv_content: ', recv_content)
    TcpClient.SendToServer(client_handle, 'next')
    all_task_info = deal_with_recv_info(recv_content, client_handle)
    # print('all_task_info: ', all_task_info)
    print('即将开启线程: ', all_task_info)
    start_multiple_thread(all_task_info)
    print('线程开启完毕......')
  except:
    print('......多半是recv超时......')

# 为当前 MEC Server 建立一个 TCP 会话
# MEP --> MEC : 发送任务
def start_session(port):
  client = TcpClient.LinkServer(CURRENT_HOST, port)
  while True:
    start_task_threads(client)

def start_threads(queue_handle, port):
  threads_info = [(port, start_session)]
  start_multiple_thread(threads_info)



all_mec_info = get_all_mec_info()
current_port_of_tcp = get_current_port(all_mec_info)
queue = Queue()
start_threads(queue, current_port_of_tcp)
