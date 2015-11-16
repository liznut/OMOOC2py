#client
import socket 
port = 8086
host = "localhost"
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
s.sendto("hello world",(host,port)) 