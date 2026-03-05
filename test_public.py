import asyncio
from coindcx.public import get_markets

async def main():
    data = await get_markets()
    print(len(data))
    print(data[0])

asyncio.run(main())