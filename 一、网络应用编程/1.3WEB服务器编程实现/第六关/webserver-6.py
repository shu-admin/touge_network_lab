#第6关：服务端异常（文件不存在异常）处理
#import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM) 
#Prepare a sever socket 
serverSocket.bind(("127.0.0.1",6789))
serverSocket.listen(1)

#while True:
print('开始WEB服务...')
try:
        connectionSocket, addr = serverSocket.accept()
        message = connectionSocket.recv(1024) # 获取客户发送的报文
        
        #读取文件内容
        filename = message.split()[1]       
        f = open(filename[1:])
        outputdata = f.read();
        
        #向套接字发送头部信息
        header = ' HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(outputdata))
        connectionSocket.send(header.encode())

        #S发送请求文件的内容
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        
        #关闭连接
        connectionSocket.close()
except IOError:             #异常处理
        #发送文件未找到的消息
        header = ' HTTP/1.1 404 not Found'
        #########Begin#########
        connectionSocket.send(header.encode())
        #########End#########
        #关闭连接
        connectionSocket.close()
#关闭套接字
serverSocket.close()