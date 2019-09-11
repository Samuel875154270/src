import config
import json
import os
import requests
import time

headers = config.web_headers

protocol = "http"
host = "192.168.1.203:12913"
headers["Cookie"] = "sessionID=QtunJk8Qrt5QV6XJBmp5HgCm8vcaJXGe; sessionID.sig=Af_DKHnYFMC6P3fEj6w1wLtPZz4"
server_id = "0f4d-93a3094ed"
role = "follow"  # publish、follow
start_login = 101001
end_login = 102001

api = "/follow/create"
headers["Host"] = host

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
