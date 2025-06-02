import asyncio

import websockets

from websocket_users_server import HOST, PORT


async def client():
    url = f"ws://{HOST}:{PORT}"
    async with websockets.connect(url) as websocket:
        message = "Привет, сервер!"
        print(f"Отправка: {message}")

        await websocket.send(message)

        for _ in range(5):
            message = await websocket.recv()
            print(message)


if __name__ == "__main__":
    asyncio.run(client())
