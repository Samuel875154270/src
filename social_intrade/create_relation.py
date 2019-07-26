import config
import json
import requests

headers = config.web_headers

protocol = "http"
host = "192.168.1.203:12913"
api = "/follow/createRelationShip"

with open("", "r") as file:
    fid = json.load(file)

pid = ""

headers["Cookie"] = "sessionID=ElmQNY3dQQpF4LiwhLBWqLkbsGWcQUFZ; sessionID.sig=fFTTCTSlmQN2nQ_i6u-mp_hlwJ0"
headers["Host"] = host
start_login = 172501
end_login = 173001

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
    params["fid"] = f
    params["package_name"] = "策略名称-{}".format(f)
    response = s.post(url="{}://{}{}".format(protocol, host, api), json=params, headers=headers).text
    print(response)
