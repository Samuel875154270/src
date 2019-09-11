from classes.DooCppSubService import DooCppSubService


class SubService(object):
    request_zone = "A"
    message_type = "tradingsystem"

    params = {
        "message_type": message_type,
        "request_zone": request_zone,
        "request_data": {}
    }

    def __init__(self, host, port, server_id, licences):
        """
        初始化
        :param host:
        :param port:
        :param server_id:
        :param licences:
        """
        self.service = DooCppSubService()
        self.service.init(host, port)

        self.server_id = server_id
        self.licences = licences

    def sub(self, cmd):
        """
        订阅订单
        :return
        """
        self.service.send(cmd, self.server_id, self.licences, self.params, is_sub=True)
        result = self.service.receive()
        if result["response_status"] == 0 and result["response_details"] == "O.K.":
            print("订阅 {} 成功。".format(cmd), result)
            # asyncio.get_event_loop().run_until_complete(service.long_receive(name=cmd))
            self.service.long_receive(name=cmd)
        else:
            print("订阅 {} 失败。".format(cmd), result)

    def sub_order(self):
        """
        订阅order订单
        :return
        """
        cmd = "subsc_order_info"
        self.service.send(cmd, self.server_id, self.licences, self.params, is_sub=True)
        result = self.service.receive()
        if result["response_status"] == 0 and result["response_details"] == "O.K.":
            print("订阅 {} 成功。".format(cmd), result)
            # asyncio.get_event_loop().run_until_complete(service.long_receive(name=cmd))
            self.service.long_receive(name=cmd)
        else:
            print("订阅 {} 失败。".format(cmd), result)

    def sub_position(self):
        """
        订阅position订单
        :return
        """
        cmd = "subsc_position_info"
        self.service.send(cmd, self.server_id, self.licences, self.params, is_sub=True)
        result = self.service.receive()
        if result["response_status"] == 0 and result["response_details"] == "O.K.":
            print("订阅 {} 成功。".format(cmd), result)
            # asyncio.get_event_loop().run_until_complete(service.long_receive(name=cmd))
            self.service.long_receive(name=cmd)
        else:
            print("订阅 {} 失败。".format(cmd), result)

    def sub_deal(self):
        """
        订阅deal订单
        :return
        """
        cmd = "subsc_deal_info"
        self.service.send(cmd, self.server_id, self.licences, self.params, is_sub=True)
        result = self.service.receive()
        if result["response_status"] == 0 and result["response_details"] == "O.K.":
            print("订阅 {} 成功。".format(cmd), result)
            # asyncio.get_event_loop().run_until_complete(service.long_receive(name=cmd))
            self.service.long_receive(name=cmd)
        else:
            print("订阅 {} 失败。".format(cmd), result)

    def sub_trade(self):
        """
        订阅MT4 trade订单
        :return
        """
        cmd = "subsc_trade_info"
        self.service.send(cmd, self.server_id, self.licences, self.params, is_sub=True)
        result = self.service.receive()
        if result["response_status"] == 0 and result["response_details"] == "O.K.":
            print("订阅 {} 成功。".format(cmd), result)
            # asyncio.get_event_loop().run_until_complete(service.long_receive(name=cmd))
            # self.service.long_receive(name=cmd, login="2089102728")
            self.service.long_receive(name=cmd, login="2089103004")
        else:
            print("订阅 {} 失败。".format(cmd), result)
