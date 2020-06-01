import sys
import os
sys.path.append(os.environ.get('ENVPATH', '/Users/miner34006/Documents/python/algo_bot'))

import pytest

from robot.strategies.base_strategy import Base_strategy

expected_keys = ['open', 'close', 'high', 'low', 'value']
historical_data = [
        {'o': 1, 'c': 2, 'l': 0, 'h': 3, 'v': 5},
        {'o': 2, 'c': 3, 'l': 1, 'h': 4, 'v': 6},
        {'o': 1, 'c': 2, 'l': 0, 'h': 3, 'v': 5},
        {'o': 2, 'c': 3, 'l': 1, 'h': 4, 'v': 6},
]


def test_stop_loss_none():
    """ Test stop loss signal when stop loss percent was set to None
    """
    strategy = Base_strategy(stop_loss=None)
    assert strategy.has_stop_loss_signal(enter_price=100, current_price=90) == False
    assert strategy.has_stop_loss_signal(enter_price=100, current_price=110) == False

def test_take_profit_none():
    """ Test take profit signal when take profit percent was set to None
    """
    strategy = Base_strategy(take_profit=None)
    assert strategy.has_take_profit_signal(enter_price=100, current_price=90) == False
    assert strategy.has_take_profit_signal(enter_price=100, current_price=110) == False

def test_stop_loss_valid():
    """ Test stop loss signal when it has valid value
    """
    strategy = Base_strategy(stop_loss=0.01)
    assert strategy.has_stop_loss_signal(enter_price=100, current_price=90) == True
    assert strategy.has_stop_loss_signal(enter_price=100, current_price=99) == True
    assert strategy.has_stop_loss_signal(enter_price=100, current_price=100) == False
    assert strategy.has_stop_loss_signal(enter_price=100, current_price=101) == False

def test_take_profit_valid():
    """ Test take profit signal when it has valid value
    """
    strategy = Base_strategy(take_profit=0.01)
    assert strategy.has_take_profit_signal(enter_price=100, current_price=99) == False
    assert strategy.has_take_profit_signal(enter_price=100, current_price=100) == False
    assert strategy.has_take_profit_signal(enter_price=100, current_price=101) == True
    assert strategy.has_take_profit_signal(enter_price=100, current_price=110) == True

def test_merge_candles_keys():
    """ Test all keys are presented in merged data
    """
    strategy = Base_strategy()
    merged_data = strategy.merge_candles(historical_data)
    for expected_key in expected_keys:
        assert expected_key in merged_data

def test_merge_candles_values():
    """ Test data is merged correct
    """
    strategy = Base_strategy()
    merged_data = strategy.merge_candles(historical_data)
    for expected_key in expected_keys:
        assert len(merged_data[expected_key]) == len(historical_data)
        for index, day_data in enumerate(historical_data):
            assert day_data[expected_key[0]] == merged_data[expected_key][index]