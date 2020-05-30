import sys
import os
sys.path.append(os.environ.get('ENVPATH', '/Users/miner34006/Documents/python/algo_bot'))

import logging
import requests

from . import REPORT
from . import base_api


class Sandbox(base_api.Base_api):
    def __init__(self, token, env=base_api.SANDBOX):
        super(Sandbox, self).__init__(token, env)
        self.base = '/sandbox'

    def register(self):
        endpoint = '{0}/{1}'.format(self.base, 'register')
        return self.post(endpoint)

    def set_currencies_balance(self, currency, balance):
        endpoint = '{0}/{1}'.format(self.base, 'currencies/balance')
        return self.post(endpoint, json={'currency': currency, 'balance': balance})

    def set_positions_balance_figi(self, figi, balance):
        endpoint = '{0}/{1}'.format(self.base, 'positions/balance')
        return self.post(endpoint, json={'figi': figi, 'balance': balance})

    def clear_sandbox():
        endpoint = '{0}/{1}'.format(self.base, 'clear')
        return self.post(endpoint)
