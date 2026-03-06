import logging


def place_market_order(client, symbol, side, quantity):

    order = client.create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity
    )

    logging.info(f"Market order response: {order}")
    print("\nAPI Response:", order)

    return order


def place_limit_order(client, symbol, side, quantity, price):

    order = client.create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC"
    )

    logging.info(f"Limit order response: {order}")
    print("\nAPI Response:", order)

    return order