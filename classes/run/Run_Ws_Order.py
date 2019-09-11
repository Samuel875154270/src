import asyncio
from classes.InTraderWsApi import InTraderWsService

api_host = "192.168.1.203:12972"
api_login_uri = "/v1/user/auth/signIn"
api_login_params = {"uemail": "sam.li@doohui.com", "password": "abc123"}

service = InTraderWsService(api_host)
service.init(api_login_uri, api_login_params)

# /v1/ws/order，Websocket连接获取订单推送
asyncio.get_event_loop().run_until_complete(service.ws_call("/v1/ws/order"))
asyncio.get_event_loop().run_forever()
