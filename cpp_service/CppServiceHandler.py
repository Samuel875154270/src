from classes.DooCppService import DooCppService


class CppServiceHandler(object):
    client = False
    message_type = None
    request_zone = "A"

    def init(self, host, port, message_type):
        """
        初始化TCP连接
        :param host:
        :param port:
        :param message_type:
        """
        self.message_type = message_type
        self.client = DooCppService()
        self.client.init(host, port)

    def close(self):
        """
        断开TCP连接
        :return:
        """
        self.client.tcp_close()

    def call(self, server_id, licences, cmd, params=None, i=0):
        """
        请求tcp接口
        :param: server_id
        :param: licences
        :param: cmd
        :param: params
        :param: i
        :return:
        """
        if params is None:
            params = {}

        request_data = {
            "message_type": self.message_type,
            "request_zone": self.request_zone,
            "request_data": params
        }
        self.client.send(cmd, server_id, licences, request_data, count=i)

    def get(self, count=1):
        """
        获取结果
        :return:
        """
        return self.client.receive(count)
