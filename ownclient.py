import socket
import sys
import threading
import random

rendezvous = ('10.30.201.12', 55555)

ports = [5001, 5002, 5003, 5004, 5005, 5006]
rand_port=random.choice(ports)

print('connecting to rendezvous server')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.bind(('0.0.0.0', rand_port))
sock.sendto(b'0', rendezvous)

while True:
    data = sock.recv(1024).decode()

    if data.strip() == 'ready':
        print('checked in with server, waiting')
        break

data = sock.recv(1024).decode()
ip, dport, sport, flag = data.split(' ')
sport = int(sport)
dport = int(dport)
flag = int(flag)

print('\ngot peer')
print('  ip:          {}'.format(ip))
print('  source port: {}'.format(sport))
print('  dest port:   {}'.format(dport))
print('  flag:        {}\n'.format(flag))

if flag==1:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('10.30.201.12', sport+7))
    server_socket.listen()

    print("listening")

    client_socket, client_address = server_socket.accept()
    print("Connected with {}".format(client_address))

    while True:
        message = client_socket.recv(1024)
        print("Received message from {}: {}".format(client_address, message.decode()))

        reply_message = input("-> ")
        client_socket.sendall(reply_message.encode())
    s.close()

elif flag==0:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip,dport+7))
    while True:
        message = input("->")
        client_socket.sendall(message.encode())

        reply_message = client_socket.recv(1024)
        print("Received reply from server: {}".format(reply_message.decode()))

    s.close()




