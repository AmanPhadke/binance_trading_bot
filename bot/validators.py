def validate_symbol(symbol):
    symbol = symbol.upper()
    symbol = symbol.replace(' ', '')
    VALID_BINANCE_SYMBOLS = [
        "BTCUSDT",
        "ETHUSDT",
        "BNBUSDT",
        "XRPUSDT",
        "SOLUSDT",
        "ADAUSDT",
        "DOGEUSDT",
        "TRXUSDT",
        "DOTUSDT",
        "MATICUSDT",
        "LTCUSDT",
        "BCHUSDT",
        "AVAXUSDT",
        "LINKUSDT",
        "ATOMUSDT",
        "ETCUSDT",
        "XLMUSDT",
        "NEARUSDT",
        "APTUSDT",
        "OPUSDT",
        "ARBUSDT",
        "FILUSDT",
        "ICPUSDT",
        "INJUSDT",
        "SUIUSDT",
        "PEPEUSDT",
        "SHIBUSDT",
        "RNDRUSDT",
        "AAVEUSDT",
        "UNIUSDT"
    ]

    if symbol not in VALID_BINANCE_SYMBOLS:
        raise ValueError('Invalid Symbol')

    return symbol

def validate_side(side):
    VALID_SIDES = {'BUY', 'SELL'}

    side = side.upper()
    if side not in VALID_SIDES:
        raise ValueError('Side can either be "BUY" or "SELL"')

    return side

def validate_type(order_type):
    VALID_ORDER_TYPES = {"MARKET", "LIMIT"}

    order_type = order_type.upper()
    if order_type not in VALID_ORDER_TYPES:
        raise ValueError('Order type must be MARKET or LIMIT')

    return order_type

def validate_quantity(quantity):
    try:
        quantity = float(quantity)  # Convert here
    except (ValueError, TypeError):
        raise ValueError("Quantity must be a valid number")

    if quantity <= 0:
        raise ValueError("Quantity must be > 0")
    
    return quantity


def validate_price(order_type, price):
    try:
        if price is not None:
            price = float(price)
    except (ValueError, TypeError):
        raise ValueError("Price must be a valid number")

    if order_type == "LIMIT":
        if price is None or price <= 0:
            raise ValueError("LIMIT orders require a valid price > 0")

    if order_type == "MARKET" and price is not None:
        raise ValueError("MARKET orders should not include price")
    

    return price








    
    
