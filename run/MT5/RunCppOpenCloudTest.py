from typing import Dict, List, Any, Union
from classes.LocalCpp import Service
import json
import uuid
import unittest


def get(service, message_type, cmd, request_data, count=1):
    """
    循环请求
    :param service:
    :param message_type:
    :param cmd:
    :param request_data:
    :param count:
    :return:
    """
    for i in range(count):
        request_id = str(uuid.uuid4())

        service.service.send(request_id, message_type, cmd, request_data)
        result = service.receive()
        yield result


def console(result):
    """
    打印迭代器的结果
    :param result:
    :return:
    """
    i = 1
    for r in result:
        print(i, r)
        i += 1


class RunCppTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        对象初始化
        :return:
        """
        cls.service = Service(host="192.168.1.228", server_id="d0a9-838c7e7f4", licenses="5fc1873d-a582-44c4-9235-b4d57c7cbe96", time_out=10)  # 测试环境
        # cls.service = Service(server_id="d0a9-838c7e7f4", licenses="5fc1873d-a582-44c4-9235-b4d57c7cbe96", time_out=10)
        cls.message_type = "CRM"

    def setUp(self):
        """
        用例初始化
        :return:
        """
        self.result = "{}"

    def tearDown(self):
        """
        用例断言
        :return:
        """
        print(self.result)
        result = json.loads(self.result)
        code = result["response_data"]["response_status"] if result["response_data"]["response_status"] != 66318 else 0
        self.assertEqual(code, 0)

    def test_1_create_account(self):
        """
        MT5 注册账号
        :return:
        """
        request_data = {
            "login": 40240016,
            "name": "TCP TEST",
            "group": "demo\samtest",
            "password": "abc123",
            "investor_password": "abc124",
            "leverage": 200,
            "enable": 1
        }
        cmd = "new_account"

        request_id = str(uuid.uuid4())

        self.service.send(request_id, self.message_type, cmd, request_data)
        self.result = self.service.receive()

    def test_2_update_account(self):
        """
        MT5 更新账号信息
        :return:
        """
        request_data = {
            "login": 40240016,
            "name": "TCP TEST",
            "group": "demo\samtest",
            "leverage": 100,
            "enable": 0
        }
        cmd = "update_account"

        request_id = str(uuid.uuid4())

        self.service.send(request_id, self.message_type, cmd, request_data)
        self.result = self.service.receive()

    def test_3_delete_account(self):
        """
        MT5 删除账号
        :return:
        """
        request_data = {
            "login": 40240016
        }
        cmd = "delete_account"

        request_id = str(uuid.uuid4())

        self.service.send(request_id, self.message_type, cmd, request_data)
        self.result = self.service.receive()

    def test_deposit(self):
        """
        MT5 入金
        :return:
        """
        request_data = {
            "login": 40240022,
            "deposit": 0.99,
            "comment": "Deposit 一二三四五六七八九十一二三四五六七八九十"
        }
        cmd = "deposit"

        request_id = str(uuid.uuid4())

        self.service.send(request_id, self.message_type, cmd, request_data)
        self.result = self.service.receive()

    def test_withdrawal(self):
        """
        MT5 出金
        :return:
        """
        request_data = {
            "login": 40240022,
            "withdrawal": 0.01,
            "comment": "Withdrawal 一二三四五六七八九十一二三四五六七八九十"
        }
        cmd = "withdrawal"
        request_id = str(uuid.uuid4())

        self.service.send(request_id, self.message_type, cmd, request_data)
        self.result = self.service.receive()

    def test_reset_password(self):
        """
        MT5 重置密码
        :return:
        """
        request_data = {
            "login": 40240022,
            "password": "abc123",
            "ismaster_password": 1
        }
        cmd = "reset_password"
        request_id = str(uuid.uuid4())

        self.service.send(request_id, self.message_type, cmd, request_data)
        self.result = self.service.receive()

    def test_increase_credit(self):
        """
        MT5 入信用
        :return:
        """
        request_data = {
            "login": 40240022,
            "credit": 0.01,
            "isadd_credit": 1,
            "comment": "Credit In 一二三四五六七八九十一二三四五六七八九十"
        }
        cmd = "update_credit"
        request_id = str(uuid.uuid4())

        self.service.send(request_id, self.message_type, cmd, request_data)
        self.result = self.service.receive()

    def test_reduce_credit(self):
        """
        MT5 出信用
        :return:
        """
        request_data = {
            "login": 40240022,
            "credit": 0.01,
            "isadd_credit": 0,
            "comment": "Credit Out 一二三四五六七八九十一二三四五六七八九十"
        }
        cmd = "update_credit"
        request_id = str(uuid.uuid4())

        self.service.send(request_id, self.message_type, cmd, request_data)
        self.result = self.service.receive()

    def test_get_login(self):
        """
        MT5 获取账号
        :return:
        """
        request_data = {
            "login": 40240022
        }
        cmd = "select_account"
        request_id = str(uuid.uuid4())

        self.service.send(request_id, self.message_type, cmd, request_data)
        self.result = self.service.receive()

    def test_transfer(self):
        """
        MT5 转账
        :return:
        """
        from_login = 40240022
        to_login = 40240021
        transfer_money = 0.01
        request_data = {
            "from_login": from_login,
            "to_login": to_login,
            "transfer_money": transfer_money,
            "comment": f"{from_login} transfer {to_login}"
        }
        cmd = "transfer_accounts"
        request_id = str(uuid.uuid4())

        self.service.send(request_id, self.message_type, cmd, request_data)
        self.result = self.service.receive()

    def test_get_online_account(self):
        """
        MT5 查询在线账户
        :return:
        """
        request_data = {}
        cmd = "get_online_account"
        request_id = str(uuid.uuid4())

        self.service.send(request_id, self.message_type, cmd, request_data)
        self.result = self.service.receive()

    def test_able_account(self):
        """
        MT5 启用/禁用 账户
        :return:
        """
        request_data = {
            "login": 40240022,
            "able": 1
        }
        cmd = "able_account"
        request_id = str(uuid.uuid4())

        self.service.send(request_id, self.message_type, cmd, request_data)
        self.result = self.service.receive()

    def test_get_group(self):
        """
        MT5 查询管理的组
        :return:
        """
        request_data = {}
        cmd = "get_companygroup"
        request_id = str(uuid.uuid4())

        self.service.send(request_id, self.message_type, cmd, request_data)
        self.result = self.service.receive()

    def test_check_pwd(self):
        """
        MT5 校验密码
        :return:
        """
        request_data = {
            "login": 40240022,
            "password": "abc123"
        }
        cmd = "check_pwd"
        request_id = str(uuid.uuid4())

        self.service.send(request_id, self.message_type, cmd, request_data)
        self.result = self.service.receive()

    def test_get_all_symbol(self):
        """
        MT5 查询所有品种
        :return:
        """
        request_data = {}
        cmd = "get_all_symbol"
        request_id = str(uuid.uuid4())

        self.service.send(request_id, self.message_type, cmd, request_data)
        self.result = self.service.receive()

    def test_get_group_spread(self):
        """
        MT5 查询所有品种
        :return:
        """
        request_data = {
            "group": "demo\samtest"
        }
        cmd = "get_group_spread"
        request_id = str(uuid.uuid4())

        self.service.send(request_id, self.message_type, cmd, request_data)
        self.result = self.service.receive()

    def test_multi_withdrawal(self):
        """
         MT5 批量出金
        :return:
        """
        data_list: List[Dict[Any, Union[int, float, str]]] = []
        for i in range(10):
            data_list.append(dict(audit_id=i, login=40240022, withdrawal=0.01, comment="Withdrawal Multi"))
        request_data = {
            "data_array": data_list
        }
        cmd = "multi_withdrawal"
        request_id = str(uuid.uuid4())

        self.service.send(request_id, self.message_type, cmd, request_data)
        self.result = self.service.receive()

    def test_multi_update_group(self):
        """
         MT5 批量调组
        :return:
        """
        data_list: List[Dict[Any, int]] = []
        for i in range(10):
            data_list.append(dict(login=40240022))
        request_data = {
            "group": "demo\samtest",
            "login_num": len(data_list),
            "logins": data_list
        }
        cmd = "multi_update_account_group"
        request_id = str(uuid.uuid4())

        self.service.send(request_id, self.message_type, cmd, request_data)
        self.result = self.service.receive()

    def test_get_all_login(self):
        """
        MT5 查询所有账号
        :return:
        """
        request_data = {}
        cmd = "get_all_login"
        request_id = str(uuid.uuid4())

        self.service.send(request_id, self.message_type, cmd, request_data)
        self.result = self.service.receive()

    def test_get_position(self):
        """
        MT5 查询账号的在途订单
        :return:
        """
        request_data = {
            "login": 40240022
        }
        cmd = "get_user_openorder"
        request_id = str(uuid.uuid4())

        self.service.send(request_id, self.message_type, cmd, request_data)
        self.result = self.service.receive()

    def test_get_order_count(self):
        """
        MT5 查询账号订单数
        :return:
        """
        request_data = {
            "login": 40240022
        }
        cmd = "get_user_ordercount"
        request_id = str(uuid.uuid4())

        self.service.send(request_id, self.message_type, cmd, request_data)
        self.result = self.service.receive()

    def test_check_connect(self):
        """
        MT5 检验MT连接
        :return:
        """
        request_data = {}
        cmd = "check_connect"
        request_id = str(uuid.uuid4())

        self.service.send(request_id, self.message_type, cmd, request_data)
        self.result = self.service.receive()


if __name__ == "__main__":
    unittest.main()
