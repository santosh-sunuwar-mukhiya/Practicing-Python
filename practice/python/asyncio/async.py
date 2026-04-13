
# practicing the concept of async & await.
import time
from rich import print
import asyncio

async def endpoint(route):
    print(f" >> Handling {route}")
    await asyncio.sleep(1)
    print(f" << response {route}")
    return route


async def server():
    tests = (
        "GET /shipment?id=1",
        "PATCH /shipment?id=4",
        "GET /shipment?id=3",
    )
    start = time.perf_counter()

    # 1. Create a list of 'tasks' (this doesn't start them yet)
    tasks = [endpoint(route) for route in tests]

    # 2. Tell the event loop: "Run all of these together!"
    # This is what FastAPI does behind the scenes for different users.
    await asyncio.gather(*tasks)

    end = time.perf_counter()
    print(f"Total time: {end - start:.2f}s") # This will now be ~1.00s

asyncio.run(server())


