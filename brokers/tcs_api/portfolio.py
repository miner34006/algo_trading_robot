import sys
import os
sys.path.append(os.environ.get('ENVPATH', '/Users/miner34006/Documents/python/algo_bot'))

from . import base_api


class Portfolio(base_api.Base_api):
    def __init__(self, token, env=base_api.SANDBOX):
        self._base = '/portfolio'
        super(Portfolio, self).__init__(token, env)

    def get_portfolio(self):
        """ Function to get current asssets in portfolio

        :return: current assets in portfolio
        :rtype: dict
        """
        return self._get(self._base)

    def get_portfolio_currencises(self):
        """ Function to get portfolio currencises

        :return: portfolio currencises
        :rtype: dict
        """
        endpoint = '{0}/{1}'.format(self._base, 'currencies')
        return self._get(endpoint)
