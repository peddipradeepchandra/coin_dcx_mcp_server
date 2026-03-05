from config import settings

MAX_ORDER_VALUE = 5000  # INR
ALLOWED_SIDES = {"buy", "sell"}

def validate_order(symbol, side, price, quantity):
    if not settings.TRADING_ENABLED:
        raise Exception("Trading is currently disabled")

    if side not in ALLOWED_SIDES:
        raise ValueError("Invalid order side")

    if price <= 0 or quantity <= 0:
        raise ValueError("Price and quantity must be positive")

    order_value = price * quantity

    if order_value > MAX_ORDER_VALUE:
        raise ValueError(
            f"Order value {order_value} exceeds limit {MAX_ORDER_VALUE}"
        )

    if settings.DRY_RUN:
        return {
            "dry_run": True,
            "symbol": symbol,
            "side": side,
            "price": price,
            "quantity": quantity,
            "order_value": order_value
        }

    return None