# 相对于 MEC , MEP 为服务端
# 与 MEC 建立会话
# 向 MEC 发送计算任务

from u_queue import Queue
from u_thread import Thread
import random
import u_time as Time
import u_tcp_server as TcpServer
import u_mysql as Mysql


CURRENT_HOST = '127.0.0.1'

# 生产者线程：create_task
# 消费者线程：send_task

def get_task_info():
  db, cursor = Mysql.get_handle()
  sql = 'SELECT * FROM task_info'
  task_info = Mysql.read(cursor, sql)
  Mysql.close(db)
  print(task_info)
  return task_info

def create_task(queue):
  while True:
    Time.Sleep(2)
    task_info = ''
    for _ in range(5):
      task_id = random.randint(3602, 3701)
      thread_id = 'thread_id_%d' % random.randint(1000, 1119)
      delay_time = '%.3f' % (random.random() * 10)
      task_info += '%s,%s,%s;' % (task_id, thread_id, delay_time)
    task_info_str = repr(task_info)
    queue.push(task_info_str)
    queue.pause()

def send_task(arguments):
  queue, port = arguments
  _server = TcpServer.CreatServer()
  server = TcpServer.WaitLink(_server, CURRENT_HOST, port)
  lock = Thread.CreateThreadLock()
  while True:
    Time.Sleep(0.1)
    if queue.isFull():
      task_info = queue.pop()
      size = TcpServer.SendToClient(server, task_info)
      recv_content = TcpServer.RecvFromClient(server)
      if recv_content == 'next':
        queue.endPause()
      else:
        raise Exception('send_task: 错误的回传信息......')

def main():
  queue_handle = Queue(1)
  thread_handle = Thread()
  # lock_handle = thread_handle.CreateThreadLock()
  threads_info = [(queue_handle, create_task), ((queue_handle, 8000), send_task)]
  thread_handle.CreateMultipleThread(threads_info)
  thread_handle.StartAllThreads()

main()

