import tornado.web
import json
import logging
import common


class BaseHandler(tornado.web.RequestHandler):
    DooSecure = None
    arguments = {}
    result = None

    def prepare(self):
        """
        框架构造方法
        :return:
        """
        pass

    def on_finish(self):
        """
        框架析构方法
        :return:
        """
        result = json.dumps(self.result) if common.is_json(self.result) else self.result
        logging.info(
            f"method: {self.request.method}, "
            f"uri: {self.request.uri}, "
            # f"headers: {json.dumps(dict(self.request.headers))}, "
            f"params: {json.dumps(self.arguments)}, "
            f"remote_ip: {self.request.remote_ip}, "
            f"response: {result}"
        )

    def initialize(self):
        """
        重写框架方法
        :return:
        """
        # 这里必须初始化为空，避免连接缓存
        self.arguments = {}
        if "Content-Type" in self.request.headers.keys() and "multipart/form-data" in self.request.headers[
            "Content-Type"].lower():
            # 非json数据
            for key in self.request.arguments.keys():
                self.arguments[key] = self.request.arguments[key][0].decode()
            # 判断是否有上传文件
            if self.request.files.get("file"):
                self.arguments["file"] = self.request.files.get("file")[0]
        else:
            # 在body中的json数据
            request_json = self.request.body.decode("utf-8")
            request_dict = {}
            if request_json is not None and request_json is not "":
                request_dict = json.loads(request_json)
            # 获取在请求url中的数据
            for key in self.request.arguments.keys():
                self.arguments[key] = bytes.decode(self.request.arguments[key][0])

            # 结合两者数据，在url中的数据优先级高
            for key in request_dict.keys():
                if self.arguments.get(key) is None:
                    self.arguments[key] = request_dict[key]

    def set_default_headers(self):
        """
        设置header，解决跨域问题
        :return:
        """
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with,authorization")
        self.set_header("Access-Control-Allow-Methods", "POST, PUT, PATCH, DELETE, GET, OPTIONS")

    def echo_json(self, code, data, total_count=None):
        """
        输出json内容
        :param code:
        :param data:
        :param total_count:
        :return:
        """
        self.result = {
            "code": code,
            "data": {
                "data": data
            }
        }
        if total_count is not None:
            self.result["data"]["total_count"] = total_count

        self.set_header("Content-Type", "application/json")
        self.finish(json.dumps(self.result))

    def echo_success(self):
        """
        响应成功
        :return:
        """
        self.echo_json(code=0, data="Success")

    def echo_fail(self):
        """
        响应失败
        :return:
        """
        self.echo_json(code=-1, data="Fail")
