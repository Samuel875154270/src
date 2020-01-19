import common
import json
import socket


class Service(object):
    _client = False

    def __init__(self, server_id=None, host=None, port=0, licenses=None, request_zone=None, time_out=None):
        """
        初始化
        :param server_id:
        :param host:
        :param port:
        :param licenses:
        :param request_zone:
        :param time_out:
        """
        self._server_id = "d06f-1e8d6b745" if server_id is None else server_id
        self._licenses = "e656b991-5706-4cb1-af8f-f69323f8f7e4" if licenses is None else licenses
        self._request_zone = "A" if request_zone is None else request_zone

        _host = "127.0.0.1" if host is None else host
        _port = 9500 if port is 0 else port
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client.connect((_host, _port))
        if time_out is None:
            self._client.settimeout(20)
        else:
            self._client.settimeout(time_out)

    def send(self, request_id, message_type, cmd, request_data=None, request_return_type=None):
        """
        进行TCP请求
        :param request_id:
        :param message_type:
        :param cmd:
        :param request_data:
        :param request_return_type:
        :return:
        """
        if request_data is None:
            request_data = {}

        params = self._create_message(request_id, message_type, cmd, request_data, request_return_type)
        print(params)
        self._client.send(params)

    def receive(self, size=0, end=b"end\r\n"):
        """
        接收TCP结果
        :param size:
        :param end:
        :return:
        """
        size = 1024 if size is 0 else size
        end_length = len(end)
        message: bytes = b""
        content = b""
        while message is not False:
            message = self._client.recv(size)
            content += message
            message_length, content_length = len(message), len(content)
            if message[message_length - end_length:] == end or (
                    content_length > 0 and content[content_length - end_length:] == end):
                break

        return content.decode()[:-5]

    def ws_receive(self, size=0, end=b"end\r\n"):
        """
        订阅推送TCP结果
        :param size:
        :param end:
        :return:
        """
        size = 1024 if size is 0 else size
        content = b""
        while True:
            content += self._client.recv(size)
            if end in content:
                message = content.split(end)
                content = end.join(message[1:])
                yield message[0].decode()
            else:
                continue

    def _create_message(self, request_id, message_type, cmd, request_data, request_return_type=None):
        """
        拼接请求参数
        :param request_id:
        :param message_type:
        :param cmd:
        :param request_data:
        :param request_return_type:
        :return:
        """
        request_time = common.get_timestamp()
        request_key = common.get_md5(f"{request_id}|{message_type}|{request_time}|{self._licenses}")  # 生成加密key

        params = dict(request_id=request_id, message_type=message_type, request_key=request_key,
                      request_zone=self._request_zone, server_id=self._server_id, cmd=cmd, request_time=request_time,
                      request_data=request_data)
        if request_return_type is not None:
            params["request_return_type"] = request_return_type

        params = f"W{json.dumps(params)}QUIT"

        return params.encode()

    # def __del__(self):
    #     """
    #     断开TCP连接
    #     :return:
    #     """
    #     self._client.close()
