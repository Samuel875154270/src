from classes.LocalCpp import Service
import threading
import uuid


def run(r_id, r_type, r_cmd, r_data):
    """

    :param r_id:
    :param r_type:
    :param r_cmd:
    :param r_data:
    :return:
    """
    service = Service()

    service.send(r_id, r_type, r_cmd, r_data)
    result = service.receive()
    print(result)


if __name__ == "__main__":
    message_type = "CRM"
    request_data = {
        "login": 2089102539
    }
    cmd = "select_account"
    threads = []
    for i in range(1):
        request_id = str(uuid.uuid4())
        thread = threading.Thread(target=run, args=(request_id, message_type, cmd, request_data))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
