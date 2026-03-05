import asyncio
import sys

from dotenv import load_dotenv

# 1. Load your .env variables BEFORE importing the coindcx module
load_dotenv()

from mcp.server.fastmcp import FastMCP
from coindcx import public, private

mcp = FastMCP("my-coindcx-server")

@mcp.tool(
    name="get_markets",
    description="List all CoinDCX trading pairs"
)
async def get_markets():
    return await public.get_markets()

@mcp.tool(name="get_ticker", description="Get ticker for a symbol")
async def get_ticker(symbol: str):
    return await public.get_ticker(symbol)

@mcp.tool(name="get_all_tickers", description="Get tickers for all markets")
async def get_all_tickers():
    return await public.get_all_tickers()

@mcp.tool(name="get_order_book", description="Get order book for a symbol")
async def get_order_book(symbol: str):
    return await public.get_order_book(symbol)

@mcp.tool(name="get_candles", description="Get OHLCV candles")
async def get_candles(symbol: str, interval: str, limit: int = 100):
    return await public.get_candles(symbol, interval, limit)


# -------- Private --------

@mcp.tool(name="get_balances", description="Fetch wallet balances")
async def get_balances():
    return await private.get_balances()

@mcp.tool(name="get_active_orders", description="Fetch active orders")
async def get_active_orders():
    return await private.get_active_orders()

@mcp.tool(name="get_order_history", description="Fetch order history")
async def get_order_history(limit: int = 50):
    return await private.get_order_history(limit)

@mcp.tool(name="place_limit_order", description="Place a limit buy/sell order")
async def place_limit_order(
    symbol: str,
    side: str,
    price: float,
    quantity: float
):
    return await private.place_limit_order(
        symbol, side, price, quantity
    )

@mcp.tool(name="cancel_order", description="Cancel order by ID")
async def cancel_order(order_id: str):
    return await private.cancel_order(order_id)

@mcp.tool(name="cancel_all_orders", description="Cancel all open orders")
async def cancel_all_orders():
    return await private.cancel_all_orders()


if __name__ == "__main__":
    # Add file=sys.stderr so it doesn't corrupt the MCP stdio channel!
    print("🚀 CoinDCX MCP Server started", file=sys.stderr, flush=True)
    mcp.run()