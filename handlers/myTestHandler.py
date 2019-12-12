from handlers import *
from service.myTestService import *


class MyTestHandler(BaseHandler):
    executor = ThreadPoolExecutor()
    service = MyTestService()

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        yield self.service.get_service(10)
        self.echo_json(
            code=0,
            data={
                "method": self.request.method,
                "uri": self.request.uri,
                "params": self.arguments,
            }
        )

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        yield self.service.post_service(0)
        self.echo_json(
            code=0,
            data={
                "method": self.request.method,
                "uri": self.request.uri,
                "params": self.arguments,
            }
        )
