from service import *
from classes.Es import ES
from .BaseHandler import BaseHandler
import common
import json
import tornado.gen
import tornado.web


class EsHanlders(BaseHandler):
    es = ES()
    executor = Executor()
    service = ExecutorRequest()

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        self.echo_json(0, f"{self.request.uri}")

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        try:
            body = self.request.body.decode()
            if common.is_dict(body):
                body = json.loads(body)
                index = body["index"]
                doc = body["doc"]
                es_body = body["body"]
                if index and doc and es_body:
                    # result = self.es.get(index, doc, es_body)
                    result = None
                    self.echo_json(0, result)

                else:
                    self.echo_json(-2, "index, doc, body must be not empty")
            else:
                self.echo_json(-1, "the data in body is not a json")

        except Exception as e:
            self.echo_json(-1000, f"An exception has occurred, exception is: {e}")
