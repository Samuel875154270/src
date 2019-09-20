import asyncio
import json
import requests
import threading
import websockets
from urllib.parse import urlencode
from requests_toolbelt import MultipartEncoder


class InTraderApiService(object):
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
        # print("cookies", self.cookies)

    def call(self, method, uri, params=None):
        """
        请求接口
        :param method:
        :param uri:
        :param params:
        :return:
        """
        params = {} if params is None else params
        url = "{}://{}{}".format(self.protocol, self.host, uri)

        rp = json.dumps({"code": -10000, "data": 'The request method must be ["GET", "POST", "PUT", "DELETE"]'})
        if method.upper() not in ["GET", "POST", "PUT", "DELETE"]:
            return rp

        try:
            if method.upper() == "GET":
                url = "{}?{}".format(url, urlencode(params).replace("+", "%20").replace("%27", "%22"))
                rp = self.http.get(url, cookies=self.cookies).text
            elif method.upper() == "POST":
                rp = self.http.post(url, cookies=self.cookies, json=params, headers=self.headers).text
            elif method.upper() == "PUT":
                rp = self.http.put(url, cookies=self.cookies, json=params, headers=self.headers).text
            elif method.upper() == "DELETE":
                rp = self.http.delete(url, cookies=self.cookies, json=params, headers=self.headers).text
            return rp
        except Exception as e:
            print(e)
            return False

    def upload(self, uri, file_path):
        """
        上传文件接口
        :param uri:
        :param file_path:
        :return:
        """
        url = "{}://{}{}".format(self.protocol, self.host, uri)

        file = open(file_path, "rb")
        data = MultipartEncoder(
            fields={
                "file": (file_path.split("/")[-1], file)
            }
        )
        self.headers["Content-Type"] = data.content_type
        try:
            rp = self.http.post(url, cookies=self.cookies, data=data, headers=self.headers).text
            return rp
        except Exception as e:
            print(e)
            return False
        finally:
            file.close()

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

    def run_ws(self, uri):
        """

        :param uri:
        :return:
        """
        asyncio.new_event_loop().run_until_complete(self.ws_call(uri))
        asyncio.new_event_loop().run_forever()

    def th_run(self, uri):
        """

        :param uri:
        :return:
        """
        th = threading.Thread(target=service.run_ws, args=(uri,))
        th.setDaemon(True)
        th.start()


if __name__ == "__main__":
    api_host = "192.168.1.203:12972"
    # api_host = "192.168.1.183:9000"
    api_login_uri = "/v1/user/auth/signIn"
    api_login_params = {"uemail": "sam.li@doohui.com", "password": "abc123"}

    service = InTraderApiService(api_host)
    service.init(api_login_uri, api_login_params)

    asyncio.new_event_loop().run_until_complete(service.ws_call("/v1/ws/quote"))
    asyncio.new_event_loop().run_forever()

    # r = service.call("GET", "/v1/user/fund/wallet", {})
    # print(r)
