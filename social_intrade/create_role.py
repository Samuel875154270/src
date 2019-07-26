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
role = "follow"  # publish、follow
start_login = 172501
end_login = 173001

value = []
all_login = list(range(start_login, end_login))
for login in [2089102782]:
    # for login in all_login:
    value.append({"server_id": server_id, "login": login})
params = {
    "type": role,
    "value": value
}
s = requests.session()
response = s.post(url="{}://{}{}".format(protocol, host, api), json=params, headers=headers).text

data = json.loads(response)["data"]
# 合并login与对应的id
login_id = list(map(lambda x, y: {**x, **{"login": y, "server_id": server_id}}, data, all_login))

# 判断文件名和写入文件
file_name = "pid_{}.json".format(server_id) if role == "publish" else "fid_{}.json".format(server_id)
with open(file_name, "w") as file:
    file.write(json.dumps(login_id, indent=4))
