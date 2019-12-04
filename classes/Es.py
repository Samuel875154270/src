import certifi
import config
from elasticsearch import Elasticsearch


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
