from classes.DooCppSubService import DooCppSubService
import asyncio
import config

gateway = config.trading_system_gateway
message_type = "tradingsystem"
request_zone = "A"

host = gateway["host"]
port = gateway["port"]
server_id = gateway["server_id"]
licences = gateway["licences"]

service = DooCppSubService()
service.init(host, port)

request_data = {}
params = {
    "message_type": message_type,
    "request_zone": request_zone,
    "request_data": request_data
}

# 订阅order订单
cmd = "subsc_order_info"
service.send(cmd, server_id, licences, params, is_sub=True)
result = service.receive()
if result["response_status"] == 0 and result["response_details"] == "O.K.":
    print("订阅 {} 成功。".format(cmd), result)
    asyncio.get_event_loop().run_until_complete(service.long_receive(name=cmd))
else:
    print("订阅 {} 失败。".format(cmd), result)

# # 订阅position订单
# cmd = "subsc_position_info"
# service.send(cmd, server_id, licences, params, is_sub=True)
# result = service.receive()
# if result["response_status"] == 0 and result["response_details"] == "O.K.":
#     print("订阅 {} 成功。".format(cmd), result)
#     asyncio.get_event_loop().run_until_complete(service.long_receive(name=cmd))
# else:
#     print("订阅 {} 失败。".format(cmd), result)

# # 订阅deal订单
# cmd = "subsc_deal_info"
# service.send(cmd, server_id, licences, params, is_sub=True)
# result = service.receive()
# if result["response_status"] == 0 and result["response_details"] == "O.K.":
#     print("订阅 {} 成功。".format(cmd), result)
#     asyncio.get_event_loop().run_until_complete(service.long_receive(name=cmd))
# else:
#     print("订阅 {} 失败。".format(cmd), result)
