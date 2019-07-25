import config
import json
import requests

headers = config.web_headers

protocol = "http"
host = "192.168.1.203:12913"
api = "/follow/create"
headers["Cookie"] = "sessionID=ElmQNY3dQQpF4LiwhLBWqLkbsGWcQUFZ; sessionID.sig=fFTTCTSlmQN2nQ_i6u-mp_hlwJ0"
headers["Host"] = host
server_id = "69b0-69167ae4a"
role = "publish"    # publish、follow
start_login = 172501
end_login = 173001

value = []
all_login = list(range(start_login, end_login))
# for login in [2089102783, 2089102792, 2089102793, 2089102795, 2089102796]:
for login in all_login:
    value.append({"server_id": server_id, "login": login})
params = {
    "type": role,
    "value": value
}
s = requests.session()
response = s.post(url="{}://{}{}".format(protocol, host, api), json=params, headers=headers).text
print(response)

response = json.loads(response)
# 合并login与对应的id
if role == "publish":
    data = response["pid"]
    pid_login = list(map(lambda x, y: {**x, **{"login": y, "server_id": server_id}}, data, all_login))
    with open("pid_{}.json".format(server_id), "a") as file:
        file.write(json.dumps(pid_login, indent=4))
else:
    data = response["fid"]
    fid_login = list(map(lambda x, y: {**x, **{"login": y, "server_id": server_id}}, data, all_login))
    with open("fid_{}.json".format(server_id), "a") as file:
        file.write(json.dumps(fid_login, indent=4))
