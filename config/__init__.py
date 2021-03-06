import os

# MySQL
mysql = {
    "db": os.getenv("DB_NAME", "doo_platform_api"),
    "host": os.getenv("DB_HOST", "192.168.1.205"),
    "user": os.getenv("DB_USER", "root"),
    "passwd": os.getenv("DB_PASSWORD", "1UP3UoS8xMebsMqMggH2"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "charset": os.getenv("DB_CHARSET", "utf8")
}

"""MT gateway配置"""
gateway = {
    "social_gateway": {
        "host": "192.168.1.228",
        "port": 9400,
        # 公有
        "server_id": "d06f-1e8d6b745",  # test2
        "licences": "e656b991-5706-4cb1-af8f-f69323f8f7e4",
        # "server_id": "0f4d-93a3094ed",  # test1
        # "licences": "1f5f0007-75d3-4f8b-b1b8-2d63e8747eed",
        # "server_id": "42ec-d1106b09e",  # mt5
        # "licences": "756de4c5-2ed6-42eb-9217-3d4f9675d8f6",
    },
    "trading_system_gateway": {
        "host": "192.168.1.228",
        "port": 9600,
        # MT5
        # "server_id": "d0a9-838c7e7f4",
        # "licences": "5fc1873d-a582-44c4-9235-b4d57c7cbe96",
        # MT4
        # "server_id": "975a-5f27ba02d",
        # "licences": "4470ca70-f098-4320-9cb0-21717e65e77f",
        "server_id": "d06f-1e8d6b745",  # test2
        "licences": "e656b991-5706-4cb1-af8f-f69323f8f7e4",
    },
    "manager_check_gateway": {
        "host": "192.168.1.228",
        "port": 10000,
        "server_id": "",
        "licences": ""
    },
    "crm_gateway": {
        "host": "192.168.1.228",
        "port": 9500,
        # "server_id": "69b0-69167ae4a",
        # "licences": "91c60c06-09e6-47c8-8c2c-3b78af7f12f7",
        # "server_id": "2f3d-bef737348",
        # "licences": "31f3b906-35ac-4eca-b450-bcaaa69477f7",
        "server_id": "42ec-d1106b09e",  # mt5
        "licences": "756de4c5-2ed6-42eb-9217-3d4f9675d8f6",
    }
}

"""price_cloud配置"""
price_cloud = {
    "intranet": {
        # 内网（未开启代理协议）
        # "host": "192.168.1.203",
        # "port": 12960,
        # 内网（已开启代理协议，仅允许白名单IP）
        "host": "192.168.1.203",
        "port": 13001
    },
    "extranet": {
        # 公网（未开启代理协议）
        "host": "songmaokeji.f3322.net",
        "port": 12960,
        # """公网（已开启代理协议，仅允许白名单IP）"""
        # "host": "songmaokeji.f3322.net",
        # "port": 13001,
    },
    "secret_key": "htrh6)(4j5345#jkld",
    "username": "client",
    "password": "1MmH0AfGWnzd"
}

web_price_cloud = {
    "intranet": {
        # 内网
        "host": "192.168.1.203",
        "port": "12958"
    },
    "extranet": {
        # 公网
        "host": "songmaokeji.f3322.net",
        "port": "12958"

    },
    "username": "client",
    "password": "1MmH0AfGWnzd",
}

web_headers = {
    "Host": "",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": ""
}

# redis
redis = {
    "host": "127.0.0.1",
    "port": 6379,
    "auth": "",
    "password": "",
    "expire": 60
}

# elastic search 配置文件
elastic = {
    'host': os.getenv('ES_HOST', '192.168.30.10'),
    'port': os.getenv('ES_PORT', 32000),
    'user': os.getenv('ES_USER', 'dootech'),
    'pass': os.getenv('ES_PASS', ''),
    'method': os.getenv('ES_METHOD', 'http')
}

# mongodb 配置文件
mongodb = {
    # 测试环境
    # "host": "192.168.30.159",
    # "port": 27017,
    # "user": "price-user",
    # "password": "dfA4FxnCgw0XIxqoHL",
    # "db": "price-cloud",
    # 预发布环境
    # "host": "192.168.30.155",
    # "port": 27017,
    # "user": "dootech",
    # "password": "TLcyNHG6NP03jaDObqUnMFESebjnfu",
    # "db": "admin",
    # 生产环境
    "host": "47.244.48.58",
    "port": 27017,
    "user": "r_price",
    "password": "Bka2qvMjC8l1IVNDxY9cESbw3",
    "db": "price_cloud",
}

symbols = [
    "AUDUSD",
    "EURUSD",
    "GBPUSD",
    "NZDUSD",
    "USDCAD",
    "USDCHF",
    "USDCNH",
    "USDHKD",
    "USDJPY",
    "USDNOK",
    "USDPLN",
    "USDSEK",
    "USDSGD",
    "USDTRY",
    "USDZAR",
    "AUDCAD",
    "AUDCHF",
    "AUDJPY",
    "AUDNZD",
    "CADCHF",
    "CADJPY",
    "CHFJPY",
    "EURAUD",
    "EURCAD",
    "EURCHF",
    "EURGBP",
    "EURJPY",
    "EURNZD",
    "GBPAUD",
    "GBPCAD",
    "GBPCHF",
    "GBPJPY",
    "GBPNZD",
    "NZDCAD",
    "NZDCHF",
    "NZDJPY",
    "XAUUSD",
    "XAGUSD",
    "CL",
    "COIL",
    "XBRUSD",
    "XNGUSD",
    "XTIUSD",
    "AUS200",
    "EU50",
    "FRA40",
    "GER30",
    "HK50",
    "NAS100",
    "JPN225",
    "US30",
    "SP500",
    "UK100",
    "FGC",
    "FBTC",
    "FHSI",
    "FMHI",
    "FCNA50",
    "FN225M",
    "FN225",
    "FDAX",
    "FNQ",
    "FSP",
    "FYM",
    "ETHUSD",
    "XRPUSD",
    "LTCUSD",
    "BTCUSD",
    "FIF300",
    "BCHUSD",
    "ES"
]
