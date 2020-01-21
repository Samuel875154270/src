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
        cls.service = Service(port=9600)
        # cls.message_type = "TRADE"
        cls.message_type = "TradingSystem"

    def setUp(self):
        """
        用例初始化
        :return:
        """
        self.result = "{}"

    def test_subsc_trade_info(self):
        """
        MT4 订阅trade信息
        :return:
        """
        request_data = {}
        cmd = "subsc_trade_info"
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
