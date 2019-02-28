"""
host,port
form the url: bind(host,port)
wait for the client request
once you get the request from client, need to accept that.
process the request
send the response.
"""
import socket
def req_process(s):
	client_socket,client_info=s.accept()
	client_socket.send(b"hello firefox how are you!!")
	req = client_socket.recv(1024)
	if req.isdigit():
		resp=b"contains only digits"
	else:
		resp=b"contains some other details alsoo"
	client_socket.send(resp)

host=socket.gethostname()
port=8090
s=socket.socket()
try:
	s.bind((host,port))
	s.listen(1024)
	while True:
		print("server is running in %s:%s"%(host,port))
		print("waiting for the client request..")
		#print(s.accept())
		req_process(s)
		
except Exception as err:
	print(err)
finally:
	s.close()


