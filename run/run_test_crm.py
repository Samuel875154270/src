from cpp_service.CppServiceHandler import CppServiceHandler
import config
import unittest

gateway = config.gateway["crm_gateway"]


class RunOpenCloud(unittest.TestCase):
    service = CppServiceHandler()
    server_id = gateway["server_id"]
    licences = gateway["licences"]

    @classmethod
    def setUpClass(cls):
        cls.service.init(host=gateway["host"], port=gateway["port"], message_type="CRM")

    @classmethod
    def tearDownClass(cls):
        cls.service.close()

    def test_check_connect(self):
        """
        检验MT连接
        """
        cmd = "check_connect"
        params = {}
        result = self.service.call(self.server_id, self.licences, cmd, params)
        print(result)

    # def test_new_account(self):
    #     """
    #     创建MT账号
    #     """
    #     cmd = "new_account"
    #     params = {
    #         "login": 123460,
    #         "name": "Test TCP",
    #         "group": "demoforex",
    #         "password": "abc123",
    #         "investor_password": "abc124",
    #         "phone_password": "abc125",
    #         "leverage": 200,
    #         "id_number": "abc-111",
    #         "email": "test@tcp.com",
    #         "phone": "12345678910",
    #         "status": "en",
    #         "country": "中国",
    #         "state": "广东省",
    #         "city": "深圳市",
    #         "zip_code": "123456",
    #         "address": "Test address",
    #         "agent_account": 0,
    #         "read_only": 0,
    #         "enable_change_password": 1,
    #         "enable": 1,
    #         "lead_source": "TCP Api Request",
    #         "comment": "TCP TEST",
    #         "default_deposit": 0.01
    #     }
    #     result = self.service.call(self.server_id, self.licences, cmd, params)
    #     print(result)
