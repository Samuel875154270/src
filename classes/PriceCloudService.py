import common
import json
import requests
import time
import socket


def build(data_type, version, data, secret_key):
    timestamp = common.get_timestamp()
    params = {
        "data_type": data_type,
        "data_time": timestamp,
        "version": version,
        "data": data,
    }
    key = common.get_md5("{}{}{}{}".format(data_type, timestamp, version, secret_key))
    params["key"] = key

    return "W{}QUIT".format(json.dumps(params))


class PriceCloudService(object):
    version = "1.0.0"
    size = 2048

    def __init__(self, host, port, secret_key=None):
        """
        初始化
        :param host:
        :param port:
        """
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.client.settimeout(15)  # 设置超时时间，单位：秒
        self.client.connect((host, port))  # 连接地址和端口

        if secret_key is None:
            raise Exception("secret_key was not existed.")
        else:
            self.secret_key = secret_key

    def login(self, username, password):
        """
        检查登录
        :param username:
        :param password:
        :return:
        """
        data_type = 0

        data = {
            "username": username,
            "password": password,
        }

        data = build(data_type, self.version, data, self.secret_key).encode()
        self.client.send(data)
        result = self.client.recv(self.size).decode()
        result = json.loads(result[1:-4])

        return result["data"]

    def get_price(self):
        while True:
            content = self.client.recv(self.size).decode().replace("QUIT", "|").split("|")[0]
            print(content)


class WebPriceCloudService(object):
    size = 2048
    protocol = "http"
    auth_uri = "/auth"
    url = ""
    start_time = 0
    headers = {"X-Auth-Token": None}
    s = requests.session()

    def __init__(self, host, port, up: tuple):
        """
        初始化
        :param host:
        :param port:
        :param up:
        """
        self.host = host
        self.port = port
        self.up = up
        self.init()

    def init(self):
        """
        初始化
        """
        self.start_time = time.time()
        self.url = "{}://{}:{}".format(self.protocol, self.host, self.port)
        r = self.s.post(
            url="{}{}".format(self.url, self.auth_uri),
            json={"u": self.up[0], "p": self.up[1]},
            headers={"Content-Type": "application/json"}
        ).text
        self.headers["X-Auth-Token"] = json.loads(r)["data"]

    def get_symbols(self):
        """
        /symbols，获取品种列表
        :return:
        """
        self.again()
        url = "{}{}".format(self.url, "/symbols")
        r = self.s.get(
            url=url,
            headers=self.headers
        ).text
        r = json.loads(r)
        return r

    def get_market(self, params):
        """
        /market，获取品种报价
        ":param params:
        :return:
        """
        self.again()
        url = "{}{}".format(self.url, "/market")
        r = self.s.get(
            url=url,
            headers=self.headers,
            params=params
        ).text
        r = json.loads(r)
        return r

    def get_kline(self, params):
        """
        /kline，获取品种K线
        ":param params:
        :return:
        """
        self.again()
        url = "{}{}".format(self.url, "/kline")
        r = self.s.get(
            url=url,
            headers=self.headers,
            params=params
        ).text
        r = json.loads(r)
        return r

    def again(self):
        """
        重新获取token
        :return:
        """
        if time.time() - self.start_time >= 50:
            self.init()
