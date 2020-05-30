import sys
import os
sys.path.append(os.environ.get('ENVPATH', '/Users/miner34006/Documents/python/algo_bot'))

import logging
import requests

from . import REPORT
from . import base_api


class Portfolio(base_api.Base_api):
    def __init__(self, token, env=base_api.SANDBOX):
        self.base = '/portfolio'
        super(Portfolio, self).__init__(token, env)

    def get_portfolio(self):
        return self.get(self.base)

    def get_portfolio_currencises(self):
        endpoint = '{0}/{1}'.format(self.base, 'currencies')
        return self.get(endpoint)
