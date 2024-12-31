import socket
client_socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 8080)
client_socket_object.connect(server_address)
try:
    message = "This is a client-side message"
    client_socket_object.send(message.encode())
    print(f"Sent to server: {message}")
    response = client_socket_object.recv(1024).decode()
    print(f"Received from server: {response}")
finally:
    client_socket_object.close()