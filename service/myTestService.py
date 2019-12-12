from service import *
import time


class MyTestService(object):
    executor = Executor()

    @tornado.concurrent.run_on_executor
    def get_service(self, seconds=10):
        time.sleep(seconds)

    @tornado.concurrent.run_on_executor
    def post_service(self, seconds=10):
        time.sleep(seconds)
