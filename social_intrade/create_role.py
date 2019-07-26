import config
import json
import os
import requests
import time

headers = config.web_headers

protocol = "https"
host = "intrade.doo.tech"
api = "/follow/create"
headers["Cookie"] = "sessionID=o8giG9NLDRoecXAQd5eMWKn8AzHC6QDb; sessionID.sig=oxt-i9hVlyODn5deg5fSlV7xie0"
headers["Host"] = host
server_id = "de1e-d4f23b1ed"
role = "follow"  # publish、follow
start_login = 101001
end_login = 104500

all_login = list(range(start_login, end_login + 1))
s = requests.session()

for login in all_login:
    value = {"server_id": server_id, "login": login}
    params = {
        "type": role,
        "value": [value]
    }
    response = s.post(url="{}://{}{}".format(protocol, host, api), json=params, headers=headers).text
    data = json.loads(response)["data"]
    if role == "publish":
        value["pid"] = data[0]["pid"]
        file_name = "./info/{}_pid.json".format(server_id)
    else:
        value["fid"] = data[0]["fid"]
        file_name = "./info/{}_fid.json".format(server_id)

    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            content = file.read()
            content = [] if content == "" or content is None else json.loads(content)
    else:
        content = []

    with open(file_name, "w") as file:
        content.append(value)
        file.write(json.dumps(content, indent=4))

    print(login, response)
    # time.sleep(1)

# value = []
# all_login = list(range(start_login, end_login))
# # for login in [2089102782]:
# for login in all_login:
#     value.append({"server_id": server_id, "login": login})
# params = {
#     "type": role,
#     "value": value
# }
# s = requests.session()
# response = s.post(url="{}://{}{}".format(protocol, host, api), json=params, headers=headers).text
# print(response)
# data = json.loads(response)["data"]
# # 合并login与对应的id
# login_id = list(map(lambda x, y: {**x, **{"login": y, "server_id": server_id}}, data, all_login))
#
# # 判断文件名和写入文件
# file_name = "pid_{}.json".format(server_id) if role == "publish" else "fid_{}.json".format(server_id)
# with open(file_name, "a") as file:
#     file.write(json.dumps(login_id, indent=4))
