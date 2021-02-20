# TCP 服务器端
# 客户端主动连接服务器端，操作服务器端

import socket, time

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
  print('当前链接信息', client, addr)
  while True:
    data = client.recv(MaxBytes)
    if not data:
      print('断开链接', client, addr)
      break
    localTime = time.asctime( time.localtime(time.time()))
    print(localTime, client, addr, data)

def StopServer(handleServer, stopInfo='stopInfo'):
  handleServer.close()
  print(stopInfo)

def main(startInfo='startInfo', host='127.0.0.1', port=8000):
  handleServer = CreatServer(startInfo)
  LinkServer(handleServer, host, port)
  MainServer(handleServer)
  StopServer(handleServer)

main()
