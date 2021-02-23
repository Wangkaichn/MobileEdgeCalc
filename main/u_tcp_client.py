# -*- coding: UTF-8 -*-
# TCP 客户端
# 客户端主动连接服务器端，操作服务器端

import socket, time, random

def CreatClient():
  TIMEOUT = 20
  client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  client.settimeout(TIMEOUT)
  return client

def LinkServer(host='127.0.0.1', port = 8000):
  handleClient = CreatClient()
  if not isinstance(port, int):
    port = int(port)
  print('准备链接: ', host, port)
  handleClient.connect((host, port))
  print('链接完成: ', host, port)
  return handleClient

def SendToServer(handleClient, send_content):
  if not send_content:
    raise Exception('请检查发送给服务器的内容...')
  return handleClient.send(send_content.encode())

def RecvFromServer(handleClient, MaxBytes = 1024 * 1024):
  recv_content = handleClient.recv(MaxBytes).decode()
  return recv_content

def TestServer(handleClient):
  while True:
    sendBytes = handleClient.send(repr(random.random()).encode())
    time.sleep(0.2)
    r = RecvFromServer(handleClient)
    print('RecvFromServer: ', r)
    # inputData = input()
    # if(inputData == "quit"):
    #   print("我要退出了，再见")
    #   break
    # if sendBytes <= 0:
    #   break

def StopClient(handleClient):
  handleClient.close()

def Test():
  client = CreatClient()
  LinkServer(client)
  TestServer(client)
  StopClient(client)

# Test()