# TCP 服务器端
# 客户端主动连接服务器端，操作服务器端

import socket, time

TIMEOUT = 120
MaxBytes = 1024 * 1024

def CreatServer():
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.settimeout(TIMEOUT)
  return server

def LinkServer(handleServer, host, port):
  handleServer.bind((host, port))
  handleServer.listen(100)
  print('服务器正在监听: ', port, ' 端口......')

def MainServer(handleServer):
  client, addr = handleServer.accept()
  print('addr: ', addr)
  while True:
    data = client.recv(MaxBytes)
    if not data:
      break
    localTime = time.asctime(time.localtime(time.time()))
    data = data.decode()
    print(localTime, ': ', data)

def StopServer(handleServer):
  handleServer.close()

def Test():
  client = CreatServer()
  LinkServer(client, '192.168.1.104', 8000)
  MainServer(client)
  StopServer(client)

Test()
