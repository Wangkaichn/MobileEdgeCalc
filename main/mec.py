# 单个树莓派 ==> 固定的 Host, 用 Port 区分不同 TCP 会话
# 单个 TCP 会话 ==> 单个 MEC Server
# 多进程开启多个 TCP 会话

from thread import Thread
import u_tcp_client as TcpClient
import mysql

CURRENT_HOST = '192.168.1.104'

def get_all_mec_info():
  db, cursor = mysql.get_handle()
  sql = "SELECT port FROM mec_info WHERE host='%s'" % CURRENT_HOST
  mec_info = mysql.read(cursor, sql)
  mysql.close(db)
  return mec_info


def handle_thread():
  f = 0
  while f > 3:
    print('f: ', f)

def create_single_session(tcp_server_info):
  host, port = tcp_server_info
  client = TcpClient.CreatClient()
  TcpClient.LinkServer(client, host, port)
  return handle_thread
  # StopClient(client)

def create_single_thread(port):
  thread_info = (CURRENT_HOST, port)
  handle_single_thread = Thread(thread_info, create_single_session)
  return (port, handle_single_thread)

def create_multiple_thread():
  threads = []
  all_mec_info = get_all_mec_info()
  for single_mec_info in all_mec_info:
    port = single_mec_info[0]
    single_mec_thread = create_single_thread(port)
    threads.append(single_mec_thread)
  return threads

def execute_multiple_thread(thread_arrow):
  ports = []
  threads = []
  for (port, thread) in [thread_arrow[0]]:
    ports.append(port)
    threads.append(thread)
  for t in threads:
    t.start()
    t.join()

multiple_thread = create_multiple_thread()
execute_multiple_thread(multiple_thread)
