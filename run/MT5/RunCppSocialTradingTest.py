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
        # cls.service = Service(host="192.168.1.228", port=9400, server_id="d0a9-838c7e7f4",
        #                       licenses="5fc1873d-a582-44c4-9235-b4d57c7cbe96", time_out=60)  # 测试环境
        cls.service = Service(port=9400, server_id="42ec-d1106b09e", licenses="756de4c5-2ed6-42eb-9217-3d4f9675d8f6",
                              time_out=60)
        cls.message_type = "TRADE"

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
        result = json.loads(self.result)
        self.assertEqual(result["response_data"]["response_status"], 0)

    def test_api_position_trade(self):
        """
        MT5 在途订单开仓、修改、平仓，API使用
        :return:
        """
        login, symbol, volume = 40240022, "USDJPY", 100
        open_result, update_result, close_result = None, None, None
        # 开仓
        request_data = {
            "login": login,
            "symbol": symbol,
            "volume": volume,
            "cmd": 0,
            "sl": 83.011,
            "tp": 140.021,
            "comment": "from tcp test"
        }
        open_cmd = "new_order_ex"
        request_id = str(uuid.uuid4())
        self.service.send(request_id, self.message_type, open_cmd, request_data, 1)
        open_result = self.service.receive()
        print(open_cmd, open_result)

        open_result_dict = json.loads(open_result)
        if open_result_dict["response_data"].get("response_status") == 0:
            # 平仓
            request_data = {
                "login": login,
                "order": open_result_dict["response_data"]["order"],
                "volume": volume
            }
            close_cmd = "close_order"
            request_id = str(uuid.uuid4())
            self.service.send(request_id, self.message_type, close_cmd, request_data, 1)
            close_result = self.service.receive()
            print(close_cmd, close_result)

        for result in [close_result, update_result, open_result]:
            if result is None:
                continue
            else:
                self.result = result
                break

    def test_position_trade(self):
        """
        MT5 在途订单开仓、修改、平仓
        :return:
        """
        login, symbol, volume = 40240022, "USDJPY", 100
        open_result, update_result, close_result = None, None, None
        # 开仓
        request_data = {
            "login": login,
            "symbol": symbol,
            "volume": volume,
            "cmd": 1,
            "sl": 70,
            "tp": 80,
            "comment": "from tcp test"
        }
        open_cmd = "new_order"
        request_id = str(uuid.uuid4())
        self.service.send(request_id, self.message_type, open_cmd, request_data, 1)
        open_result = self.service.receive()
        print(open_cmd, open_result)

        open_result_dict = json.loads(open_result)
        if open_result_dict["response_data"].get("response_status") == 0:
            # 修改
            request_data = {
                "login": login,
                "symbol": symbol,
                "order": open_result_dict["response_data"]["order"],
                "sl": 100.01,
                "tp": 120.02,
                "comment": "from tcp test"
            }
            update_cmd = "update_order"
            request_id = str(uuid.uuid4())
            self.service.send(request_id, self.message_type, update_cmd, request_data, 1)
            update_result = self.service.receive()
            print(update_cmd, update_result)

        if update_result is not None:
            # 平仓
            request_data = {
                "login": login,
                "order": open_result_dict["response_data"]["order"],
                "volume": volume
            }
            close_cmd = "close_order"
            request_id = str(uuid.uuid4())
            self.service.send(request_id, self.message_type, close_cmd, request_data, 1)
            close_result = self.service.receive()
            print(close_cmd, close_result)

        for result in [close_result, update_result, open_result]:
            if result is None:
                continue
            else:
                self.result = result
                break

    def test_multi_trade(self):
        """
        MT5 批量开仓、批量平仓
        :return:
        """
        login, symbol, volume, follow_id = 40240022, "USDJPY", 100, "multi test 123"
        open_result, close_result = None, None

        # 批量开仓
        data_list: List[Dict[Any, Union[int, str, float, int, float, float, str, str]]] = []
        for i in range(100):
            data_list.append(dict(
                login=login,
                symbol=symbol,
                volume=volume,
                cmd=0,
                sl=70.002,
                tp=150.004,
                comment="from tcp test",
                follow_id=follow_id
            ))
        request_data = {
            "data_array": data_list
        }
        open_cmd = "multi_new_order"
        request_id = str(uuid.uuid4())
        self.service.send(request_id, self.message_type, open_cmd, request_data, 1)
        open_result = self.service.receive()
        print(open_cmd, open_result)

        open_result_dict = json.loads(open_result)
        if open_result_dict["response_data"].get("response_status") == 0:
            # 批量平仓
            order_list = open_result_dict["response_data"]["data_array"]
            print(order_list)
            close_data_list: List[Dict[Any, Union[int, int, float, int]]] = []
            for order in order_list:
                close_data_list.append(dict(
                    login=login,
                    order=order["order"],
                    follow_id=follow_id,
                    volume=volume
                ))
            request_data = {
                "data_array": close_data_list
            }
            close_cmd = "multi_close_order"
            request_id = str(uuid.uuid4())
            self.service.send(request_id, self.message_type, close_cmd, request_data, 1)
            close_result = self.service.receive()
            print(close_cmd, close_result)

        for result in [close_result, open_result]:
            if result is None:
                continue
            else:
                self.result = result
                break

    def test_pending_trade(self):
        """
        MT5 创建挂单、修改挂单、关闭挂单
        :return:
        """
        login, symbol, volume = 40240022, "USDJPY", 100
        open_result, update_result, close_result = None, None, None
        # 创建挂单
        request_data = {
            "login": login,
            "symbol": symbol,
            "volume": volume,
            "cmd": 2,
            "sl": 210,
            "tp": 220,
            "comment": "from tcp test pending",
            "pending_price": 100.01,
            "expiration_time": common.get_timestamp() + 3600
        }
        open_cmd = "new_order"
        request_id = str(uuid.uuid4())
        self.service.send(request_id, self.message_type, open_cmd, request_data, 1)
        open_result = self.service.receive()
        print(open_cmd, open_result)

        open_result_dict = json.loads(open_result)
        if open_result_dict["response_data"].get("response_status") == 0:
            # 修改挂单
            request_data = {
                "login": login,
                "symbol": symbol,
                "order": open_result_dict["response_data"]["order"],
                "sl": 90.011,
                "tp": 130.031,
                "pending_price": 100.02,
                "expiration_time": common.get_timestamp() + 7200
            }
            update_cmd = "update_order"
            request_id = str(uuid.uuid4())
            self.service.send(request_id, self.message_type, update_cmd, request_data, 1)
            update_result = self.service.receive()
            print(update_cmd, update_result)

        if update_result is not None:
            # 关闭挂单
            request_data = {
                "login": login,
                "order": open_result_dict["response_data"]["order"]
            }
            close_cmd = "delete_order"
            request_id = str(uuid.uuid4())
            self.service.send(request_id, self.message_type, close_cmd, request_data, 1)
            close_result = self.service.receive()
            print(close_cmd, close_result)

        for result in [close_result, update_result, open_result]:
            if result is None:
                continue
            else:
                self.result = result
                break

    def test_check_pwd(self):
        """
        MT5 校验主密码
        :return:
        """
        request_data = {
            "login": 40240022,
            "password": "abc123"
        }
        cmd = "check_pwd"
        request_id = str(uuid.uuid4())
        self.service.send(request_id, self.message_type, cmd, request_data, 1)
        self.result = self.service.receive()

    def test_position_of_login(self):
        """
        MT5 获取账号在途订单
        :return:
        """
        request_data = {
            "login": 40240022
        }
        cmd = "get_opened_order_info"
        request_id = str(uuid.uuid4())
        self.service.send(request_id, self.message_type, cmd, request_data, 1)
        self.result = self.service.receive()

    def test_order_status(self):
        """
        MT5 获取订单状态
        :return:
        """
        request_data = {
            "login": 40240022,
            "order": 1347456
        }
        cmd = "get_order_status"
        request_id = str(uuid.uuid4())
        self.service.send(request_id, self.message_type, cmd, request_data, 1)
        self.result = self.service.receive()

    def test_get_login(self):
        """
        MT5 获取账号
        :return:
        """
        request_data = {
            "login": 40240022
        }
        cmd = "select_account"
        request_id = str(uuid.uuid4())
        self.service.send(request_id, self.message_type, cmd, request_data, 1)
        self.result = self.service.receive()

    def test_get_all_login(self):
        """
        MT5 获取所有账号
        :return:
        """
        request_data = {}
        cmd = "get_all_login"
        request_id = str(uuid.uuid4())
        self.service.send(request_id, self.message_type, cmd, request_data, 1)
        self.result = self.service.receive()

    def test_get_all_order_of_login(self):
        """
        MT5 获取账号所有的订单数
        :return:
        """
        request_data = {
            "login": 40240022
        }
        cmd = "get_user_ordercount"
        request_id = str(uuid.uuid4())
        self.service.send(request_id, self.message_type, cmd, request_data, 1)
        self.result = self.service.receive()

    def test_get_all_symbol(self):
        """
        MT5 获取所有品种信息
        :return:
        """
        request_data = {}
        cmd = "get_all_symbolinfo"
        request_id = str(uuid.uuid4())
        self.service.send(request_id, self.message_type, cmd, request_data, 1)
        self.result = self.service.receive()

    def test_get_symbol(self):
        """
        MT5 获取单个品种信息
        :return:
        """
        request_data = {
            "symbol": "USDJPY"
        }
        cmd = "get_symbolinfo"
        request_id = str(uuid.uuid4())
        self.service.send(request_id, self.message_type, cmd, request_data, 1)
        self.result = self.service.receive()


if __name__ == "__main__":
    unittest.main()
