# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.environ.get('ENVPATH', '/Users/miner34006/Documents/python/algo_bot'))

from utils.logger import get_logger


REPORT = get_logger(__name__)


class Backtest():
    def __init__(self, total_buy=0, total_sell=0):
        self.total_buy = total_buy
        self.total_sell = total_sell
        
        self.total_profit = 0
        self.total_profit_percent = 0
        self.last_buy_price = 0
        self.last_sell_price = 0
        self.in_position = False
        self.recalculate()

    def recalculate(self):
        """ Function to recalculate data
        """
        if self.total_sell and self.total_buy:
            self.total_profit = self.total_sell - self.total_buy
            self.total_profit_percent = round((self.total_profit / self.total_buy) * 100, 2)

    def print_results(self,):
        """ Function to print testing results
        """
        self.recalculate()
        REPORT.info('Total BUY = {0}'.format(self.total_buy))
        REPORT.info('Total SELL = {0}'.format(self.total_sell))
        REPORT.info('Total PROFIT = {0}'.format(self.total_profit))
        REPORT.info('Total PROFIT PERCENT = {0}%'.format(self.total_profit_percent))
        REPORT.info('In position = {0}'.format(self.in_position))
