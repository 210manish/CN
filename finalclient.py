import socket

rendezvous = ('10.20.201.134', 55570)
print('connecting to rendezvous server')

peer_sender=int(input("Enter 1 if you can send files "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(rendezvous)

while True:
    if (peer_sender==1):
        message = input("File details(fileName;lines): ")
        sock.sendall(message.encode())
        reply = sock.recv(1024).decode()
        print("Received message : ",reply)
        port=int(reply.split(";")[1])
        print(port)
        break

    elif (peer_sender==0):
        message = input("Enter the file you want: ")
        sock.sendall(message.encode())
        present=sock.recv(1024).decode().split(";")
        print(present[0])
        if int(present[1])==1:
            sock.sendall("ok".encode())
            cli=sock.recv(1024).decode().split(";")
            c1=cli[0].split(" ")
            #print(c1)
            c2=cli[1].split(" ")
            #print(c2)
            c3=cli[2].split(" ")
            #print(c3)
            break
        else:
            break

if(peer_sender==1):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('10.20.201.134',port+21))
    server_socket.listen()

    print("Server started")

    while True:
        client_socket, client_address = server_socket.accept()
        print("Connected with {}".format(client_address))
        FILE_NAME=client_socket.recv(1024).decode()
        print(FILE_NAME)
        with open(FILE_NAME, 'rb') as f:
            #client_socket.sendall(FILE_NAME.encode())
            while True:
                data = f.read(1024)
                print(data)
                if not data:
                    break
                client_socket.sendall(data)
        print("File transferred successfully")

elif(peer_sender==0):
    
    for i in range(len(cli)):
        peer_info=cli[i].split(" ")
        print(peer_info)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('10.20.201.134',int(peer_info[1])+21))

        client_socket.sendall(peer_info[2].encode())
        print("file name sent")
        #file_name = client_socket.recv(1024).decode()
        file_name="exam"+str(i+1)+".txt"
        with open(file_name, 'wb') as f:
            while True:
                data = client_socket.recv(1024)
                print(data.decode())
                if not data:
                    break
                #byte_data=data.encode()
                f.write(data)
        f.close()
        print("File transferred successfully")






