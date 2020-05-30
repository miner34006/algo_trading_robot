import sys
import os
sys.path.append(os.environ.get('ENVPATH', '/Users/miner34006/Documents/python/algo_bot'))

from . import base_api


class Market(base_api.Base_api):
    def __init__(self, token, env=base_api.SANDBOX):
        self._base = '/market'
        super(Market, self).__init__(token, env)

    def get_stocks(self):
        """ Function to get all available stocks

        :return: stock response from api
        :rtype: dict
        """
        endpoint = '{0}/{1}'.format(self._base, 'stocks')
        return self._get(endpoint)

    def search_by_figi(self, figi):
        """ Function to get information about stock using figi

        :param figi: stock figi
        :type figi: str
        :return: information about stock
        :rtype: dict
        """
        endpoint = '{0}/{1}'.format(self._base, 'search/by-figi')
        return self._get(endpoint, params={'figi': figi})

    def search_by_ticker(self, ticker):
        """ Function to get information about stock using ticker

        :param ticker: stock ticker
        :type ticker: str
        :return: information about stock
        :rtype: dict
        """
        endpoint = '{0}/{1}'.format(self._base, 'search/by-ticker')
        return self._get(endpoint, params={'ticker': ticker})