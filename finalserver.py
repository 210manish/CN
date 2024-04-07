from socket import *

sock = socket(AF_INET,SOCK_STREAM)
sock.bind(("10.20.201.134",55570))
sock.listen()

print("listening")

while True:
	clients = []
	while True:
		client_socket, client_address = sock.accept()
		print("connection from {}".format(client_address))
		addr,port=client_address		
		
		message = client_socket.recv(1024).decode()
		print("Received message from {}: {}".format(client_address, message))
		file_name=message.split(";")[0]
		lines=message.split(";")[1]

		clients.append([str(addr),str(port),str(file_name),str(lines)])
		
		if(len(clients)==4):
			if(clients[3][2]!=clients[0][2] and clients[3][2]!=clients[1][2] and clients[3][2]!=clients[2][2]):
				dummy_rep="File not present with peers;0"
				client_socket.sendall(dummy_rep.encode())
			else:
				dummy_rep="File present with peers;1"
				client_socket.sendall(dummy_rep.encode())
				dummy_resp=client_socket.recv(1024).decode()
				c1=" ".join(clients[0])
				c2=" ".join(clients[1])
				c3=" ".join(clients[2])
				res=c1+";"+c2+";"+c3
				client_socket.sendall(res.encode())
				break

		reply='Got file details waiting for more peers;'+str(port)
		client_socket.sendall(reply.encode())
