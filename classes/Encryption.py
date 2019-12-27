import base64
import datetime
import hashlib
from Crypto.Cipher import AES, DES3
from Crypto.Util.Padding import pad
from urllib.parse import urlencode


class MyEncode(object):

    def __init__(self, key, iv="IB9N75V82Q0KJ3BK"):
        """

        :param key:
        :param iv:
        """
        self.key = key.encode()
        self.iv = iv.encode()

    def aes_encode(self, string):
        """

        :param string:
        :return:
        """
        aes = AES.new(key=self.key, mode=AES.MODE_CBC, IV=self.iv)
        encode_aes = aes.encrypt(self.pad(string))
        encode_string = base64.encodebytes(encode_aes).replace(b"\n", b"").decode()
        print(encode_string)
        return encode_string.replace("+", "-").replace("/", "_")

    @staticmethod
    def pad(string):
        size = 32
        pad_string = string.encode() + b"\0" * (size - len(string) % size)
        print(len(pad_string), pad_string)
        return pad_string

    @staticmethod
    def get_md5(string):
        """

        :param string:
        :return:
        """
        m = hashlib.md5()
        m.update(string.encode())
        return m.hexdigest()


class TcEncode(object):
    """
    具有 Base 64 编码 DES3 加密算法
    电码本模式（ECB）
    pkcs7Padding 加密
    """

    def __init__(self, key="d1oo2tE#$^#$X^@$34c!8@hl"):
        """

        :param key:
        """
        self.key = key.encode()

    def des_encode(self, string):
        """

        :param string:
        :return:
        """
        des = DES3.new(key=self.key, mode=DES3.MODE_ECB)
        encode_des = des.encrypt(self._pad(string))
        en_string = base64.encodebytes(encode_des).replace(b"\n", b"").decode()
        return self._url_encode(en_string)

    @staticmethod
    def _pad(string):
        """

        :param string:
        :return:
        """
        pad_string = pad(string.encode(), DES3.block_size, "pkcs7")  # pkcs7补全
        return pad_string

    @staticmethod
    def _url_encode(string):
        """

        :param string:
        :return:
        """
        return urlencode({"tkn": string})


if __name__ == "__main__":
    time_format: str = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
    print(time_format)
    params = {
        "aci": time_format,
        "page": "featured_forex",  # economic_calendar、featured_forex、av_ideas
        "usi": "testUser",
        "lang": "en",  # en、cs、ct、ko
        "eml": "test@recognia.com",
        # "uty": "FxOnly",
        # "usg": "Demo"
    }
    init_string = ""
    for k, v in params.items():
        init_string += f"{k}={v}&"

    tc = TcEncode()
    encode_string = tc.des_encode(init_string[:-1])
    if params["page"] in ["economic_calendar", "featured_forex"]:
        url = f"https://site.recognia.com/doo/serve.shtml?{encode_string}"
    else:
        url = f"https://site.ct.recognia.com/doo/serve.shtml?{encode_string}"

    print(params["page"], ": ", url)
