import certifi
import config
from elasticsearch import Elasticsearch
from elasticsearch import helpers


class ES(object):
    es = None

    def __init__(self):
        """
        ElasticSearch连接
        """
        address = ("http://{}:{}@{}:{}".format(config.elastic["user"], config.elastic["pass"], config.elastic["host"],
                                               config.elastic["port"]))
        is_https = config.elastic["method"] == "https"
        self.es = Elasticsearch(hosts=address, retry_on_timeout=True, maxsize=500, timeout=50, use_ssl=is_https,
                                verify_certs=True, ca_certs=certifi.where())

    def get(self, index, doc_type, body, params=None, scroll=None):
        """
        请求es查询
        :param index:
        :param doc_type:
        :param body:
        :param params:
        :param scroll:
        :return:
        """
        params = {} if params is None else params
        result = self.es.search(index=index, doc_type=doc_type, body=body, params=params, scroll=scroll)
        return result

    def scroll(self, scroll_id, scroll="5m"):
        result = self.es.scroll(
            scroll_id=scroll_id,
            scroll=scroll
        )
        return result

    def scan(self, index, doc_type, query=None,  scroll="5m", size=1000, request_timeout=None, clear_scroll=True):
        """

        :param index:
        :param doc_type:
        :param query:
        :param scroll:
        :param size:
        :param request_timeout:
        :param clear_scroll:
        :return:
        """
        result = helpers.scan(
            client=self.es,
            index=index,
            doc_type=doc_type,
            query=query,
            scroll=scroll,
            size=size,
            request_timeout=request_timeout,
            clear_scroll=clear_scroll,
        )

        return result
