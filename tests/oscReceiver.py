from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.dispatcher import Dispatcher
import asyncio


def filter_handler(address, *args):
    print(f"{address}: {args}")


dispatcher = Dispatcher()
dispatcher.map("/plant1", filter_handler)
dispatcher.map("/plant2", filter_handler)
dispatcher.map("/plant3", filter_handler)
dispatcher.map("/plant4", filter_handler)
dispatcher.map("/plant5", filter_handler)
dispatcher.map("/plant6", filter_handler)

ip = "127.0.0.1"
port = 2222


async def loop():
    """Example main loop that only runs for 10 iterations before finishing"""
    for i in range(100000):
        print(f"Loop {i}")
        await asyncio.sleep(1)


async def init_main():
    server = AsyncIOOSCUDPServer((ip, port), dispatcher, asyncio.get_event_loop())
    transport, protocol = await server.create_serve_endpoint()  # Create datagram endpoint and start serving

    await loop()  # Enter main loop of program

    transport.close()  # Clean up serve endpoint


asyncio.run(init_main())

