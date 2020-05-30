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
        """ Function to get all current orders

        :return: all active orders
        :rtype: dict
        """
        return self._get(self._base)

    def create_limit_order(self, figi, lots=1, operation=OPERATION_BUY, price=0):
        """ Function to create a limit order

        :param figi: stock figi
        :type figi: str
        :param lots: number of lots to create, defaults to 1
        :type lots: int, optional
        :param operation: operation to perform, defaults to OPERATION_BUY
        :type operation: str, optional
        :param price: price to set for order, defaults to 0
        :type price: int, optional
        :return: limit order response from api
        :rtype: dict
        """
        endpoint = '{0}/{1}'.format(self._base, 'limit-order')
        data = {
            'lots': lots,
            'operation': operation,
            'price': price
        }
        return self._post(endpoint, params={'figi': figi}, json=data)

    def create_market_order(self, figi, lots=1, operation=OPERATION_BUY):
        """ Function to create a market order

        :param figi: stock figi
        :type figi: str
        :param lots: number of lots to create, defaults to 1
        :type lots: int, optional
        :param operation: operation to perform, defaults to OPERATION_BUY
        :type operation: str, optional
        :return: market order response from api
        :rtype: dict
        """
        endpoint = '{0}/{1}'.format(self._base, 'market-order')
        data = {
            'lots': lots,
            'operation': operation,
        }
        return self._post(endpoint, params={'figi': figi}, json=data)

    def cancel_order(self, order_id):
        """ Function to cancel an order

        :param order_id: order id
        :type order_id: str
        :return: cancel order response from api
        :rtype: dict
        """
        endpoint = '{0}/{1}'.format(self._base, 'cancel')
        return self._post(endpoint, json={'orderId': order_id})
