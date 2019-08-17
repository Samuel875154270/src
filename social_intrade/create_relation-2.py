import config
import json
import requests

headers = config.web_headers

protocol = "http"
host = "192.168.1.203:12913"
api = "/follow/createRelationShip"

fid_file = "./info/d06f-1e8d6b745_fid.json"

with open(fid_file, "r") as file:
    fid = json.load(file)

start_login = 171001
pid = "b6be2e10-be3e"
count = 1000
error_name = "error.log"

headers["Cookie"] = "sessionID=08pY5jdaruKnITRCwPtC7J02hnYH2PvE; sessionID.sig=Gctp_XQL7E3IWoTEi4tDZ20q9J4"
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
    "follow_multiple": 1,
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
