# TCP 客户端
# 客户端主动连接服务器端，操作服务器端

import socket, time

TIMEOUT = 10
MaxBytes = 1024 * 1024

def CreatClient(startInfo):
  print(startInfo)
  client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  client.settimeout(TIMEOUT)
  return client

def LinkServer(handleClient, host='127.0.0.1', port = 8000):
  handleClient.connect((host,port))

def MainClient(handleClient):
  while True:
    inputData = input()
    if(inputData == "quit"):
      print("我要退出了，再见")
      break
    sendBytes = handleClient.send(inputData.encode())
    if sendBytes <= 0:
      break

def StopClient(handleClient, stopInfo='stopInfo'):
  handleClient.close()
  print(stopInfo)

def main(startInfo='startInfo', host='127.0.0.1', port=8000):
  client = CreatClient(startInfo)
  LinkServer(client, host, port)
  MainClient(client)
  StopClient(client)

main('MAC', '192.168.1.104', 8000)
