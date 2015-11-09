# coding=utf-8
import socket 
port = 8081
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
#从给定的端口，从任何发送者，接收UDP数据报 
s.bind(("",port)) 
print 'waiting on port:',port 
while True: 
  data,addr = s.recvfrom(1024) 
  #接收一个数据报(最大到1024字节) 
  print 'reciveed:',data,"from",addr 


import socket 
port = 8081
host = "localhost"
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
s.sendto("hello world",(host,port)) 

