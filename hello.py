# import socket
#
# host, port = '127.0.0.1', 10011
# try:
#     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client.connect((host, port))  # 连接地址和端口
#     # req = b'GET / HTTP/1.1\r\nHost:www.baidu.com\r\nConnection:keep-alive\r\n\r\n'
#     req = b'POST /v1/login HTTP/1.1\r\n' \
#           b'Host: 127.0.0.1:10011\r\n' \
#           b'Accept: application/json\r\n' \
#           b'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36\r\n' \
#           b'Content-Type: application/json\r\n' \
#           b'\r\n' \
#           b'uemail=sam.lee@doo.hk&password=abc123'
#           # b'{"uemail":"sam.lee@doo.hk","password":"abc123"}'
#     print(req.decode())
#     client.send(req)
#     print("=============")
#     print(client.recv(1024).decode())
# except Exception as e:
#     print(e)


# import requests
#
# host = "192.168.1.203:1888"
# uri = "/rebate/v1/database_historys"
# headers = {
#     "X-Auth-Appid": "appcc6113a06601"
# }
# params = {
#     "server_id": "69b0-69167ae4a",
#     "status": "pass",
#     "start_time": "2018-01-01",
#     "end_time": "2029-01-01",
#     "ticket": "13115006",
#     "trade_symbol": "USDCAD",
#     "login": 2089102868,
#     "agent": "M9546869",
#     "serial": "RB0805110831131150061",
#     "operator": "14f6-6eef6c191",
#     "page": 1,
#     "pagesize": 3
# }
# s = requests.session()
# rp = s.get("http://" + host + uri, params=params, headers=headers).text
# print(rp)
