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
    for i in range(3):
        if i == 0:
            th = threading.Thread(target=service.sub_order, args=())
            # service.sub_order()
        elif i == 1:
            th = threading.Thread(target=service.sub_position, args=())
            # service.sub_position()
        else:
            th = threading.Thread(target=service.sub_deal, args=())
            # service.sub_deal()
        th.start()
        threads.append(th)
