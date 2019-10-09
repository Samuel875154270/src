import asyncio
import json
import requests
import threading
import websockets
from urllib.parse import urlencode


class InTraderWsService(object):
    protocol = "http"
    ws_protocol = "ws"
    headers = {"Content-Type": "application/json"}
    cookies = dict()

    def __init__(self, host, uri="/v1/user/auth/check", params=None):
        """
        初始化，检查登录状态
        :param host:
        """
        self.http = requests.Session()

        self.host = host
        params = {"device_id": "sam_test_123"} if params is None else params

        url = "{}://{}{}".format(self.protocol, self.host, uri)
        url = "{}?{}".format(url, urlencode(params).replace("+", "%20").replace("%27", "%22"))
        init = self.http.get(url, headers=self.headers)
        # print(init.text)
        self.ws_cookies = dict(init.cookies)
        # print("ws_cookies", self.ws_cookies)

    def init(self, login_uri, login_params):
        """
        登录获取cookies
        :param login_uri:
        :param login_params:
        """
        url = "{}://{}{}".format(self.protocol, self.host, login_uri)
        rp = self.http.post(url, json=login_params, headers=self.headers)
        self.cookies = dict(rp.cookies)
        # print(rp.text)
        # print("cookies", self.cookies)

    async def ws_call(self, uri):
        """
        web_socket 连接获取推送
        :param uri:
        :return:
        """
        ws_url = "{}://{}{}".format(self.ws_protocol, self.host, uri)
        headers = {
            "Cookie": "SID={}".format(self.cookies["SID"])
        }
        async with websockets.connect(ws_url, extra_headers=headers, ping_interval=20) as web_socket:
            while True:
                result = await web_socket.recv()
                print(result)
                # return result


if __name__ == "__main__":
    api_host = "192.168.1.203:12972"
    api_login_uri = "/v1/user/auth/signIn"
    api_login_params = {"uemail": "sam.li@doohui.com", "password": "abc123"}

    service = InTraderWsService(api_host)
    service.init(api_login_uri, api_login_params)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(service.ws_call("/v1/ws/quote"))
    # loop.run_forever()

