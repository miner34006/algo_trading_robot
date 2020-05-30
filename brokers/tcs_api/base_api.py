import sys
import os
sys.path.append(os.environ.get('ENVPATH', '/Users/miner34006/Documents/python/algo_bot'))

import logging
import requests

from . import REPORT

SANDBOX = 'sandbox'
EXCHANGE = 'exchange'

SANDBOX_URL = 'https://api-invest.tinkoff.ru/openapi/sandbox'
EXCHANGE_URL = 'https://api-invest.tinkoff.ru/openapi'


class Base_api(object):
    def __init__(self, token, env=SANDBOX):
        self.token = token
        self.env = env
        self.__base_url = self.__get_base_url(env)

    @property
    def env(self):
        return self.__env

    @env.setter
    def env(self, env):
        if env != SANDBOX and env != EXCHANGE:
            raise ValueError('Invalid env value = {0}. Valid values are {1}'.format(env, [SANDBOX, EXCHANGE]))
        self.__env = env
        self.__base_url = self.__get_base_url(env)

    def __get_base_url(self, env):
        return SANDBOX_URL if env == SANDBOX else EXCHANGE_URL
    
    def __get_auth_header(self, token=None):
        return {'Authorization': 'Bearer {0}'.format(token or self.token)}

    def post(self, endpoint, json=None, headers=None):
        url = self.__base_url + endpoint
        response = requests.post(url, json=json, headers=headers or self.__get_auth_header())
        REPORT.debug('POST response from <{0}>: {1}'.format(url, response.json()))
        return response.json()

    def get(self, endpoint, params=None, headers=None):
        url = self.__base_url + endpoint
        response = requests.get(url, params=params, headers=headers or self.__get_auth_header())
        REPORT.debug('GET response from <{0}>: {1}'.format(url, response.json()))
        return response.json()
        