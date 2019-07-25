import config
import json
import threading
from cpp_service.CppServiceHandler import CppServiceHandler


def multi_call_fun(fun_name, count, *arg):
    for c in range(count):
        eval("{}{}".format(fun_name, arg))


class ConcurrentHandler(object):

    def __init__(self, host, port, server_id, licences):
        """
        初始化
        :param host:
        :param port:
        :param server_id:
        :param licences:
        """
        self.server_id = server_id
        self.licences = licences

        self.service = CppServiceHandler()
        self.service.init(host, port, message_type="TRADE")

    def new_order(self):
        """
        单个订单开仓
        :return:
        """
        cmd = "new_order"
        params = {
            "login": 2089102729,
            "symbol": "EURUSD",
            "volume": 1000,
            "cmd": 0,
            # "sl": 0,
            # "tp": 0,
            "comment": "test001",
            # "expiration_time": 0,
            # "pending_price": 0,
        }
        result = self.service.call(self.server_id, self.licences, cmd, params)
        print(result)

    def new_order_ex(self):
        """
        单个订单开仓
        :return:
        """
        cmd = "new_order_ex"
        params = {
            "login": 2089102729,
            "symbol": "EURUSD",
            "volume": 1000,
            "cmd": 0,
            # "sl": 0,
            # "tp": 0,
            "comment": "test001",
            # "expiration_time": 0,
            # "pending_price": 0,
        }
        result = self.service.call(self.server_id, self.licences, cmd, params)
        print(result)

    def multi_new_order(self):
        """
        批量开仓
        :return:
        """
        cmd = "multi_new_order"
        params = {
            "data_array": []
        }
        for i in range(2):
            params["data_array"].append(
                {
                    "cmd": 1,
                    "comment": "test",
                    "follow_id": "test test",
                    "login": 2089102728,
                    "sl": 0.0,
                    "symbol": "EURUSD",
                    "tp": 0.0,
                    "volume": 1000
                }
            )
        result = self.service.call(self.server_id, self.licences, cmd, params)
        # print(result)

    def get_all_symbolinfo(self):
        """
        获取所有品种信息
        :return:
        """
        cmd = "get_all_symbolinfo"
        params = {}
        result = self.service.call(self.server_id, self.licences, cmd, params)
        # print(result)

    def select_account(self):
        """
        获取用户
        :return:
        """
        cmd = "select_account"
        params = {
            "login": 2089102729
        }
        result = self.service.call(self.server_id, self.licences, cmd, params)
        # print(result)

    def get_opened_order_info(self):
        """
        获取用户在途订单
        :return:
        """
        cmd = "get_opened_order_info"
        params = {
            "login": 2089102729
        }
        result = self.service.call(self.server_id, self.licences, cmd, params)
        # print(result)

    def get_history_order_info(self):
        """
        获取历史订单Order(mt4)
        :return:
        """
        cmd = "get_history_order_info"
        params = {
            "login": 2089102729,
            "from": 0,
            "to": 1563408000
        }
        result = self.service.call(self.server_id, self.licences, cmd, params)
        # print(result)


if __name__ == "__main__":
    social_gateway = config["social_gateway"]
    service = ConcurrentHandler(social_gateway["host"], social_gateway["port"], social_gateway["server_id"], social_gateway["licences"])

    functions = [
        # "new_order",
        "new_order_ex",
        # "multi_new_order",
        # "get_all_symbolinfo",
        # "select_account",
        # "get_opened_order_info",
        # "get_history_order_info"
    ]

    # threads = []
    # for f in functions:
    #     fun_obj = "service.{}".format(f)
    #     th = threading.Thread(target=eval(fun_obj), args=())
    #     th.start()
    #     threads.append(th)
    #
    # for t in threads:
    #     t.join()

    for f in functions:
        fun_obj = "service.{}()".format(f)
        eval(fun_obj)
