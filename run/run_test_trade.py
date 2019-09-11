from cpp_service.CppServiceHandler import CppServiceHandler
import config
import json
import time
import unittest

gateway = config.gateway["trading_system_gateway"]


class RunOpenCloud(unittest.TestCase):
    service = CppServiceHandler()
    server_id = gateway["server_id"]
    licences = gateway["licences"]

    @classmethod
    def setUpClass(cls):
        """
        初始化链接TCP
        :return:
        """
        cls.service.init(host=gateway["host"], port=gateway["port"], message_type="TRADE")
        cls.log_name = "./log/test_case{}.log".format(time.strftime("%Y%m%d", time.localtime(time.time())))
        cls.error_log_name = "./log/error_log_name{}.log".format(time.strftime("%Y%m%d", time.localtime(time.time())))

    @classmethod
    def tearDownClass(cls):
        """
        断开TCP
        :return:
        """
        cls.service.close()

    def setUp(self):
        """

        :return:
        """
        self.start_time_stamp = time.time()
        self.start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.start_time_stamp))

    def tearDown(self):
        """

        :return:
        """
        now = time.time()
        self.end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now))
        self.time_diff = round((now - self.start_time_stamp) * 1000, 2)
        msg = "start_time: {}|end_time: {}|time: {}s\n".format(self.start_time, self.end_time, self.time_diff)
        with open(self.log_name, "a") as f:
            f.write(msg)
            f.write(json.dumps(self.result[0]))
            f.write("\n\n")

        if self.result[0]["response"]["response_data"]["response_status"] != 0:
            with open(self.error_log_name, "a") as e:
                e.write(msg)
                e.write(json.dumps(self.result[0]))
                e.write("\n\n")

    def test_subsc_order_info(self):
        """
        订阅推送order
        """
        cmd = "subsc_order_info"
        params = {}
        self.service.call(self.server_id, self.licences, cmd, params)
        self.result = self.service.get()
        print(self.result)
        return self.result

    def test_new_account(self):
        """
        新建账号account
        """
        if self.test_subsc_order_info()[0]["response"]["response_data"]["response_details"] == "O.K.":
            print("OK")
        cmd = "new_account"
        params = {
            "login": 10260,
            "name": "trading system gateway",
            "group": "demo\samtest",
            "password": "abc123",
            "investor_password": "abc124",
            "leverage": 200,
            "email": "2029100780@test.com",
            "phone": "2029100780",
            "enable_change_password": 1,
            "read_only": 0,
            "enable": 1,
            "default_deposit": 1000,
        }
        self.service.call(self.server_id, self.licences, cmd, params)
        self.result = self.service.get()
        print(self.result)
        return self.result
