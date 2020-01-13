import config
from playhouse.pool import PooledMySQLDatabase

# 使用连接池
database = PooledMySQLDatabase(
    database=config.mysql["db"],
    max_connections=300,
    **{
        "host": config.mysql["host"],
        "user": config.mysql["user"],
        "passwd": config.mysql["passwd"],
        "port": int(config.mysql["port"]),
        "charset": config.mysql["charset"]
    }
)

__all__ = ["database"]
