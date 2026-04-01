# Binance Trading Bot

A Python-based trading bot for placing orders on Binance Futures using the REST API.

## Features
- Place limit and market orders
- Input validation and error handling
- HMAC-SHA256 signature authentication
- Logging to file and stdout
- Command-line interface

## Setup

### Requirements
- Python 3.8+
- `requests` library
- `python-dotenv`

### Installation
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create `.env` file with your Binance credentials:
```
BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret
BINANCE_TESTNET_URL=https://testnet.binancefuture.com
```

## Usage
```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 45000
```

### Arguments
- `--symbol` - Trading pair (BTCUSDT, ETHUSDT, etc.)
- `--side` - BUY or SELL
- `--type` - LIMIT or MARKET
- `--quantity` - Order quantity
- `--price` - Price (required for LIMIT orders)

## Project Structure
- `bot/client.py` - Binance API client
- `bot/orders.py` - Order preparation and validation
- `bot/validators.py` - Input validation
- `bot/config.py` - Configuration management
- `bot/cli.py` - Command-line interface
- `bot/logging_config.py` - Logging setup
