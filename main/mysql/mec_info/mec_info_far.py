# 远程查询
# 此表用于保存 MEC 服务器的所有信息
# columns
#  *****  id INT NOT NULL AUTO_INCREMENT  *****
#  *****  x VARCHAR(20) NOT NULL          *****
#  *****  y VARCHAR(20) NOT NULL          *****
#  *****  cf VARCHAR(20) NOT NULL         *****
#  *****  status INT NOT NULL             *****

import socket, time, mec_info as db_mec_info

TIMEOUT = 120
MaxBytes = 1024 * 1024

def CreatServer(startInfo):
  print(startInfo)
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.settimeout(TIMEOUT)
  return server

def LinkServer(handleServer, host, port):
  handleServer.bind((host, port))
  handleServer.listen(1)

def MainServer(handleServer):
  client, addr = handleServer.accept()
  print('当前链接信息', addr)
  while True:
    data = client.recv(MaxBytes)
    if not data:
      print('断开链接', addr)
      break
    data = data.decode()
    localTime = time.asctime(time.localtime(time.time()))
    if data.startswith('sql:'):
      sql = data.split('sql:')[1]
      print('sql: ', sql)
      a = db_mec_info.read(sql)
      print(localTime, addr, data, a)
    else:
      print(localTime, addr, data, '无 sql')

def StopServer(handleServer, stopInfo='stopInfo'):
  handleServer.close()
  print(stopInfo)

def main(host='127.0.0.1', port=8000, startInfo='startInfo'):
  handleServer = CreatServer(startInfo)
  LinkServer(handleServer, host, port)
  MainServer(handleServer)
  StopServer(handleServer)

main('192.168.1.104')