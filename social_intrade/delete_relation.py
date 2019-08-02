import config
import json
import requests

headers = config.web_headers

protocol = "https"
host = "intrade.doo.tech"
get_api = "/follow/getRelation"
del_api = "/follow/destroyRelation"

pid = "9a5dad4e-af62"
start_page = 52
end_page = 71

headers["Cookie"] = "sessionID=bp1BHcXPH78wSE1ZlBUwd8DzSu0PUN8R; sessionID.sig=5YAPR9hPHuFmLrhUHG9SsEyS7LE"
headers["Host"] = host

get_params = {
    "pagesize": 20,
    "id": pid,
    "type": "publish",
    "history": False
}
del_params = {
    "stop_follow": "1"
}

s = requests.session()

while end_page >= start_page:
    get_params["page"] = end_page
    response = s.post(url="{}://{}{}".format(protocol, host, get_api), json=get_params, headers=headers).text
    response = json.loads(response)
    for r in response["data"]["data"]:
        rid = r["rid"]
        del_params["id"] = [rid]
        del_rp = s.post(url="{}://{}{}".format(protocol, host, del_api), json=del_params, headers=headers).text
        print(del_params, del_rp)

    end_page -= 1

print("end")
