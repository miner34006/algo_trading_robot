import sys
import os
sys.path.append(os.environ.get('ENVPATH', '/Users/miner34006/Documents/python/algo_bot'))

from abc import ABCMeta, abstractmethod


class Base_broker():
    __metaclass__ = ABCMeta

    @abstractmethod
    def buy(self, ticker, amount):
        pass
        
    @abstractmethod
    def sell(self, ticker, amount):
        pass