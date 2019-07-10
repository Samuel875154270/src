import hashlib
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
