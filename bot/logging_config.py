import logging
import sys

def set_logging():
    logger = logging.getLogger('trading_bot')
    if logger.handlers:
        return logger

    handler = logging.FileHandler('trading_bot.log')
    stdout_handler = logging.StreamHandler(stream=sys.stdout)
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    return logger



