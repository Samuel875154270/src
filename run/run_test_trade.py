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
        result = self.service.call(self.server_id, self.licences, cmd, params)
        print(result)
