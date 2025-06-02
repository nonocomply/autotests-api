import asyncio

import websockets
from websockets import ServerConnection

HOST = "localhost"
PORT = 8765


async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")

        for i in range(5):
            response = f"{i+1} Сообщение пользователя: {message}"
            await websocket.send(response)


async def main():
    server = await websockets.serve(echo, host=HOST, port=PORT)
    print(f"WebSocket сервер запущен на ws://{HOST}:{PORT}")
    await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
