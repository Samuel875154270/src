from classes.DooApiService import DooApiService
import json


protocol = "http"
host = "api-hk-tx.doo.tech"
headers = {
    "Host": "appf1c8a29ea26f-crm-ad-hk-tx.dootech.io",
    "Connection": "keep-alive",
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    "Sec-Fetch-Mode": "cors",
    "Content-Type": "application/json",
    "Sec-Fetch-Site": "same-origin",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": "SessionId=U0nQDTB7pee4I3CrklD4MPa4tF82t_fm; SessionId.sig=Ani1Cm4Iwmym_nb8x7vwElLugPo"
}

create_uri = "/user/v2/user"
create_params = {
    "lastname": "test",
    "firstname": "",
    "uemail": "",
    "currency": "USD",
    "uhead": {
        "url": {
            "aws": "https://cdn-backup-2.fincdn.com/crmv4/1566289754617.png"
        }
    },
    "uphonecode": "+86",
    "uphone": "",
    "utype": "ib",
    "uroleid": "edf4-31a2d2646",
    "source_uuid": "8c12-e64f32f84",
    "password": "abc123",
    "client_source": "admin"
}
# 17700100001, 17700101001
service = DooApiService("appf1c8a29ea26f", "0mXdkBgncLF8WuS1y6lb1P0v6YDLfYnT", "{}://{}".format(protocol, host))
for i in range(17700100055, 17700101001):
    create_params["agent"] = ""
    create_params["firstname"] = "{}".format(i)
    create_params["uemail"] = "{}@test.com".format(i)
    create_params["uphone"] = "{}".format(i)
    rp_1 = service.call(create_uri, "POST", create_params)

    f_uuid = json.loads(rp_1["result"])["data"]["uuid"]
    create_params["firstname"] = "{}".format(i + 1100000000)
    create_params["uemail"] = "{}@test.com".format(i + 1100000000)
    create_params["uphone"] = "{}".format(i + 1100000000)
    create_params["agent"] = "{}".format(f_uuid)
    rp_2 = service.call(create_uri, "POST", create_params)

    s_uuid = json.loads(rp_2["result"])["data"]["uuid"]
    create_params["firstname"] = "{}".format(i + 1100000000 * 2)
    create_params["uemail"] = "{}@test.com".format(i + 1100000000 * 2)
    create_params["uphone"] = "{}".format(i + 1100000000 * 2)
    create_params["agent"] = "{}".format(s_uuid)
    rp_3 = service.call(create_uri, "POST", create_params)

    print(i, rp_1, rp_2, rp_3)
