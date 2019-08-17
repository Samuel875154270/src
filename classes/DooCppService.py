import common
import json
import os
import socket
import time


def concat_result(list1, list2):
    """
    处理结果
    :param list1:
    :param list2:
    :return:
    """
    list1 = sorted(list1, key=lambda x: list(x.items())[0][0])
    list2 = sorted(list2, key=lambda x: list(x.items())[0][0])

    if len(list1) != len(list2):
        return False

    result = []
    for l in range(len(list1)):
        result.append({
            "request_id": list1[l]["request_id"],
            "request": list1[l],
            "response": list2[l],
        })

    return result


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
    request_data = []

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

    def send(self, cmd, server_id, licences, request_data=None, request_return_type=1, count=0):
        """
        发送数据
        :param cmd:
        :param server_id:
        :param licences:
        :param request_data:
        :param request_return_type:
        :param count:
        :return:
        """
        if request_data is None:
            request_data = {}

        data = gateway_params(cmd, server_id, request_data, licences, request_return_type)
        self.request_data.append(data)  # 记录每次请求的参数

        # 拼接数据格式
        data = "W{}QUIT".format(json.dumps(data)).encode()
        # print("发送前")
        start_time = time.time()
        print("程序{}".format(count), cmd,
              "开始时间：{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))),
              "\n请求参数：{}".format(data))
        self.client.send(data)
        # print("发送后")

        # try:
        #     # print("接收前")
        #     content = b""
        #     data = ""
        #     while data is not False:
        #         data = self.client.recv(1024)
        #         content += data
        #         if content[len(content) - 5:] == b'end\r\n':
        #             break
        #
        #     end_time = time.time()
        #     if cmd == "multi_new_order":
        #         print("程序{}".format(count), cmd,
        #               "结束时间：{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))),
        #               "执行用时：{}ms".format(round((end_time - start_time) * 1000)), "\n返回结果：{}".format(content))
        #     else:
        #         print("程序{}".format(count), cmd,
        #               "结束时间：{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))),
        #               "执行用时：{}ms".format(round((end_time - start_time) * 1000)), "\n返回结果：{}".format(content))
        #     return content
        # except socket.timeout as e:
        #     print(cmd, "接收超时：", e)
        # except Exception as e:
        #     print(cmd, "其他错误：", e)

    def receive(self, times=1):
        """
        接收数据
        :param times:
        :return:
        """
        i = 1
        result = b""
        all_result = []
        while times > 0:
            content = self.client.recv(1024)
            result += content
            count = result.count(b"\nend\r\n")
            if count == 0:
                continue
            else:
                result_list = result.split(b"\nend\r\n")
                for r in result_list[:-1]:
                    all_result.append(json.loads(r))
                    name = "{}-{}.log".format(time.strftime("%Y%m%d", time.localtime(time.time())), i)
                    if not os.path.exists(name):
                        file = open(name, "w", encoding="GBK")
                        file.close()
                    if os.path.getsize(name) > 20 * 1024 * 1024:
                        name = "{}-{}.log".format(time.strftime("%Y%m%d", time.localtime(time.time())), i + 1)
                    with open(name, "a", encoding="GBK") as file:
                        file.write("Time: {}\nResult: {}\n\n".format(
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), r))
                result = result_list[-1]

            times -= 1

        finally_result = concat_result(self.request_data, all_result)

        return finally_result

    def tcp_close(self):
        """
        断开TCP连接
        :return:
        """
        self.client.close()
