from classes.PriceCloudService import PriceCloudService
import config

if __name__ == '__main__':
    price_cloud = config.price_cloud

    # 外网，正确密码
    extranet = price_cloud["extranet"]
    t = PriceCloudService(extranet["host"], extranet["port"], price_cloud["secret_key"])
    check = t.login(price_cloud["username"], price_cloud["password"])
    # check = t.login(price_cloud["username"], "")
    if check["code"] == 0:
        print("登录成功")
        t.get_price()
    else:
        print("登录失败")

    # # 内网，正确密码
    # intranet = price_cloud["intranet"]
    # t = TCPService(intranet["host"], intranet["port"], price_cloud["secret_key"])
    # # check = t.login(price_cloud["username"], price_cloud["password"])
    # check = t.login(price_cloud["username"], "11111111")
    # if check["code"] == 0:
    #     print("登录成功")
    #     t.get_price()
    # else:
    #     print("登录失败")
