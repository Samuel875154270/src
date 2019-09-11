import config
import json
import requests

headers = config.web_headers

protocol = "http"
host = "192.168.1.203:12913"
api = "/follow/createRelationShip"

fid_file = "./info/0f4d-93a3094ed_fid.json"

with open(fid_file, "r") as file:
    fid = json.load(file)

start_login = 101001
pid = "d614ee14-cacf"
count = 1000
error_name = "error.log"

headers["Cookie"] = "sessionID=QtunJk8Qrt5QV6XJBmp5HgCm8vcaJXGe; sessionID.sig=Af_DKHnYFMC6P3fEj6w1wLtPZz4"
headers["Host"] = host

params = {
    "pid": pid,
    "fid": "",
    "disabled": False,
    "package_name": "策略名称-",
    "comment_mode": 0,
    "position_volume_limit": 20,
    "follow_direction": "positive",
    "follow_symbols": config.symbols,
    "follow_multiple_type": "fixed",
    "follow_multiple": 0.01,
    "order_loss_point": 0,
    "order_profit_point": 0,
    "follow_type": "all",
    "follow_volume_max": 1
}
s = requests.session()
for f in fid:
    params["fid"] = f["fid"]
    params["package_name"] = "策略-{}".format(f["login"])
    response = s.post(url="{}://{}{}".format(protocol, host, api), json=params, headers=headers).text
    print(f["login"], f["fid"], response, pid)
    if '{"code":0' not in response:
        with open(error_name, "a") as file:
            file.write("{}\t{}\t{}\t{}\n".format(f["login"], f["fid"], response, pid))

    if f["login"] == start_login + count - 1:
        break

with open(error_name, "a") as file:
    file.write("=" * 50)
    file.write("\n")

print("end")
