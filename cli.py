import argparse
import sys
from bot.config import API_KEY, API_SECRET, TESTNET_URL
from bot.client import BinanceClient
from bot.orders import validate_order

def main():
    def arguments():
        parser = argparse.ArgumentParser(description = 'Trading Bot')

        parser.add_argument('--symbol', help='Add the Symbol', required = True)
        parser.add_argument('--side', help = 'Add the side', required= True)
        parser.add_argument('--type', help='Add type', required = True)
        parser.add_argument('--quantity', help='Add the quantity', required = True)
        parser.add_argument('--price', help='This is required for the Limit')

        args = parser.parse_args()
        return args

    args = arguments()
    
    validation_result = validate_order(args.symbol, args.side, args.type, args.quantity, args.price)
    print(validation_result)

    api_key = API_KEY
    api_secret = API_SECRET
    base_url = TESTNET_URL

    client = BinanceClient(api_key, api_secret, base_url)

    # Unpack the validated tuple
    symbol, side, order_type, quantity, price = validation_result

    # Place the order
    result = client.place_order(symbol, side, order_type, quantity, price)

    print(result)


if __name__ == "__main__":
    main()