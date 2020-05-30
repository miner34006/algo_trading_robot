import sys
import os
sys.path.append(os.environ.get('ENVPATH', '/Users/miner34006/Documents/python/algo_bot'))

from . import base_api

OPERATION_BUY = 'Buy'
OPERATION_SELL = 'Sell'


class Orders(base_api.Base_api):
    def __init__(self, token, env=base_api.SANDBOX):
        self._base = '/orders'
        super(Orders, self).__init__(token, env)

    def get_orders(self):
        return self._get(self._base)

    def create_limit_order(self, figi, lots=1, operation=OPERATION_BUY, price=0):
        endpoint = '{0}/{1}'.format(self._base, 'limit-order')
        data = {
            'lots': lots,
            'operation': operation,
            'price': price
        }
        return self._post(endpoint, params={'figi': figi}, json=data)

    def create_market_order(self, figi, lots=1, operation=OPERATION_BUY):
        endpoint = '{0}/{1}'.format(self._base, 'market-order')
        data = {
            'lots': lots,
            'operation': operation,
        }
        return self._post(endpoint, params={'figi': figi}, json=data)

    def cancel_order(self, order_id):
        endpoint = '{0}/{1}'.format(self._base, 'cancel')
        return self._post(endpoint, json={'orderId': order_id})
