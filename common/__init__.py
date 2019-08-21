import config
import hashlib
import redis
import time
import uuid


def get_md5(string):
    """
    对字符串进行md5加密
    :param string:
    :return:
    """
    obj = hashlib.md5()
    obj.update(string.encode())
    return obj.hexdigest()


def get_timestamp():
    """
    获取时间戳
    :return:
    """
    return int(time.time())


def get_uuid():
    """
    获取uuid
    :return:
    """
    return uuid.uuid4().__str__()


def get_redis():
    """
    获取Redis连接
    :return:redis.Redis
    """
    pool = redis.ConnectionPool(host=config.redis["host"], port=config.redis["port"])
    rs = redis.StrictRedis(connection_pool=pool)
    return rs
