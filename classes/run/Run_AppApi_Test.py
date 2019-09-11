import json
import time
import unittest
from classes.InTraderAppApi import InTraderApiService


class RunTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        实例化对象
        :return:
        """
        host = "192.168.1.203:12972"
        cls.service = InTraderApiService(host)

        login_uri = "/v1/user/auth/signIn"
        login_params = {"uemail": "sam.li@doohui.com", "password": "abc123"}
        cls.service.init(login_uri, login_params)

    @classmethod
    def tearDownClass(cls):
        """
        结束实例化对象
        :return:
        """
        # method = "POST"
        # uri = "/v1/user/auth/signOut"
        # cls.service.call(method, uri)
        pass

    def setUp(self):
        """

        :return:
        """
        pass

    def tearDown(self):
        """

        :return:
        """
        pass

    def test_user_auth_code(self):
        """
        发送验证码
        :return:
        """
        method = "POST"
        uri = "/v1/user/auth/code"
        params = {
            "type": "email",
            "uemail": "sam.li@doohui.com"
        }
        rp = self.service.call(method, uri, params)
        print(rp)

    def test_chart_kline(self):
        """
        获取K线接口
        :return:
        """
        k_type = "1"
        p_dict = {"1": 60, "5": 300, "15": 900, "30": 1800, "60": 3600, "240": 14400, "D": 86400, "W": 604800, "M": 2592000}

        method = "GET"
        uri = "/v1/chart/kline"
        params = {
            "symbol": "USDJPY",
            "period": k_type,
            "from": int(time.time()) - p_dict.get(k_type) | 60,
            "to": int(time.time())
        }
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    def test_user_auth_place(self):
        """
        交易下单
        :return:
        """
        method = "POST"
        uri = "/v1/trade/operate/place"
        params = {
            "symbol": "USDJPY",
            "cmd": 1,
            "volume": 0.01
        }
        rp = self.service.call(method, uri, params)
        print(rp)

    def test_user_auth_referral(self):
        """
        获取推广链接
        :return:
        """
        method = "GET"
        uri = "/v1/user/referral"
        params = {}
        rp = self.service.call(method, uri, params)
        print(rp)


if __name__ == "__main__":
    unittest.main()
