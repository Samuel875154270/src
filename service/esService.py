import json
import requests
import tornado.concurrent
from .baseService import Executor
from tornado.httpclient import AsyncHTTPClient
from urllib.parse import urlencode

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
}


class ExecutorRequest(object):
    executor = Executor()

    @tornado.concurrent.run_on_executor
    def call(self, method, url, params=None):
        """

        :param method:
        :param url:
        :param params:
        :return:
        """
        method = method.upper()
        if params is None:
            params = {}

        if method in ["POST", "PUT", "PATCH"]:
            rp = requests.request(
                method=method,
                url=url,
                json=params,
                headers=headers
            )
        else:
            params = urlencode(params).replace('+', '%20').replace('%27', '%22')
            rp = requests.request(
                method=method,
                url=f"{url}?{params}",
                headers=headers
            )
        return rp.content
