import sys
import os
sys.path.append(os.environ.get('ENVPATH', '/Users/miner34006/Documents/python/algo_bot'))

from .base_broker import Base_broker
from .tcs_api.tinkoff_api import Tinkoff_api
from .tcs_api.base_api import SANDBOX


class Tcs_broker(Base_broker):
    def __init__(self, token, env=SANDBOX):
        self.token = token
        self.api = Tinkoff_api(token, env)

    def buy(self, ticker, amount):
        pass
        
    def sell(self, ticker, amount):
        pass 