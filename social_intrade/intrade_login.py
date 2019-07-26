import config
import json
import requests


class InTrade(object):

    def login(self, login_url, login_params):
        """
        登录并获取cookies
        :param login_url:
        :param login_params:
        :return:
        """

    def call(self, url, method, params, headers=None):
        """

        :param url:
        :param method:
        :param params:
        :param headers:
        :return:
        """
        headers = config.web_headers if headers is None else headers

        s = requests.session()
        if method.upper() == "GET":
            response = s.get(url=url, headers=headers).text
        elif method.upper() == "POST":
            response = s.post(url=url, json=params, headers=headers).text
        elif method.upper() == "PUT":
            response = s.put(url=url, json=params, headers=headers).text
        elif method.upper() == "PATCH":
            response = s.patch(url=url, json=params, headers=headers).text
        elif method.upper() == "DELETE":
            response = s.delete(url=url, json=params, headers=headers).text
        else:
            response = s.head(url=url, headers=headers).text

        response = json.loads(response)
        return response
