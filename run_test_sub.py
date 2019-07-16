from cpp_service.SubService import SubService
import config
import threading

if __name__ == "__main__":
    gateway = config.trading_system_gateway
    host = gateway["host"]
    port = gateway["port"]
    server_id = gateway["server_id"]
    licences = gateway["licences"]

    service = SubService(host, port, server_id, licences)

    threads = []
    for s in ["subsc_order_info", "subsc_position_info", "subsc_deal_info"]:
        if s == "subsc_order_info":
            th = threading.Thread(target=service.sub, args=(s,))
            # service.sub_order()
        elif s == "subsc_position_info":
            th = threading.Thread(target=service.sub, args=(s,))
            # service.sub_position()
        else:
            th = threading.Thread(target=service.sub, args=(s,))
            # service.sub_deal()
        th.start()
        threads.append(th)
