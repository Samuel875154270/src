from cpp_service.CppServiceHandler import CppServiceHandler
import config

gateway = config.gateway["crm_gateway"]
server_id = gateway["server_id"]
licences = gateway["licences"]

service = CppServiceHandler()

service.init(host=gateway["host"], port=gateway["port"], message_type="CRM")


cmd = "new_account"
params = {
    "group": "SOCIAL-008",
    "password": "abc123",
    "investor_password": "abc124",
    "phone_password": "abc125",
    "leverage": 500,
    "id_number": "abc-111",
    "phone": "12345678910",
    "status": "en",
    "country": "China",
    "state": "Guangdong",
    "city": "Shenzhen",
    "zip_code": "518000",
    "address": "address",
    "agent_account": 0,
    "read_only": 0,
    "enable_change_password": 1,
    "enable": 1,
    "lead_source": "test",
    "comment": "test",
    "default_deposit": 50000
}

start_login = 172501
end_login = 173001

for login in range(start_login, end_login):
    params["login"] = login
    params["name"] = "Follower {}".format(login)
    params["email"] = "test{}@follower.com".format(login)
    # print(params)
    result = service.call(server_id, licences, cmd, params)
    print(result)
