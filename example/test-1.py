import socket
import time
MaxBytes=1024*1024
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.settimeout(120)
host = '127.0.0.1'
#host = socket.gethostname()
port = 8000
server.bind((host, port))
server.listen(1)
try:
    client,addr = server.accept()
    print(addr," 连接上了")
    while True:
        data = client.recv(MaxBytes)
        if not data:
            print('数据为空，我要退出了')
            break
        localTime = time.asctime( time.localtime(time.time()))
        print(localTime,' 接收到数据字节数:',len(data))
        print(data.decode())
        client.send(data)
except BaseException as e:
    print("出现异常：")
    print(repr(e))
finally:
    server.close()
    print("我已经退出了，后会无期")