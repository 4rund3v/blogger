#!/usr/bin/env python

# WS server example

import asyncio
import websockets
from blogger.conf import settings


async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name} {path}")
    greeting = f"Hello {name}!"
    await websocket.send(greeting)
    print(f"> {greeting}")


def main():
    start_server = websockets.serve(hello, "localhost", settings.WEB_SOCKET_PORT)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    main()
