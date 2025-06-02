import socket

from websocket_users_server import HOST

TCP_PORT = 12345


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (HOST, TCP_PORT)
    server_socket.bind(server_address)

    server_socket.listen(10)
    print("Сервер запущен и ждет подключений...")

    while True:
        message_history = []

        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        data = client_socket.recv(1024).decode()
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")
        message_history.append(data)

        response = "Привет!"

        if data == "Как дела?":
            response = "\n".join(message_history)

        client_socket.send(response.encode())

        client_socket.close()


if __name__ == "__main__":
    server()
