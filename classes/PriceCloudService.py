import common
import json
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


class TCPService(object):
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
        result = self.client.recv(self.size).decode()[1:-4]
        print(result)
        result = json.loads(result)

        return result["data"]

    def get_price(self):
        while True:
            content = self.client.recv(self.size).decode().replace("QUIT", "|").split("|")[0]
            print(content)
