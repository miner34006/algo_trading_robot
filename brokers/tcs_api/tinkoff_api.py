import sys
import os
sys.path.append(os.environ.get('ENVPATH', '/Users/miner34006/Documents/python/algo_bot'))

from . import base_api

from .market import Market
from .portfolio import Portfolio
from .sandbox import Sandbox
from .orders import Orders


class Tinkoff_api():
    """ Represintation of Tinkoff API
    """
    def __init__(self, token, env=base_api.SANDBOX):
        self.market = Market(token, env)
        self.portfolio = Portfolio(token, env)
        self.sandbox = Sandbox(token, env)
        self.sandbox = Sandbox(token, env)
        self.orders = Orders(token, env)
