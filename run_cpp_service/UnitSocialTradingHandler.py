from classes.DooCppService import DooCppService


class UnitSocialTradingHandler(object):
    client = False
    message_type = "tradingsystem"
    request_zone = "A"

    def init(self, host, port):
        """
        初始化TCP连接
        :param host:
        :param port:
        """
        self.client = DooCppService()
        self.client.init(host, port)

    def close(self):
        """
        断开TCP连接
        :return:
        """
        self.client.tcp_close()

    def call(self, server_id, licences, cmd, params=None, is_sub=False):
        """
        请求tcp接口
        :param: server_id
        :param: licences
        :param: cmd
        :param: params
        :param: is_sub
        :return:
        """
        print(is_sub)
        if params is None:
            params = {}

        request_data = {
            "message_type": self.message_type,
            "request_zone": self.request_zone,
            "request_data": params
        }

        self.client.send(cmd, server_id, licences, request_data, is_sub)

        return self.client.receive()
