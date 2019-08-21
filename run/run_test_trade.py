from cpp_service.CppServiceHandler import CppServiceHandler
import config
import unittest

gateway = config.gateway["trading_system_gateway"]


class RunOpenCloud(unittest.TestCase):
    service = CppServiceHandler()
    server_id = gateway["server_id"]
    licences = gateway["licences"]

    @classmethod
    def setUpClass(cls):
        cls.service.init(host=gateway["host"], port=gateway["port"], message_type="TRADE")

    @classmethod
    def tearDownClass(cls):
        cls.service.close()

    def test_subsc_order_info(self):
        """
        订阅推送order
        """
        cmd = "subsc_order_info"
        params = {}
        self.service.call(self.server_id, self.licences, cmd, params)
        result = self.service.get()
        print(result)
        return result

    def test_new_account(self):
        """
        订阅推送order
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
        result = self.service.get()
        print(result)
        return result
