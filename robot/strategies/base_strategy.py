# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.environ.get('ENVPATH', '/Users/miner34006/Documents/python/algo_bot'))

import operator
from abc import ABCMeta, abstractmethod

import numpy as np

from utils.logger import get_logger


REPORT = get_logger(__name__)


class Base_strategy():
    __metaclass__ = ABCMeta
    def __init__(self, stop_loss=0.02, take_profit=0.1):
        self.stop_loss = stop_loss
        self.take_profit = take_profit

    def has_stop_loss_signal(self, enter_price, current_price):
        """ Function to check if strategy has stop loss signal

        :param enter_price: buy price of assert
        :type enter_price: float
        :param current_price: current assert price
        :type current_price: float
        :return: has signal for stop loss
        :rtype: bool
        """
        return current_price <= enter_price * (1 - self.stop_loss) if self.stop_loss else False

    def has_take_profit_signal(self, enter_price, current_price):
        """ Function to check if strategy has take profit signal

        :param enter_price: buy price of assert
        :type enter_price: float
        :param current_price: current assert price
        :type current_price: float
        :return: has signal for take profit
        :rtype: bool
        """
        return current_price >= enter_price * (1 + self.take_profit) if self.take_profit else False
    
    def merge_candles(self, historical_data):
        """ Function to make data valid for testing

        :param historical_data: historical data from api
        :type historical_data: list
        :return: historical data in dict format
        :rtype: dict
        """
        merged_data = {
            'open': np.array(list(map(operator.itemgetter('o'), historical_data))),
            'close': np.array(list(map(operator.itemgetter('c'), historical_data))),
            'high': np.array(list(map(operator.itemgetter('h'), historical_data))),
            'low': np.array(list(map(operator.itemgetter('l'), historical_data))),
            'value': np.array(list(map(operator.itemgetter('v'), historical_data))),
        }
        return merged_data

    @abstractmethod
    def has_buy_signal(self, historical_data):
        """ Function to check if strategy has buy signal

        :param historical_data: historical data from api
        :type historical_data: list
        :return: strategy has buy signal
        :rtype: bool
        """
        pass
        
    @abstractmethod
    def has_sell_signal(self, historical_data):
        """ Function to check if strategy has sell signal

        :param historical_data: historical data from api
        :type historical_data: list
        :return: strategy has sell signal
        :rtype: bool
        """
        pass
    
    @abstractmethod
    def back_test_strategy(self, historical_data):
        """ Function to test strategy on hostorical data

        :param historical_data: historical data from api
        :type historical_data: list
        :return: back test results
        :rtype: backtest.Backtest
        """        
        pass
