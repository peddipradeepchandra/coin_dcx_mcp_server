import httpx

API_BASE_URL = "https://api.coindcx.com"
PUBLIC_BASE_URL = "https://public.coindcx.com"

async def get_markets():
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{API_BASE_URL}/exchange/v1/markets")
        r.raise_for_status()
        return r.json()
    
async def get_ticker(symbol: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{API_BASE_URL}/exchange/ticker")
        r.raise_for_status()
        data = r.json()
        # Uses 'market' (e.g., "BTCINR")
        return next((x for x in data if x.get("market") == symbol), None)

async def get_all_tickers():
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{API_BASE_URL}/exchange/ticker")
        r.raise_for_status()
        return r.json()

async def get_order_book(pair: str):
    async with httpx.AsyncClient() as client:
        r = await client.get(
            f"{PUBLIC_BASE_URL}/market_data/orderbook",
            params={"pair": pair} # Requires pair (e.g., "I-BTC_INR")
        )
        r.raise_for_status()
        return r.json()

async def get_candles(pair: str, interval: str, limit: int = 100):
    async with httpx.AsyncClient() as client:
        r = await client.get(
            f"{PUBLIC_BASE_URL}/market_data/candles",
            params={
                "pair": pair,         # Requires pair (e.g., "I-BTC_INR")
                "interval": interval, # Acceptable: "1m", "5m", "1h", "1d", etc.
                "limit": limit
            }
        )
        r.raise_for_status()
        return r.json()