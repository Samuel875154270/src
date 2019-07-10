import common
import json
import socket


def gateway_params(cmd, server_id, request_data, licences, request_return_type=1, is_sub=False):
    """
    拼接组合gateway访问数据
    :param cmd:
    :param server_id:
    :param request_data:
    :param licences:
    :param request_return_type:
    :param is_sub:
    :return:
    """
    request_id = common.get_uuid()
    message_type = request_data.get("message_type")
    request_time = common.get_timestamp()
    # md5 加密参数
    request_key = common.get_md5("{}|{}|{}|{}".format(request_id, message_type, request_time, licences))
    # 网关参数格式
    params = {
        "request_id": request_id,
        "message_type": message_type,
        "request_key": request_key,
        "request_zone": request_data.get("request_zone"),
        "server_id": server_id,
        "cmd": cmd,
        "request_time": request_time,
        "request_data": request_data.get("request_data")
    }
    if is_sub is False:
        params["request_return_type"] = 1 if request_return_type == 1 else 0

    return params


class DooCppSubService(object):
    client = False

    def init(self, host, port):
        """
        开启TCP连接
        :param host:
        :param port:
        :return:
        """
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.client.settimeout(15)  # 设置超时时间，秒
        self.client.connect((host, port))  # 连接地址和端口

    def send(self, cmd, server_id, licences, request_data=None, request_return_type=1, is_sub=False):
        """
        发送数据
        :param cmd:
        :param server_id:
        :param licences:
        :param request_data:
        :param request_return_type:
        :param is_sub:
        :return:
        """
        if request_data is None:
            request_data = {}

        data = gateway_params(cmd, server_id, request_data, licences, request_return_type, is_sub)

        # 拼接数据格式
        data = "W{}QUIT".format(json.dumps(data)).encode()
        # print(data)
        # print("发送前")
        self.client.send(data)
        # print("发送后")

    def receive(self, size=1024, name=""):
        """
        接收数据
        :param: name
        :return:
        """
        content = ""
        while True:
            data = self.client.recv(size).decode()
            content += data
            if "\nend\r\n" in data:
                break
        content = content.replace("\nend\r\n", "")
        return json.loads(content)["response_data"]

    async def long_receive(self, size=1024, name=""):
        """
        长链接接收数据
        :param: name
        :return:
        """
        while True:
            content = ""
            while True:
                data = self.client.recv(size).decode()
                content += data
                if "\nend\r\n" in data:
                    break
            content = content.replace("\nend\r", "")
            print("{}".format(name), json.loads(content)["response_data"]["data_body"])

    def tcp_close(self):
        """
        断开TCP连接
        :return:
        """
        self.client.close()
