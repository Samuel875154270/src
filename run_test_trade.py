from run_cpp_service.UnitSocialTradingHandler import UnitSocialTradingHandler
import config
import unittest

gateway = config.trading_system_gateway


class RunOpenCloud(unittest.TestCase):
    service = UnitSocialTradingHandler()
    server_id = gateway["server_id"]
    licences = gateway["licences"]

    @classmethod
    def setUpClass(cls):
        cls.service.init(host=gateway["host"], port=gateway["port"])

    @classmethod
    def tearDownClass(cls):
        cls.service.close()

    def test_subsc_order_info(self):
        """
        订阅推送order
        """
        cmd = "subsc_order_info"
        params = {}
        result = self.service.call(self.server_id, self.licences, cmd, params, is_sub=True)
        print(result)
