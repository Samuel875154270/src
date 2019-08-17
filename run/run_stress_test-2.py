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

    def get_opened_order_info(self, params, c=1):
        """
        批量平仓
        :param params:
        :param c:
        :return:
        """
        cmd = "get_opened_order_info"
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

    # # 根据login批量开仓
    # start_login, end_login = 100001, 100001
    # login_list = list(range(start_login, end_login + 1))
    # params = {
    #     "data_array": []
    # }
    # for login in login_list:
    #     params["data_array"].append(
    #         {
    #             "cmd": 1,
    #             "login": login,
    #             "symbol": "USDJPY",  # USDJPY、CADJPY、EURGBP、EURUSD
    #             "volume": 10,
    #             "tp": 0.0,
    #             "sl": 0.0,
    #             "comment": "stress test",
    #             "follow_id": "trader is {}".format(login)
    #         }
    #     )
    # service.multi_new_order(params)
    # result = service.get_result(1)
    # print(result)

    login = 100008
    # 根据login获取在途订单
    service.get_opened_order_info(params={"login": login})
    position = service.get_result(1)[0]["response"]["response_data"]["data_array"][0]
    login_order = []
    for p in position:
        login_order.append((p["login"], p["order"]))
    print(len(login_order))
    # 根据login和order平仓
    # login_order = [
    #     (100003, 192292),
    # ]
    threads = []
    for lo in login_order:
        params = {
            "login": lo[0],
            "order": lo[1],
        }
        print(params)
        th = threading.Thread(target=service.close_order, args=(params,))
        th.start()
        threads.append(th)

    for t in threads:
        t.join()

    result = service.get_result(len(threads))
    result = result if result else []
    for r in result:
        print(r)

    # 断开链接
    service.close()
