from service import *
from classes.Es import ES
import common
import json
import tornado.gen
import tornado.web


class EsHanlders(tornado.web.RequestHandler):
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

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        body = self.request.body.decode()
        if common.is_json(body):
            body = json.loads(body)
            index = body["index"]
            doc = body["doc"]
            es_body = body["body"]

            if index and doc and es_body:
                result = self.es.get(index, doc, es_body)
                self.finish({
                    "code": 0,
                    "info": result
                })
            else:
                self.finish({
                    "code": -2,
                    "info": "index, doc, body must be not empty"
                })
        else:
            self.finish({
                "code": -1,
                "info": "the data in body is not a json"
            })
