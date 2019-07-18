import config
import json
import threading
from cpp_service.CppServiceHandler import CppServiceHandler


class ConcurrentHandler(object):
    message_type = "TRADE"

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

    def multi_new_order(self):
        """
        批量开仓
        :return:
        """
        cmd = "multi_new_order"
        params = {}
        result = self.service.call(self.server_id, self.licences, cmd, params)
        print(result)

    def get_all_symbolinfo(self):
        """
        获取所有品种信息
        :return:
        """
        cmd = "get_all_symbolinfo"
        params = {}
        result = self.service.call(self.server_id, self.licences, cmd, params)
        print(result)


if __name__ == "__main__":
    gateway = config.trading_system_gateway
    service = ConcurrentHandler(gateway["host"], gateway["port"], gateway["server_id"], gateway["licences"])
