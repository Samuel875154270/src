from pymongo import MongoClient


class Mongodb(object):
    client = False
    db = False

    def __init__(self, host, port, user, password, database, is_live=False):
        """
        初始化mongodb链接
        :param host:
        :param port:
        :param user:
        :param password:
        :param database:
        :param is_live:
        :return:
        """
        if is_live is True:
            self.client = MongoClient(host=host, port=port, connect=False)
            self.db = self.client.get_database(database)
            self.db.authenticate(user, password)

        else:
            self.client = MongoClient(
                f"mongodb://{user}:{password}@{host}:{port}/"
            )
            self.db = self.client[database]

    def get(self, collection_name, query, limit):
        """
        根据条件查询
        :param collection_name:
        :param query:
        :param limit:
        :return:
        """
        collection = self.db[collection_name]
        result = collection.find(query).limit()

        return list(result)
