from config.route import route
import logging
import tornado.ioloop
import tornado.web

level = logging.INFO
logging.basicConfig(
    level=level,
    format="%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="access.log"
)
console = logging.StreamHandler()
console.setLevel(level)
formatter = logging.Formatter("%(name)-12s: %(levelname)-8s %(message)s")
console.setFormatter(formatter)
logging.getLogger("").addHandler(console)

if __name__ == "__main__":
    port = 9999
    app = tornado.web.Application(route)
    app.listen(port)
    print(f"http://127.0.0.1:{port}")
    tornado.ioloop.IOLoop.instance().start()
