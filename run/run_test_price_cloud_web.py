from classes.PriceCloudService import WebPriceCloudService
import config
import json

if __name__ == '__main__':
    price_cloud = config.web_price_cloud
    host = price_cloud["intranet"]["host"]
    port = price_cloud["intranet"]["port"]
    username = price_cloud["username"]
    password = price_cloud["password"]

    service = WebPriceCloudService(host, port, (username, password))

    # while True:
    #     price = service.get_market({"symbol": "AUDCAD-Sam.g"})
    #     # print(price)
    #     print(price.get("data"))
    #     # time.sleep(5)

    params = {
        "symbol": "XAUUSD",
        "period": "30",
        "from": 1571011200,
        # "to": 1570727700 + 300,
        # "from": 1570795200,
        # "to": 1570694400 + 60 * 60 * 17,
        "limit": "1000",
    }
    result = service.get_kline(params)
    print(result)

    if result != "":
        result = json.loads(result)
        if result["code"] == 0:
            data = result["data"]
            print(len(data))
            for l in range(len(data)):
                if l < len(data) - 1:
                    print(data[l]["time"], data[l + 1]["time"], data[l]["time"] - data[l + 1]["time"])
                else:
                    print(data[l]["time"])

