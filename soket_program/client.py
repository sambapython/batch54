import socket
host="khyaathipython"
port=8090
s=socket.socket()
s.connect((host,port))
ack = s.recv(50)
print("ack=%s"%ack)
s.send(b"2323")
res = s.recv(1024)
print("response:",res)
