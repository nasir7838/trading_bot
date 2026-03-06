from binance.client import Client

def create_client(api_key, api_secret):

    client = Client(api_key, api_secret)

    client.FUTURES_URL = "https://testnet.binance.vision/api/v3/order"

    return client