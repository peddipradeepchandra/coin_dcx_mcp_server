from coindcx import public
from coindcx import private

# -------- Private --------

@mcp.tool(
    name="get_markets",
    description="List all CoinDCX trading pairs"
)
async def markets():
    return await public.get_markets()

@mcp.tool(name="get_ticker", description="Get ticker for a symbol")
async def ticker(symbol: str):
    return await public.get_ticker(symbol)

@mcp.tool(name="get_all_tickers", description="Get tickers for all markets")
async def all_tickers():
    return await public.get_all_tickers()

@mcp.tool(name="get_order_book", description="Get order book for a symbol")
async def order_book(symbol: str):
    return await public.get_order_book(symbol)

@mcp.tool(name="get_candles", description="Get OHLCV candles")
async def candles(symbol: str, interval: str, limit: int = 100):
    return await public.get_candles(symbol, interval, limit)


# -------- Private --------

@mcp.tool(name="get_balances", description="Fetch wallet balances")
async def balances():
    return await private.get_balances()

@mcp.tool(name="get_active_orders", description="Fetch active orders")
async def active_orders():
    return await private.get_active_orders()

@mcp.tool(name="get_order_history", description="Fetch order history")
async def order_history(limit: int = 50):
    return await private.get_order_history(limit)

@mcp.tool(name="place_limit_order", description="Place a limit buy/sell order")
async def place_order(
    symbol: str,
    side: str,
    price: float,
    quantity: float
):
    return await private.place_limit_order(
        symbol, side, price, quantity
    )

@mcp.tool(name="cancel_order", description="Cancel order by ID")
async def cancel(order_id: str):
    return await private.cancel_order(order_id)

@mcp.tool(name="cancel_all_orders", description="Cancel all open orders")
async def cancel_all():
    return await private.cancel_all_orders()