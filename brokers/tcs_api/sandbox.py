import sys
import os
sys.path.append(os.environ.get('ENVPATH', '/Users/miner34006/Documents/python/algo_bot'))

from . import base_api


class Sandbox(base_api.Base_api):
    def __init__(self, token, env=base_api.SANDBOX):
        super(Sandbox, self).__init__(token, env)
        self._base = '/sandbox'

    def register(self):
        endpoint = '{0}/{1}'.format(self._base, 'register')
        return self._post(endpoint)

    def set_currencies_balance(self, currency, balance):
        endpoint = '{0}/{1}'.format(self._base, 'currencies/balance')
        return self._post(endpoint, json={'currency': currency, 'balance': balance})

    def set_positions_balance_figi(self, figi, balance):
        endpoint = '{0}/{1}'.format(self._base, 'positions/balance')
        return self._post(endpoint, json={'figi': figi, 'balance': balance})

    def clear_sandbox():
        endpoint = '{0}/{1}'.format(self._base, 'clear')
        return self._post(endpoint)
