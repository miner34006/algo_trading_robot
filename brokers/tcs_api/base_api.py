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
        self.env = env
        self.__token = token
        self.__base_url = self.__get_base_url(env)

    @property
    def env(self):
        """ Function to get current env variable

        :return: current env value
        :rtype: str
        """
        return self.__env

    @env.setter
    def env(self, env):
        """ Function to set a new env

        :param env: new value for env
        :type env: str
        :raises ValueError: incorrect env value
        """
        if env != SANDBOX and env != EXCHANGE:
            raise ValueError('Invalid env value = {0}. Valid values are {1}'.format(env, [SANDBOX, EXCHANGE]))
        self.__env = env
        self.__base_url = self.__get_base_url(env)

    def __get_base_url(self, env):
        """ Function to get base api url according to env value

        :param env: current env
        :type env: str
        :return: base api url
        :rtype: str
        """
        return SANDBOX_URL if env == SANDBOX else EXCHANGE_URL
    
    def __get_auth_header(self, token=None):
        """ Function to get auth header for http request

        :param token: token for auth header, defaults to None
        :type token: str, optional
        :return: auth header
        :rtype: dict
        """
        return {'Authorization': 'Bearer {0}'.format(token or self.__token)}

    def _post(self, endpoint, params=None, json=None, headers=None):
        """ Function for post request api

        :param endpoint: endpoint for request
        :type endpoint: str
        :param params: request params, defaults to None
        :type params: dict, optional
        :param json: json request data, defaults to None
        :type json: dict, optional
        :param headers: request headers, defaults to None
        :type headers: dict, optional
        :return: response from api
        :rtype: dict
        """
        url = self.__base_url + endpoint
        response = requests.post(url, json=json, params=params, headers=headers or self.__get_auth_header())
        REPORT.debug('POST response from <{0}>: {1}'.format(url, response.json()))
        return response.json()

    def _get(self, endpoint, params=None, headers=None):
        """ Function for get request to api

        :param endpoint: endpoint for request
        :type endpoint: str
        :param params: request params, defaults to None
        :type params: dict, optional
        :param headers: request headers, defaults to None
        :type headers: dict, optional
        :return: response from api
        :rtype: dict
        """
        url = self.__base_url + endpoint
        response = requests.get(url, params=params, headers=headers or self.__get_auth_header())
        REPORT.debug('GET response from <{0}>: {1}'.format(url, response.json()))
        return response.json()
        