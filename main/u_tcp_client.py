# TCP 客户端
# 客户端主动连接服务器端，操作服务器端

import socket, time

TIMEOUT = 10
MaxBytes = 1024 * 1024

def CreatClient():
  client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  client.settimeout(TIMEOUT)
  return client

def LinkServer(handleClient, host='127.0.0.1', port = 8000):
  if not isinstance(port, int):
    port = int(port)
  print('准备链接: ', host, port)
  handleClient.connect((host, port))
  print('链接完成: ', host, port)


def MainClient(handleClient):
  while True:
    inputData = input()
    if(inputData == "quit"):
      print("我要退出了，再见")
      break
    sendBytes = handleClient.send(inputData.encode())
    if sendBytes <= 0:
      break

def StopClient(handleClient):
  handleClient.close()

def Test():
  client = CreatClient()
  LinkServer(client, '192.168.1.104', 8000)
  MainClient(client)
  StopClient(client)