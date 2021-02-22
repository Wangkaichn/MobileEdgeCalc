# 单个树莓派 ==> 固定的 Host & Port
# 单个 TCP 会话 ==> 单个 MEC Server 集群
# 单个 Thread  ==> 单个 MEC Server

# import Thread
import u_tcp_client as TcpClient
import mysql, time

CURRENT_HOST = '192.168.1.104'

def get_current_port():
  db, cursor = mysql.get_handle()
  sql = "SELECT port FROM mec_info WHERE host='%s'" % CURRENT_HOST
  CURRENT_PORT = mysql.read(cursor, sql, fetch_one = True)[0]
  mysql.close(db)
  return CURRENT_PORT

# 为当前 MEC Server 建立一个 TCP 会话
# MEP --> MEC : 发送任务
def create_single_session():
  port = get_current_port()
  client = TcpClient.CreatClient()
  TcpClient.LinkServer(client, CURRENT_HOST, port)
  while True:
    localtime = time.asctime(time.localtime(time.time()))
    send_content = 'Client - %s' % localtime
    TcpClient.SendToServer(client, send_content)
    time.sleep(5)
    recv_content = TcpClient.RecvFromServer(client)
    print('recv_content: ', recv_content)
  
create_single_session()