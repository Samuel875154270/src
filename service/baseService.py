from concurrent.futures import ThreadPoolExecutor


class Executor(ThreadPoolExecutor):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not getattr(cls, "_instance", None):
            cls._instance = ThreadPoolExecutor(max_workers=10)

        return cls._instance
