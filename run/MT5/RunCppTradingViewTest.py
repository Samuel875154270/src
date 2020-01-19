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
    i = 1
    for r in result:
        print(i, r)
        i += 1


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

    def tearDown(self):
        """
        用例断言
        :return:
        """
        print(self.result)
        # result = json.loads(self.result)
        # result["now"] = common.get_timestamp()
        # with open("kline.json", "w") as file:
        #     file.write(json.dumps(result, indent=4))

        result = json.loads(self.result)
        self.assertEqual(result["response_data"]["response_status"], 0)

    def test_get_chart(self):
        """
        MT5 获取图表
        :return:
        """
        # period：1 / 5 / 15 / 30 / 60 / 240 / 1440 / 10080 / 43200
        request_data = {
            "symbol": "USDJPY",
            "from": common.get_timestamp() - 3600 * 24 * 5,
            "to": common.get_timestamp(),
            "period": 1
        }
        cmd = "get_chart"
        request_id = str(uuid.uuid4())
        self.service.send(request_id, self.message_type, cmd, request_data, 1)
        self.result = self.service.receive()

    def test_get_mt_info(self):
        """
        MT5 获取时区
        :return:
        """
        request_data = {}
        cmd = "get_mt_info"
        request_id = str(uuid.uuid4())
        self.service.send(request_id, self.message_type, cmd, request_data, 1)
        self.result = self.service.receive()

    def test_get_group_info(self):
        """
        MT5 获取组信息
        :return:
        """
        request_data = {}
        cmd = "get_group_info"
        request_id = str(uuid.uuid4())
        self.service.send(request_id, self.message_type, cmd, request_data, 1)
        self.result = self.service.receive()

    def test_get_history_order_info(self):
        """
        MT5 获取历史订单
        :return:
        """
        request_data = {
            "login": 2089106302,
            "from": 0,
            "to": common.get_timestamp(),
        }
        cmd = "get_history_order_info"
        request_id = str(uuid.uuid4())
        self.service.send(request_id, self.message_type, cmd, request_data, 1)
        self.result = self.service.receive()

    def test_get_symbol_tick(self):
        """
        MT5 获取品种报价信息
        :return:
        """
        request_data = {
            "symbol": "USDJPY"
        }
        cmd = "get_symbol_tick"
        request_id = str(uuid.uuid4())
        self.service.send(request_id, self.message_type, cmd, request_data, 1)
        self.result = self.service.receive()

    def test_multi_get_symbol_tick(self):
        """
        MT5 获取品种报价信息
        :return:
        """
        request_data = {
            "data_array": [
                {"symbol": "USDJPY"},
                {"symbol": "GBPUSD"},
                {"symbol": "EURUSD"},
            ]
        }
        cmd = "multi_get_symbol_tick"
        request_id = str(uuid.uuid4())
        self.service.send(request_id, self.message_type, cmd, request_data, 1)
        self.result = self.service.receive()


if __name__ == "__main__":
    unittest.main()
