import time
import hmac
import hashlib
import requests

class BinanceClient():
    def __init__(self, api_key, api_secret, base_url):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url
        print('Keys Added!')

    def _generate_signature(self, payload):
        secret = self.api_secret

        return hmac.new(
            secret.encode(),
            payload.encode(),
            hashlib.sha256
        ).hexdigest()
        print('Signature Generated!')

    def _helper(self, symbol, side, order_type, quantity, price, timeInForce,timestamp):
        
        payload = f'symbol={symbol}&side={side}&type={order_type}&quantity={quantity}&timestamp={timestamp}&timeInForce={timeInForce}'

        if order_type == 'LIMIT':
            payload += f'&price={price}'

        signature = self._generate_signature(payload)
        return signature
    
    def place_order(self, symbol, side, order_type, quantity, price):
        #setting timeinforce forLIMIT and MARKET
        timeInForce = 'GTC'

        if order_type == 'MARKET':
            timeInForce = 'IOC'

        #getting current timestamp
        timestamp = int(time.time() * 1000)

        #creating query string
        signature = self._helper(symbol, side, order_type, quantity, price, timeInForce, timestamp)

        params = {
            'symbol':symbol,
            'side': side,
            'type':order_type,
            'timeInForce': timeInForce,
            'quantity':quantity,
            'timestamp': timestamp,
            'signature': signature,
        }
        print('Params Created!')

        if order_type == 'LIMIT':
            params['price'] = price
        print('Price Added!')

        headers = {
            'X-MBX-APIKEY': self.api_key,
        }

        print("Params:", params)  # Add before requests.post()
        response = requests.get(
            self.base_url,
            headers=headers,
            params=params,
        )
        print('Response Received!')

        print(f"Full URL: {self.base_url}")
        print(f"Status Code: {response.status_code}")

        if response.status_code in [200, 201, 202]:
            try:
                data = response.json()
                return {'success': True, **data}
            except:
                return {'success': True, 'message': 'Order accepted (no response body)'}

        # if response.status_code == 200:
        #     print('Response is 200!')
        #     data = response.json()
        #     print('Data Received!')
        #     print(data)
        #     orderId = data['orderId']
        #     status = data['status']
        #     executedQty = data['executedQty']
        #     cummulativeQuoteQty = data['cummulativeQuoteQty']

        #     return {
        #         'orderId': orderId,
        #         'status': status,
        #         'executedQty': executedQty,
        #         'cummulativeQuoteQty': cummulativeQuoteQty
        #     }
        #     print('Order Placed!')
        #     print(data)
        
        if response.status_code != 200:
            print('Response is not 200!')
            print(response.status_code)
            print('Order Placement Failed!')
            print(response.text)
            return None





