import asyncio
import websockets
import os

print("reading file...")

port = os.getenv("PORT")
port = int(port) if port != None else 8000
print(port)


async def consumer_handler(websocket: websockets.WebSocketServerProtocol, path: str):
    async for message in websocket:
        print(message)


async def handler(websocket: websockets.WebSocketServerProtocol, path: str):
    print("user connected...")
    await websocket.send("connected")
    consumer_task = asyncio.ensure_future(consumer_handler(websocket, path))
    _, pending = await asyncio.wait([consumer_task], return_when=asyncio.FIRST_COMPLETED)
    for task in pending:
        task.cancel()


start_server = websockets.serve(handler, "0.0.0.0", port)
print("starting socket server...")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

print("do something e z")
