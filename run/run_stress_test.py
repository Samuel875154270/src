import config
import json
import threading
import time
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

    def new_order_ex(self, params, c=1):
        """
        单个订单开仓
        :param params:
        :param c:
        :return:
        """
        cmd = "new_order_ex"
        self.service.call(self.server_id, self.licences, cmd, params, c)

    def close_order(self, params, c=1):
        """
        单个订单平仓
        :param params:
        :param c:
        :return:
        """
        cmd = "close_order"
        self.service.call(self.server_id, self.licences, cmd, params, c)

    def multi_new_order(self, params, c=1):
        """
        批量开仓
        :param params:
        :param c:
        :return:
        """
        cmd = "multi_new_order"
        self.service.call(self.server_id, self.licences, cmd, params, c)

    def multi_close_order(self, params, c=1):
        """
        批量平仓
        :param params:
        :param c:
        :return:
        """
        cmd = "multi_close_order"
        self.service.call(self.server_id, self.licences, cmd, params, c)

    def get_result(self, count):
        return self.service.get(count)

    def close(self):
        self.service.close()


if __name__ == "__main__":
    # 初始化链接
    social_gateway = config.gateway["social_gateway"]
    service = ConcurrentHandler(social_gateway["host"], social_gateway["port"], social_gateway["server_id"],
                                social_gateway["licences"])

    # 根据login批量开仓
    start_login = 100008
    end_login = 1000008
    # login_1 = list(range(100081, 100455 + 1))
    # login_2 = list(range(170031, 170120 + 1))
    login_list = list(range(start_login, start_login + 1))
    # login_list = [100001, 100002, 100003, 100004, 100005]
    # login_list = login_1
    params = {
        "data_array": []
    }

    length = len(login_list)
    times = int(length / 50) if length % 50 == 0 else int(length / 50) + 1
    print(times)
    for t in range(times):
        for login in login_list[t * 50: (t + 1) * 50]:
            params["data_array"].append(
                {
                    "cmd": 1,
                    "login": login,
                    "symbol": "USDJPY",  # USDJPY、CADJPY、EURGBP、EURUSD
                    "volume": 1,
                    "tp": 0.0,
                    "sl": 0.0,
                    "comment": "stress test",
                    "follow_id": "trader is {}".format(login)
                }
            )
        service.multi_new_order(params)
        params["data_array"] = []

    result = service.get_result(1)
    print(result)

    # # 根据login和order平仓
    # login_order = [
    #     (104500, 192172),
    # ]
    # threads = []
    # for lo in login_order:
    #     params = {
    #         "login": lo[0],
    #         "order": lo[1],
    #     }
    #     th = threading.Thread(target=service.close_order, args=(params,))
    #     th.start()
    #     threads.append(th)
    #
    # for t in threads:
    #     t.join()
    #
    # result = service.get_result(len(threads))
    # for r in result:
    #     print(r)

    # 断开链接
    service.close()
