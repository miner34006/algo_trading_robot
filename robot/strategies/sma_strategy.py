# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.environ.get('ENVPATH', '/Users/miner34006/Documents/python/algo_bot'))

import talib

from robot.strategies.base_strategy import Base_strategy
from robot.strategies.backtest import Backtest
from utils.logger import get_logger


REPORT = get_logger(__name__)


class SMA_strategy(Base_strategy):
    def __init__(self, long_period=26, short_period=12, stop_loss=0.02, take_profit=0.1):
        if short_period > long_period:
            raise ValueError('Long period must be more than short period! ({0} < {1})'
                             .format(long_period, short_period))
        super(SMA_strategy, self).__init__(stop_loss=stop_loss, take_profit=take_profit)
        self.long_period = long_period
        self.short_period = short_period
        self.name = self.__class__.__name__
        
    def has_buy_signal(self, historical_data):
        """ Function to check if strategy has buy signal

        :param historical_data: list with historical data from api
        :type historical_data: list
        :return: strategy has buy signal
        :rtype: bool
        """
        merged_data = self.merge_candles(historical_data)
        ma_long = talib.EMA(merged_data['close'], timeperiod=self.long_period)
        ma_short = talib.EMA(merged_data['close'], timeperiod=self.short_period)
        has_buy_signal =  ma_long[-2] > ma_short[-2] and ma_long[-1] < ma_short[-1]
        if has_buy_signal:
            REPORT.info('Found buy signal at {0}'.format(historical_data[-1]['time']))
        return has_buy_signal
        
    def has_sell_signal(self, historical_data):
        """ Function to check if strategy has sell signal

        :param historical_data: list with historical data from api
        :type historical_data: list
        :return: strategy has sell signal
        :rtype: bool
        """
        merged_data = self.merge_candles(historical_data)
        ma_long = talib.EMA(merged_data['close'], timeperiod=self.long_period)
        ma_short = talib.EMA(merged_data['close'], timeperiod=self.short_period)
        has_sell_signal = ma_long[-2] < ma_short[-2] and ma_long[-1] > ma_short[-1]
        if has_sell_signal:
            REPORT.info('Found sell signal at {0}'.format(historical_data[-1]['time']))
        return has_sell_signal
    
    def back_test_strategy(self, historical_data):
        """ Function to test strategy on hostorical data

        :param historical_data: historical data from api
        :type historical_data: list
        :return: back test results
        :rtype: backtest.Backtest
        """
        if len(historical_data) < self.long_period:
            raise ValueError('Historical data is too short for creating MA data.'\
                             'Historical length = {0}, but long period = {1}'
                             .format(len(historical_data), self.long_period))

        backtest_stats = Backtest()
        for candle_index in range(len(historical_data)):
            if candle_index < self.long_period + 1:
                continue
            
            time_period = historical_data[:candle_index]
            close_price = time_period[-1]['c']
            stop_loss = self.has_stop_loss_signal(
                enter_price=backtest_stats.last_buy_price, 
                current_price=close_price) if backtest_stats.in_position else False
            take_profit = self.has_take_profit_signal(
                enter_price=backtest_stats.last_buy_price, 
                current_price=close_price) if backtest_stats.in_position else False

            if self.has_buy_signal(time_period) and not backtest_stats.in_position:
                backtest_stats.in_position = True
                backtest_stats.total_buy += close_price
                backtest_stats.last_buy_price = close_price

            elif backtest_stats.in_position and (self.has_sell_signal(time_period) or stop_loss or take_profit):
                backtest_stats.in_position = False
                backtest_stats.total_sell += close_price
                profit = close_price - backtest_stats.last_buy_price
        return backtest_stats

