import asyncio
from coindcx.private import get_balances

async def main():
    data = await get_balances()
    print(data)

asyncio.run(main())