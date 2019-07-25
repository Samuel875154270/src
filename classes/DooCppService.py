import common
import json
import socket
import struct
import time


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


class DooCppService(object):
    client = False

    def init(self, host, port):
        """
        开启TCP连接
        :param host:
        :param port:
        :return:
        """
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.client.settimeout(30)  # 设置超时时间，秒
        self.client.connect((host, port))  # 连接地址和端口

    def send(self, cmd, server_id, licences, request_data=None, request_return_type=1):
        """
        发送数据
        :param cmd:
        :param server_id:
        :param licences:
        :param request_data:
        :param request_return_type:
        :return:
        """
        t = time.time()
        if request_data is None:
            request_data = {}

        data = gateway_params(cmd, server_id, request_data, licences, request_return_type)

        # 拼接数据格式
        data = "W{}QUIT".format(json.dumps(data)).encode()
        print(data)
        # print("发送前")
        self.client.send(data)
        # print("发送后")

        try:
            # 接收报头长度
            res = self.client.recv(4)
            # print(res)
            # 对报头长度解压
            header_size = struct.unpack('i', res)[0]
            # print(header_size)
            # 接收报头长度的内容
            header_bytes = self.client.recv(header_size)
            content = res + header_bytes
            # content = (res + header_bytes).decode("gbk").replace("\nend\r\n", "")
            print(cmd, "开始时间：{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))))
            print(cmd, "执行时间：{}ms".format(round((time.time() - t) * 1000)))
            return content
        except socket.timeout as e:
            print("接收超时：", e)
        except Exception as e:
            print("其他错误：", e)

        # try:
        #     # print("接收前")
        #     content = b""
        #     while True:
        #         data = self.client.recv(1024)
        #         content += data
        #         if b"\nend\r\n" in data:
        #             break
        #     content = content.decode().split("\nend\r\n")
        #     # print("接收后")
        #     return content
        # except socket.timeout as e:
        #     print("接收超时：", e)
        # except Exception as e:
        #     print("其他错误：", e)

    def receive(self):
        """
        接收数据
        :return:
        """
        try:
            # 接收报头长度
            res = self.client.recv(4)
            # print(res)
            # 对报头长度解压
            header_size = struct.unpack('i', res)[0]
            # print(header_size)
            # 接收报头长度的内容
            header_bytes = self.client.recv(header_size)
            content = res + header_bytes
            # content = (res + header_bytes).decode("gbk").replace("\nend\r\n", "")
            return content

        except socket.timeout as e:
            print("接收超时：", e)
        except Exception as e:
            print("其他错误：", e)

    # def receive(self, size=1024):
    #     """
    #     接收数据
    #     :param: size
    #     :return:
    #     """
    #     try:
    #         # print("接收前")
    #         content = b""
    #         while True:
    #             data = self.client.recv(size)
    #             content += data
    #             if b"\nend\r\n" in data:
    #                 break
    #         content = content.decode().split("\nend\r\n")
    #         # print("接收后")
    #         return content
    #     except socket.timeout as e:
    #         print("接收超时：", e)
    #     except Exception as e:
    #         print("其他错误：", e)

    def tcp_close(self):
        """
        断开TCP连接
        :return:
        """
        self.client.close()
