from typing import Dict, List, Any, Union
from classes.LocalCpp import Service
import common
import json
import uuid
import unittest


def get(service, message_type, cmd, request_data, count=1):
    """
    循环请求
    :param service:
    :param message_type:
    :param cmd:
    :param request_data:
    :param count:
    :return:
    """
    for i in range(count):
        request_id = str(uuid.uuid4())

        service.service.send(request_id, message_type, cmd, request_data)
        result = service.receive()
        yield result


def console(result):
    """
    打印迭代器的结果
    :param result:
    :return:
    """
    for r in result:
        print(r)


class RunCppTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        对象初始化
        :return:
        """
        cls.service = Service(port=9600, server_id="d0a9-838c7e7f4", licenses="5fc1873d-a582-44c4-9235-b4d57c7cbe96",
                              time_out=300)
        cls.message_type = "TradingSystem"

    def setUp(self):
        """
        用例初始化
        :return:
        """
        self.result = "{}"

    def test_subsc_order_info(self):
        """
        MT5 订阅order信息
        :return:
        """
        request_data = {}
        cmd = "subsc_order_info"
        request_id = str(uuid.uuid4())
        self.service.send(request_id, self.message_type, cmd, request_data, 1)
        self.result = self.service.receive()
        result = json.loads(self.result)
        if result["response_data"]["response_status"] == 0 and result["response_data"]["response_details"] == "O.K.":
            print("订阅 {} 成功。".format(cmd), result)

        for ws_result in self.service.ws_receive():
            print(ws_result)

    def test_subsc_deal_info(self):
        """
        MT5 订阅deal信息
        :return:
        """
        request_data = {}
        cmd = "subsc_deal_info"
        request_id = str(uuid.uuid4())
        self.service.send(request_id, self.message_type, cmd, request_data, 1)
        self.result = self.service.receive()
        result = json.loads(self.result)
        if result["response_data"]["response_status"] == 0 and result["response_data"]["response_details"] == "O.K.":
            print("订阅 {} 成功。".format(cmd), result)

        for ws_result in self.service.ws_receive():
            print(ws_result)

    def test_subsc_position_info(self):
        """
        MT5 订阅position信息
        :return:
        """
        request_data = {}
        cmd = "subsc_position_info"
        request_id = str(uuid.uuid4())
        self.service.send(request_id, self.message_type, cmd, request_data, 1)
        self.result = self.service.receive()
        result = json.loads(self.result)
        if result["response_data"]["response_status"] == 0 and result["response_data"]["response_details"] == "O.K.":
            print("订阅 {} 成功。".format(cmd), result)

        for ws_result in self.service.ws_receive():
            print(ws_result)


if __name__ == "__main__":
    unittest.main()
