import config
import json
import threading
import time
from functools import reduce
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

    def new_order(self, c=1):
        """
        单个订单开仓
        :param c:
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
        result = self.service.call(self.server_id, self.licences, cmd, params, c)
        print(result)

    def new_order_ex(self, c=1):
        """
        单个订单开仓
        :param c:
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
        result = self.service.call(self.server_id, self.licences, cmd, params, c)
        print(result)

    def multi_new_order(self, c=1):
        """
        批量开仓
        :param c:
        :return:
        """
        # time.sleep(1)
        cmd = "multi_new_order"
        params = {
            "data_array": []
        }
        for i in range(1):
            params["data_array"].append(
                {
                    "cmd": 0,
                    "comment": "test",
                    "follow_id": "test test",
                    "login": 101001,
                    "sl": 0.0,
                    "symbol": "EURUSD",
                    "tp": 0.0,
                    "volume": 1
                }
            )
        # for i in [25945, 104499]:
        #     params["data_array"].append(
        #         {
        #             "cmd": 1,
        #             "comment": "test",
        #             "follow_id": "test test",
        #             "login": i,
        #             "sl": 0.0,
        #             "symbol": "EURAUD",
        #             "tp": 0.0,
        #             "volume": 200
        #         }
        #     )
        result = self.service.call(self.server_id, self.licences, cmd, params, c)
        # print(result)

    def get_all_symbolinfo(self, c=1):
        """
        获取所有品种信息
        :param c:
        :return:
        """
        cmd = "get_all_symbolinfo"
        params = {}
        result = self.service.call(self.server_id, self.licences, cmd, params, c)
        # print(result)

    def select_account(self, c=1):
        """
        获取用户
        :param c:
        :return:
        """
        cmd = "select_account"
        params = {
            "login": 2089102729
        }
        result = self.service.call(self.server_id, self.licences, cmd, params, c)
        # print(result)

    def get_opened_order_info(self, c=1):
        """
        获取用户在途订单
        :param c:
        :return:
        """
        cmd = "get_opened_order_info"
        params = {
            "login": 2089102729
        }
        result = self.service.call(self.server_id, self.licences, cmd, params, c)
        # print(result)

    def get_history_order_info(self, c=1):
        """
        获取历史订单Order(mt4)
        :param c:
        :return:
        """
        cmd = "get_history_order_info"
        params = {
            "login": 2089102729,
            "from": 0,
            "to": 1563408000
        }
        result = self.service.call(self.server_id, self.licences, cmd, params, c)
        # print(result)

    def get_all_login(self, c=1):
        """
        查询所有账号(mt4)
        :param c:
        :return:
        """
        cmd = "get_all_login"
        params = {}
        result = self.service.call(self.server_id, self.licences, cmd, params, c)
        # print(result)

    def select_account(self, c=1):
        """
        查询账号(mt5)
        :param c:
        :return:
        """
        cmd = "select_account"
        params = {
            "login": 40240012
        }
        result = self.service.call(self.server_id, self.licences, cmd, params, c)
        # print(result)

    def many(self, fun_list):
        """
        批量请求不同接口
        :param fun_list:
        :return:
        """

        new_threads = []
        for fun in fun_list:
            item = list(fun.items())[0]
            name = item[0]
            count = item[1]
            for i in range(1, count + 1):
                print("self.{}".format(name), i)
                new_th = threading.Thread(target=eval("self.{}".format(name)), args=(i,))
                new_th.start()
                new_threads.append(new_th)

            for new_t in new_threads:
                new_t.join()

    def get_result(self, count):
        return self.service.get(count)

    def close(self):
        self.service.close()


if __name__ == "__main__":
    social_gateway = config.gateway["social_gateway"]
    service = ConcurrentHandler(social_gateway["host"], social_gateway["port"], social_gateway["server_id"],
                                social_gateway["licences"])
    # service = ConcurrentHandler("192.168.1.190", 9117, social_gateway["server_id"],
    #                             social_gateway["licences"])

    fun_name_list = [
        # {"new_order_ex": 100},
        # {"get_all_symbolinfo": 1},
        # {"select_account": 1},
        # {"get_opened_order_info": 1},
        # {"get_all_login": 1},
        {"multi_new_order": 1},
        # {"select_account": 2},
    ]
    count = reduce(lambda x, y: x + y, list(map(lambda item: list(item.values())[0], fun_name_list)))

    service.many(fun_name_list)
    result = service.get_result(count)
    service.close()
    print(result)
