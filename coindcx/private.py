from .client import private_post
from .guards import validate_order

async def get_balances():
    return await private_post(
        "/exchange/v1/users/balances",
        {}
    )

async def get_active_orders():
    return await private_post(
        "/exchange/v1/orders/active_orders",
        {}
    )

async def get_order_history(limit: int = 50):
    return await private_post(
        "/exchange/v1/orders/trade_history",
        {"limit": limit}
    )

from .client import private_post
from .guards import validate_order

async def place_limit_order(
    symbol: str,
    side: str,
    price: float,
    quantity: float
):
    guard_result = validate_order(
        symbol, side, price, quantity
    )

    # DRY RUN triggered
    if guard_result is not None:
        return guard_result

    body = {
        "market": symbol,
        "side": side,
        "order_type": "limit_order",
        "price_per_unit": price,
        "total_quantity": quantity
    }

    return await private_post(
        "/exchange/v1/orders/create",
        body
    )

async def cancel_order(order_id: str):
    return await private_post(
        "/exchange/v1/orders/cancel",
        {"id": order_id}
    )

async def cancel_all_orders():
    return await private_post(
        "/exchange/v1/orders/cancel_all",
        {}
    )