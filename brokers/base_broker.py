import sys
import os
sys.path.append(os.environ.get('ENVPATH', '/Users/miner34006/Documents/python/algo_bot'))

from abc import ABC, abstractmethod


class BaseBroker(ABC):
    @abstractmethod
    def buy(self, ticker, amount):
        pass
        
    @abstractmethod
    def sell(self, ticker, amount):
        pass