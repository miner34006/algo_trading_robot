import sys
import os
sys.path.append(os.environ.get('ENVPATH', '/Users/miner34006/Documents/python/algo_bot'))

import logging
import requests

from . import REPORT
from . import base_api


class Market(base_api.Base_api):
    def __init__(self, token, env=base_api.SANDBOX):
        self.base = '/market'
        super(Market, self).__init__(token, env)

    def get_stocks(self):
        endpoint = '{0}/{1}'.format(self.base, 'stocks')
        return self.get(endpoint)

    def search_by_figi(self, figi):
        endpoint = '{0}/{1}'.format(self.base, 'search/by-figi')
        return self.get(endpoint, params={'figi': figi})

    def search_by_ticker(self, ticker):
        endpoint = '{0}/{1}'.format(self.base, 'search/by-ticker')
        return self.get(endpoint, params={'ticker': ticker})