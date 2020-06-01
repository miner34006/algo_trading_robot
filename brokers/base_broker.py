import sys
import os
sys.path.append(os.environ.get('ENVPATH', '/Users/miner34006/Documents/python/algo_bot'))

from abc import ABCMeta, abstractmethod


class Base_broker():
    __metaclass__ = ABCMeta

    @abstractmethod
    def buy(self, ticker, amount):
        """ Function to buy assert on stock exchange

        :param ticker: ticker of the assert
        :type ticker: str
        :param amount: amount of assert to buy
        :type amount: int
        """
        pass
        
    @abstractmethod
    def sell(self, ticker, amount):
        """ Function to buy assert on stock exchange

        :param ticker: ticker of the assert
        :type ticker: str
        :param amount: amount of assert to sell
        :type amount: int
        """
        pass