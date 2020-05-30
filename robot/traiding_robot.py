import sys
import os
sys.path.append(os.environ.get('ENVPATH', '/Users/miner34006/Documents/python/algo_bot'))

from . import REPORT


class Traiding_robot(object):
    def __init__(self, broker, strategy):
        self.broker = broker
        self.strategy = strategy


if __name__ == "__main__":
    from brokers.tcs_api.tinkoff_api import Tinkoff_api
    from brokers.tcs_broker import Tcs_broker
    from api.tcs_api.base_api import SANDBOX

    token = os.environ.get('API_TOKEN')
    broker = Tcs_broker(token, SANDBOX)

    robot = Traiding_robot(broker, None)
    