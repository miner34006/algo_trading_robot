import sys
import os
sys.path.append(os.environ.get('ENVPATH', '/Users/miner34006/Documents/python/algo_bot'))

import datetime

import pytest
from mock import Mock, call

import robot.traiding_robot as traiding_robot
from utils.consts import Time_intervals, Base
from tests.base_strategy_tests import historical_data


@pytest.fixture
def robot():
    from robot.traiding_robot import Traiding_robot
    from brokers.tcs_broker import Tcs_broker
    from robot.strategies.base_strategy import Base_strategy

    robot = traiding_robot.Traiding_robot(Tcs_broker(None, 'sandbox'), Base_strategy())
    get_market_candles_mock = Mock(return_value={'payload': {'candles': historical_data}})
    search_by_ticker_mock = Mock(return_value={'payload': {'instruments': [{'figi': 'TEST_FIGI'}]}})
    robot.broker.api.market.get_market_candles = get_market_candles_mock
    robot.broker.api.market.search_by_ticker = search_by_ticker_mock
    return robot

def test_get_historical_data_with_day_interval_one_cycle(robot):
    """ Test one interval historical data get with day interval

    :param robot: mocked robot
    :type robot: traiding_robot.Traiding_robot
    """
    interval = Time_intervals.DAY
    from_datetime = datetime.datetime.now() - datetime.timedelta(days=10)
    to_datetime = datetime.datetime.now()
    data = robot.get_historical_data('TICKER', from_datetime=from_datetime, to_datetime=to_datetime, interval='day')

    robot.broker.api.market.search_by_ticker.assert_called_once_with('TICKER')
    robot.broker.api.market.get_market_candles.assert_called_once_with(
        figi='TEST_FIGI', interval='day', from_datetime=from_datetime.strftime(Base.DATE_TIME_FORMAT), 
        to_datetime=to_datetime.strftime(Base.DATE_TIME_FORMAT))
    assert data == historical_data

def test_get_historical_data_with_hour_interval_one_cycle(robot):
    """ Test one interval historical data get with hour interval

    :param robot: mocked robot
    :type robot: traiding_robot.Traiding_robot
    """
    interval = Time_intervals.HOUR
    from_datetime = datetime.datetime.now() - datetime.timedelta(days=5)
    to_datetime = datetime.datetime.now()
    data = robot.get_historical_data('TICKER', from_datetime=from_datetime, to_datetime=to_datetime, interval=interval)

    robot.broker.api.market.search_by_ticker.assert_called_once_with('TICKER')
    robot.broker.api.market.get_market_candles.assert_called_once_with(
        figi='TEST_FIGI', interval=interval, from_datetime=from_datetime.strftime(Base.DATE_TIME_FORMAT), 
        to_datetime=to_datetime.strftime(Base.DATE_TIME_FORMAT))
    assert data == historical_data

def test_get_historical_data_with_day_interval_several_cycles(robot):
    """ Test several interval historical data get with day interval

    :param robot: mocked robot
    :type robot: traiding_robot.Traiding_robot
    """
    interval = Time_intervals.DAY
    from_datetime = datetime.datetime.now() - datetime.timedelta(days=365+123)
    to_datetime = datetime.datetime.now()
    data = robot.get_historical_data('TICKER', from_datetime=from_datetime, to_datetime=to_datetime, interval=interval)

    robot.broker.api.market.search_by_ticker.assert_called_once_with('TICKER')
    calls = [
        call(figi='TEST_FIGI', interval=interval, 
             from_datetime=from_datetime.strftime(Base.DATE_TIME_FORMAT), 
             to_datetime=(from_datetime + datetime.timedelta(days=Time_intervals.INTERVALS_DELTA[interval])).strftime(Base.DATE_TIME_FORMAT)),
        call(figi='TEST_FIGI', interval=interval, 
             from_datetime=(from_datetime + datetime.timedelta(days=Time_intervals.INTERVALS_DELTA[interval])).strftime(Base.DATE_TIME_FORMAT), 
             to_datetime=to_datetime.strftime(Base.DATE_TIME_FORMAT)),
    ]
    robot.broker.api.market.get_market_candles.assert_has_calls(calls, any_order=False)
    assert data == historical_data * 2


def test_get_historical_data_with_hour_interval_several_cycles(robot):
    """ Test several interval historical data get with hour interval

    :param robot: mocked robot
    :type robot: traiding_robot.Traiding_robot
    """
    interval = Time_intervals.HOUR
    from_datetime = datetime.datetime.now() - datetime.timedelta(days=7+3)
    to_datetime = datetime.datetime.now()
    data = robot.get_historical_data('TICKER', from_datetime=from_datetime, to_datetime=to_datetime, interval=interval)

    robot.broker.api.market.search_by_ticker.assert_called_once_with('TICKER')
    calls = [
        call(figi='TEST_FIGI', interval=interval, 
             from_datetime=from_datetime.strftime(Base.DATE_TIME_FORMAT), 
             to_datetime=(from_datetime + datetime.timedelta(days=Time_intervals.INTERVALS_DELTA[interval])).strftime(Base.DATE_TIME_FORMAT)),
        call(figi='TEST_FIGI', interval=interval, 
             from_datetime=(from_datetime + datetime.timedelta(days=Time_intervals.INTERVALS_DELTA[interval])).strftime(Base.DATE_TIME_FORMAT), 
             to_datetime=to_datetime.strftime(Base.DATE_TIME_FORMAT)),
    ]
    robot.broker.api.market.get_market_candles.assert_has_calls(calls, any_order=False)
    assert data == historical_data * 2