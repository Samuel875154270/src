import config
import json
import hashlib
import redis
import time
import uuid
import tornado.log


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


def is_dict(value):
    """
    判断字符串是否为dict格式
    :param value:
    :return:
    """
    try:
        json.loads(value)
        return True
    except TypeError:
        return False


def is_json(value):
    """
    判断字符串是否为json格式
    :param value:
    :return:
    """
    try:
        json.dumps(value)
        return True
    except TypeError:
        return False


def log_request(handler):
    if handler.get_status() < 400:
        log_method = tornado.log.access_log.info
    elif handler.get_status() < 500:
        log_method = tornado.log.access_log.warning
    else:
        log_method = tornado.log.access_log.error

    request_time = 1000.0 * handler.request.request_time()
    log_method("%d %s %.2fms %s", handler.get_status(), handler._request_summary(), request_time,
               handler.request.headers.get("User-Agent", ""))
