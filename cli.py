import argparse
from bot.client import create_client
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_side, validate_type
from bot.logging_config import setup_logger

print("CLI script started")

# ==============================
# API KEYS (Use .env in production)
# ==============================
API_KEY = "YOUR_TESTNET_API_KEY"
API_SECRET = "YOUR_TESTNET_SECRET"

# Setup logger
setup_logger()

# ==============================
# Argument Parser
# ==============================
parser = argparse.ArgumentParser(description="Crypto Trading Bot CLI")

parser.add_argument("--symbol", required=True, help="Trading pair (ex: BTCUSDT)")
parser.add_argument("--side", required=True, help="BUY or SELL")
parser.add_argument("--type", required=True, help="MARKET or LIMIT")
parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
parser.add_argument("--price", type=float, help="Price required for LIMIT orders")

args = parser.parse_args()

# ==============================
# Validate inputs
# ==============================
validate_side(args.side)
validate_type(args.type)

# ==============================
# Create Binance client
# ==============================
client = create_client(API_KEY, API_SECRET)

# ==============================
# Order Summary
# ==============================
print("\n------ ORDER SUMMARY ------")
print(f"Symbol: {args.symbol}")
print(f"Side: {args.side}")
print(f"Type: {args.type}")
print(f"Quantity: {args.quantity}")
print(f"Price: {args.price}")

# ==============================
# Place Order
# ==============================
try:

    if args.type == "MARKET":
        order = place_market_order(
            client,
            args.symbol,
            args.side,
            args.quantity
        )

    elif args.type == "LIMIT":

        if not args.price:
            raise ValueError("LIMIT order requires --price")

        order = place_limit_order(
            client,
            args.symbol,
            args.side,
            args.quantity,
            args.price
        )

    # ==============================
    # Print API Response
    # ==============================
    print("\nAPI Response:")
    print(order)

    if "orderId" in order:

        print("\nOrder Placed Successfully")
        print("Order ID:", order["orderId"])
        print("Status:", order["status"])
        print("Executed Qty:", order["executedQty"])

    else:
        print("\nOrder Failed:")
        print(order)

except Exception as e:

    print("\nOrder Failed:")
    print(str(e))