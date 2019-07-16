from run_cpp_service.SubService import SubService
import config

if __name__ == "__main__":
    gateway = config.trading_system_gateway
    host = gateway["host"]
    port = gateway["port"]
    server_id = gateway["server_id"]
    licences = gateway["licences"]

    service = SubService(host, port, server_id, licences)
    """订阅position"""
    service.sub_position()

