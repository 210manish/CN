from socket import *

sock = socket(AF_INET,SOCK_DGRAM)
sock.bind(("10.30.201.12",55555))

while True:
	clients = []

	while True:
		data,address = sock.recvfrom(128)
		print("connection from {}".format(address))
		clients.append(address)

		sock.sendto(b"ready",address)

		if(len(clients)==2):
			print("got two clients. Exchanging their info")
			break

	c1 = clients.pop()
	c1_addr,c1_port = c1
	c2 = clients.pop()
	c2_addr,c2_port = c2

	sock.sendto("{} {} {} {}".format(c1_addr,c1_port,c2_port,1).encode(),c2)
	sock.sendto("{} {} {} {}".format(c2_addr,c2_port,c1_port,0).encode(),c1)
