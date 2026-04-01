from .validators import validate_symbol, validate_side, validate_type, validate_quantity, validate_price
from .logging_config import set_logging

log = set_logging()
def validate_order(symbol, side, order_type, quantity, price):
    try:
        symbol = validate_symbol(symbol)
        log.info('Symbol Validated')

        side = validate_side(side)
        log.info('Side Validated')

        order_type = validate_type(order_type)
        log.info('Type Validated')

        quantity = validate_quantity(quantity)
        log.info('Quantity Validated')

        price = validate_price(order_type, price)
        log.info('Price Validated')
        log.info('All validations passed')
        
        return symbol, side, order_type, quantity, price

    except Exception as e:
        log.error(f'Job Failed: {str(e)}')
        return f"Order preparation failed: {str(e)}"




        



