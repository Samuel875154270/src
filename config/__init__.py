"""MT gateway配置"""
gateway = {
    "social_gateway": {
        "host": "192.168.1.228",
        "port": 9400,
        # 公有
        "server_id": "d06f-1e8d6b745",
        "licences": "e656b991-5706-4cb1-af8f-f69323f8f7e4",
    },
    "trading_system_gateway": {
        "host": "192.168.1.228",
        "port": 9600,
        "server_id": "d0a9-838c7e7f4",
        "licences": "5fc1873d-a582-44c4-9235-b4d57c7cbe96"
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
        "server_id": "69b0-69167ae4a",
        "licences": "91c60c06-09e6-47c8-8c2c-3b78af7f12f7"
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
        # "host": "songmaokeji.f3322.net",
        # "port": 12960,
        # """公网（已开启代理协议，仅允许白名单IP）"""
        "host": "songmaokeji.f3322.net",
        "port": 13001,
    },
    "secret_key": "htrh6)(4j5345#jkld",
    "username": "client",
    "password": "1MmH0AfGWnzd"
}
