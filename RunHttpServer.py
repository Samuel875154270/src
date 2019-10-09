from http.server import BaseHTTPRequestHandler
import json


class TestServer(BaseHTTPRequestHandler):

    def do_GET(self):
        path = self.path.split("?")
        if len(path) == 2:
            uri, params = path[0], path[1]
        else:
            uri, params = path[0], ""
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(
            json.dumps({"code": 0, "data": {"method": "GET", "uri": uri, "params": params}}).encode())

    def do_POST(self):
        uri = self.path
        length = int(self.headers["content-length"])
        params = self.rfile.read(length).decode()
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        self.wfile.write(
            json.dumps({"code": 0, "data": {"method": "POST", "uri": uri, "params": json.loads(params)}}).encode())
