import config
import json
import requests

headers = config.web_headers

protocol = "https"
host = "intrade.doo.tech"
api = "/follow/createRelationShip"


# pid_file = "./info/191f-205a88b45_pid.json"
pid_file = "./info/de1e-d4f23b1ed_pid.json"
with open(pid_file, "r") as file:
    pid = json.load(file)

start_login = 100001
fid = "00a895a0-af5e"
count = 50

headers["Cookie"] = "sessionID=o8giG9NLDRoecXAQd5eMWKn8AzHC6QDb; sessionID.sig=oxt-i9hVlyODn5deg5fSlV7xie0"
headers["Host"] = host

params = {
    "pid": "",
    "fid": fid,
    "disabled": False,
    "package_name": "From-",
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
for p in pid:
    params["pid"] = p["pid"]
    params["package_name"] = "From-{}".format(p["login"])
    response = s.post(url="{}://{}{}".format(protocol, host, api), json=params, headers=headers).text
    print(p["login"], p["pid"], response, fid)
    if '{"code":0' not in response:
        with open("error.log", "a") as file:
            file.write("{}\t{}\t{}\t{}\n".format(p["login"], p["pid"], response, fid))

    if p["login"] == start_login + count - 1:
        break

with open("error.log", "a") as file:
    file.write("=" * 50)
    file.write("\n")

print("end")
