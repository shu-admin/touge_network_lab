# 第1关：Ping服务端创建UDP套接字

# UDPPingerServer.py 
from socket import * 

########## Begin ##########

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('0.0.0.0', 12000))
########## End ##########

print( serverSocket)
