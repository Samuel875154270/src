from http.server import HTTPServer
from RunHttpServer import TestServer


def run(host: tuple):
    server = HTTPServer(host, TestServer)
    server.serve_forever()


if __name__ == "__main__":
    host = ("127.0.0.1", 8090)
    print("Starting server, listen at: %s:%s" % host)
    run(host)
