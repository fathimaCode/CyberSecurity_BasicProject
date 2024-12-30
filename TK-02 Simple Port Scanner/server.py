import socket
server_socket_object=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket_object.bind((1,2))
server_socket_object.listen(1)
client_socket,client_address=server_socket_object.accept()
client.socket.sendall(b'This is server side message')
client_msg=client_socket.recv(1024)
print(f"client_msg:{client_msg.decode()}")