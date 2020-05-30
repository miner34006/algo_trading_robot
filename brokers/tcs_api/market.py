import sys
import os
sys.path.append(os.environ.get('ENVPATH', '/Users/miner34006/Documents/python/algo_bot'))

from . import base_api


class Market(base_api.Base_api):
    def __init__(self, token, env=base_api.SANDBOX):
        self._base = '/market'
        super(Market, self).__init__(token, env)

    def get_stocks(self):
        endpoint = '{0}/{1}'.format(self._base, 'stocks')
        return self._get(endpoint)

    def search_by_figi(self, figi):
        endpoint = '{0}/{1}'.format(self._base, 'search/by-figi')
        return self._get(endpoint, params={'figi': figi})

    def search_by_ticker(self, ticker):
        endpoint = '{0}/{1}'.format(self._base, 'search/by-ticker')
        return self._get(endpoint, params={'ticker': ticker})