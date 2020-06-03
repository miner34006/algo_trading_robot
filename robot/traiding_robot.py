import sys
import os
sys.path.append(os.environ.get('ENVPATH', '/Users/miner34006/Documents/python/algo_bot'))

import operator
import datetime
import time

import utils.consts as consts


class Traiding_robot(object):
    def __init__(self, broker, strategy):
        self.broker = broker
        self.strategy = strategy

    def get_historical_data(self, ticker, from_datetime, to_datetime, interval):
        """ Function to get historical data for trading

        :param ticker: ticker name
        :type ticker: str
        :param from_datetime: from date time value
        :type from_datetime: datetime.datetime
        :param to_datetime: to date time value
        :type to_datetime: datetime.datetime
        :param interval: time interval (day, hour etc.)
        :type interval: str
        :return: list with historical data from api
        :rtype: list
        """
        figi = self.broker.api.market.search_by_ticker(ticker)['payload']['instruments'][0]['figi']
        days_delta = consts.Time_intervals.INTERVALS_DELTA[interval]

        historical_data = []
        while from_datetime < to_datetime - datetime.timedelta(seconds=1):
            delta = to_datetime - from_datetime if from_datetime + datetime.timedelta(days=days_delta) > to_datetime \
                else datetime.timedelta(days=days_delta) 
            
            historical_data += self.broker.api.market.get_market_candles(
                figi=figi, interval=interval,
                from_datetime=from_datetime.strftime(consts.Base.DATE_TIME_FORMAT), 
                to_datetime=(from_datetime + delta).strftime(consts.Base.DATE_TIME_FORMAT)
            )['payload']['candles']
            from_datetime += delta         
        return historical_data

    def run(self, ticker, lots=1, sleep_time=60):
        """ Function to run trading algorithm

        :param ticker: ticker to trade
        :type ticker: str
        :param lots: number of lots to trade
        :type lots: int, optional
        :param sleep_time: sleep time before checking, defaults to 60
        :type sleep_time: int, optional
        """
        to_datetime = datetime.datetime.now()
        from_datetime = to_datetime - datetime.timedelta(days=30)
        while True:
            historical_data = get_historical_data(ticker, from_datetime, to_datetime)
            # if self.strategy.need_to_buy(historical_data):
            #     self.broker.buy(ticker, amount=lots)
            # elif self.strategy.need_to_sell(historical_data):
            #     self.broker.sell(ticker, amount=lots)
            time.sleep(sleep_time)

    def test_startegy(self, ticker, from_datetime, to_datetime, interval, lots=1, strategy=None, print_results=True):
        """ Function to test strategy

        :param ticker: ticker for testing
        :type ticker: str
        :param from_datetime: start datetime for testing
        :type from_datetime: datetime.datetime
        :param to_datetime: end datetime for testing
        :type to_datetime: datetime.datetime
        :param interval: candle type (hour, day, month)
        :type interval: str
        :param lots: number of lots to trade
        :type lots: int, optional
        :param strategy: strategy to test
        :type strategy: base_strategy.Base_strategy
        :param print_results: print testing results
        :type print_results: bool
        :return: testing results
        :rtype: backtest.Backtest
        """
        strategy = strategy or self.strategy
        historical_data = self.get_historical_data(ticker, from_datetime, to_datetime, interval)
        backtest = strategy.back_test_strategy(historical_data)
        if print_results:
            backtest.print_results()
        return backtest

    