# -*- coding: UTF-8 -*-
# TCP 服务器端
# 客户端主动连接服务器端，操作服务器端

import socket, time

TIMEOUT = 120
MaxBytes = 1024 * 1024

def CreatServer():
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.settimeout(TIMEOUT)
  return server

def WaitLink(handleServer, host, port):
  handleServer.bind((host, port))
  handleServer.listen(100)
  print('服务器正在监听: ', port, ' 端口......')
  client, address = handleServer.accept()
  print(address, ' ==> 已链接......')
  return client

def SendToClient(handleServer, send_content):
  if not send_content:
    raise Exception('请检查发送给客户端的内容...')
  return handleServer.send(send_content.encode())

def RecvFromClient(handleServer, MaxBytes = 1024 * 1024):
  recv_content = handleServer.recv(MaxBytes).decode()
  return recv_content

def TestServer(handleServer):
  client, addr = handleServer.accept()
  print('addr: ', addr)
  index = 0
  while True:
    data = client.recv(MaxBytes)
    if not data:
      break
    data = data.decode()
    index += 1
    send_content = 'Server 收到: %d 个包, 当前: %s' % (index, data)
    client.send(send_content.encode())

def StopServer(handleServer):
  handleServer.close()

# def Test():
#   server = LinkServer(8000)
#   TestServer(server)
#   StopServer(server)

# Test()
