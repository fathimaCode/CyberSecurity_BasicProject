import socket
client_socket_object= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket_object.bind(('localhost',80))
msg=client_socket_object.recv(1024).decode()
print(f"Received from server: {msg}")
message="This is client side message"
client_socket_object.send(message.encode())
client_socket_object.close()