from classes.PriceCloudService import WebPriceCloudService
import config
import time

if __name__ == '__main__':
    price_cloud = config.web_price_cloud
    host = price_cloud["intranet"]["host"]
    port = price_cloud["intranet"]["port"]
    username = price_cloud["username"]
    password = price_cloud["password"]

    service = WebPriceCloudService(host, port, (username, password))

    while True:
        price = service.get_market({"symbol": "AUDCAD-Sam.g"})
        # print(price)
        print(price.get("data"))
        time.sleep(5)
