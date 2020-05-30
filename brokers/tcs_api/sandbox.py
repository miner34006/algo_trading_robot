import sys
import os
sys.path.append(os.environ.get('ENVPATH', '/Users/miner34006/Documents/python/algo_bot'))

from . import base_api


class Sandbox(base_api.Base_api):
    def __init__(self, token, env=base_api.SANDBOX):
        super(Sandbox, self).__init__(token, env)
        self._base = '/sandbox'

    def register(self):
        """ Function to register a sandbox bill

        :return: register response from api
        :rtype: dict
        """
        endpoint = '{0}/{1}'.format(self._base, 'register')
        return self._post(endpoint)

    def set_currencies_balance(self, currency, balance):
        """ Function to set currency balance

        :param currency: currency type
        :type currency: str
        :param balance: currency balance
        :type balance: int
        :return: response from api
        :rtype: dict
        """
        endpoint = '{0}/{1}'.format(self._base, 'currencies/balance')
        return self._post(endpoint, json={'currency': currency, 'balance': balance})

    def set_positions_balance_figi(self, figi, balance):
        """ Function to set stock balance for account

        :param figi: stock figi
        :type figi: str
        :param balance: number of stocks to set
        :type balance: int
        :return: response from api
        :rtype: dict
        """
        endpoint = '{0}/{1}'.format(self._base, 'positions/balance')
        return self._post(endpoint, json={'figi': figi, 'balance': balance})

    def clear_sandbox():
        """ Function to clear the sandbox

        :return: response from api
        :rtype: dict
        """
        endpoint = '{0}/{1}'.format(self._base, 'clear')
        return self._post(endpoint)
