import socket

from tcp_users_server import TCP_PORT
from websocket_users_server import HOST

server_address = (HOST, TCP_PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect(server_address)

    message = "Привет, сервер!"
    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print(response)
