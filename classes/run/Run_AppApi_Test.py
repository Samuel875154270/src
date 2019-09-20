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

    # user 相关接口
    # auth 接口
    def test_user_auth_check(self):
        """
        登录状态检查
        :return:
        """
        method = "GET"
        uri = "/v1/user/auth/check"
        params = {
            "device_id": "sam_test_123"
        }
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    def test_user_auth_code(self):
        """
        发送验证码
        :return:
        """
        method = "POST"
        uri = "/v1/user/auth/code"
        params = {
            "type": "email",  # email / phone
            "uemail": "sam.li@doohui.com",
            # "uphonecode": "+86",
            # "uphone": "15820262316"
        }
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    def test_user_auth_validate(self):
        """
        手机邮箱验证码校验
        :return:
        """
        method = "POST"
        uri = "/v1/user/auth/validate"
        params = {
            "type": "email",  # email / phone
            "uemail": "sam.li@doohui.com",
            # "uphonecode": "+86",
            # "uphone": "15820262316"
            "code": ""
        }
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    def test_user_auth_resetPsw(self):
        """
        重置密码
        :return:
        """
        method = "PUT"
        uri = "/v1/user/auth/resetPsw"
        params = {
            "token": "xxx",  # token来自 /v1/user/auth/validate 的返回值
            "password": "abc123"
        }
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    # def test_user_auth_signIn(self):
    #     """
    #     登录校验
    #     :return:
    #     """
    #     method = "POST"
    #     uri = "/v1/user/auth/signIn"
    #     params = {
    #         "uemail": "sam.li@doohui.com",
    #         # "uphonecode": "+86",
    #         # "uphone": "15820262316"
    #         "password": "abc123"
    #     }
    #     rp = self.service.call(method, uri, params)
    #     print(json.dumps(json.loads(rp), indent=2))
    #
    # def test_user_auth_signOut(self):
    #     """
    #     登录校验
    #     :return:
    #     """
    #     method = "POST"
    #     uri = "/v1/user/auth/signOut"
    #     params = {}
    #     rp = self.service.call(method, uri, params)
    #     print(json.dumps(json.loads(rp), indent=2))

    # profile 接口
    def test_user_profile_code(self):
        """
        发送验证码
        :return:
        """

        method = "POST"
        uri = "/v1/user/profile/code"
        params = {
            "type": "email"  # email / phone
        }
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    def test_user_profile_validate(self):
        """
        手机邮箱验证码校验
        :return:
        """

        method = "POST"
        uri = "/v1/user/profile/validate"
        params = {
            "type": "email",  # email / phone
            "code": "xxx"
        }
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    def test_user_profile_update(self):
        """
        更新用户信息
        :return:
        """

        method = "PUT"
        uri = "/v1/user/profile/update"
        params = {
            "token": "xxx",
            "password": "abc123",
            "uemail": "sam.li@doohui.com",
            # "uphonecode": "+86",
            # "uphone": "15820262316"
        }
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    def test_user_profile_avator(self):
        """
        更新用户头像
        :return:
        """

        method = "PUT"
        uri = "/v1/user/profile/avator"
        params = {
            "uhead": {
                "aws": "xxxxx"
            }
        }
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    # notice 接口
    def test_user_notice(self):
        """
        获取通知列表
        :return:
        """

        method = "GET"
        uri = "/v1/user/notice"
        params = {
            "page": 1,
            "pagesize": 3,
            "title": "www",
            "state": "0",  # 通知状态（0： 未读， 1：已读）
        }
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    def test_user_notice_id(self):
        """
        获取通知消息详情
        :return:
        """

        method = "GET"
        uri = "/v1/user/notice/4069"
        params = {}
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    # referral 接口
    def test_user_referral(self):
        """
        获取用户推广链接列表
        :return:
        """

        method = "GET"
        uri = "/v1/user/referral"
        params = {}
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    # setting 接口
    def test_get_user_setting(self):
        """
        获取用户设置
        :return:
        """

        method = "GET"
        uri = "/v1/user/setting"
        params = {
            "keys": "Crm_Time,Crm_Security"
        }
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    def test_put_user_setting(self):
        """
        更新用户设置
        :return:
        """

        method = "PUT"
        uri = "/v1/user/setting"
        params = {
            "data": {
                "Sam": {
                    "k1": "v1"
                }
            }
        }
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    # fund 相关接口
    # wallet 接口
    def test_get_fund_wallet(self):
        """
        获取钱包列表
        :return:
        """

        method = "GET"
        uri = "/v1/fund/wallet"
        params = {}
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    # wallet 接口
    def test_post_fund_account(self):
        """
        新增资金账户（银行卡/电汇/数字货币）
        :return:
        """

        method = "POST"
        uri = "/v1/fund/account"
        params = {}
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    def test_put_fund_account(self):
        """
        更新资金账户（银行卡/电汇/数字货币）
        :return:
        """

        method = "POST"
        uri = "/v1/fund/account"
        params = {}
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    def test_get_fund_account(self):
        """
        获取资金账户（银行卡/电汇/汇款/数字货币）
        :return:
        """

        method = "GET"
        uri = "/v1/fund/account"
        params = {
            "operate": "deposit",  # 操作（deposit / withdrawal）
            "type": "wire"  # deposit时可 wire/remittance/digital；withdrawal时可传wire_transfer/digital_currency/bankcard
        }
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    def test_delete_fund_account(self):
        """
        删除资金账户（银行卡/电汇/数字货币）
        :return:
        """

        method = "GET"
        uri = "/v1/fund/account/xxx"
        params = {
            "id": ""
        }
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    def test_common_file_upload(self):
        """
        上传文件
        :return:
        """
        uri = "/v1/common/file/upload"
        rp = self.service.upload(uri, "../file/photo.png")
        print(json.dumps(json.loads(rp), indent=2))

    # chart 接口
    def test_chart_kline(self):
        """
        获取K线接口
        :return:
        """
        k_type = "1"
        p_dict = {"1": 60, "5": 300, "15": 900, "30": 1800, "60": 3600, "240": 14400, "D": 86400, "W": 604800,
                  "M": 2592000}

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

    # trade 相关接口
    # symbol 接口
    def test_trade_symbol(self):
        """
        获取品种列表
        :return:
        """

        method = "POST"
        uri = "/v1/trade/symbol"
        params = {
            "symbols": [
                "AUDUSD",
                "USDJPY"
            ],
            "types": [0, 1, 2]
        }
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    def test_trade_symbol_detail(self):
        """
        获取品种详情
        :return:
        """

        method = "GET"
        uri = "/v1/trade/symbol/AUDUSD"
        params = {}
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    def test_trade_symbol_quote(self):
        """
        获取品种初始报价
        :return:
        """

        method = "POST"
        uri = "/v1/trade/symbol/quote"
        params = {
            "symbols": [
                "AUDUSD",
                "USDJPY"
            ]
        }
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    # account 接口
    def test_trade_account(self):
        """
        获取关联交易账号列表
        :return:
        """

        method = "GET"
        uri = "/v1/trade/account"
        params = {}
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    def test_trade_account_switch(self):
        """
        切换选择的交易账号
        :return:
        """

        method = "PUT"
        uri = "/v1/trade/account/switch"
        params = {
            "login": 2089103004,
            "server_id": "d06f-1e8d6b745"
        }
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    def test_trade_account_info(self):
        """
        获取交易账号详情
        :return:
        """

        method = "GET"
        uri = "/v1/trade/account/info"
        params = {}
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    # record 接口
    def test_trade_record_history(self):
        """
        获取历史订单
        :return:
        """

        method = "GET"
        uri = "/v1/trade/record/history"
        params = {}
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    def test_trade_record_position(self):
        """
        获取在途订单
        :return:
        """

        method = "GET"
        uri = "/v1/trade/record/position"
        params = {}
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    def test_trade_record_pending(self):
        """
        获取挂单列表
        :return:
        """

        method = "GET"
        uri = "/v1/trade/record/pending"
        params = {}
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    # operate 接口
    def test_trade_operate_place(self):
        """
        交易下单（在途单、挂单）
        :return:
        """
        method = "POST"
        uri = "/v1/trade/operate/place"
        params = {
            "symbol": "EURUSD",
            "cmd": 0,  # buy=0，sell=1，buy limit=2，sell limit=3，buy stop=4，sell stop=5
            "volume": 0.01,
            # "pending_price": 0.01,  # 挂单价格（cmd为2-5时必填）
            # "sl": 0.01,
            # "tp": 0.01
        }
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    def test_trade_operate_update(self):
        """
        订单更新
        :return:
        """
        method = "PUT"
        uri = "/v1/trade/operate/update/xxx"
        params = {
            "symbol": "USDJPY",
            "pending_price": 0.01,  # 挂单价格（cmd为2-5时必填）
            # "sl": 0.01,
            # "tp": 0.01
        }
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    def test_trade_operate_cancel(self):
        """
        挂单取消
        :return:
        """
        method = "DELETE"
        uri = "/v1/trade/operate/cancel/xxx"
        params = {
            "symbol": "USDJPY"
        }
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))

    def test_trade_operate_close(self):
        """
        在途单平仓
        :return:
        """
        method = "DELETE"
        uri = "/v1/trade/operate/close/xxx"
        params = {
            "symbol": "USDJPY",
            # "volume": 0.01  # 平仓手数（不传为全平）
        }
        rp = self.service.call(method, uri, params)
        print(json.dumps(json.loads(rp), indent=2))


if __name__ == "__main__":
    unittest.main()
