import threading
import json
import requests
import time

url = "http://192.168.1.203:12956/chart/v1/bars?symbol=USDJPY&resolution=M&from=547356867&to=1563420927"
headers = {
    "Host": "192.168.1.203:12956",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "Accept": "*/*",
    "Referer": "http://192.168.1.203:12956/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": "SID=4JQDruGqOoR5WfYvOOeuS6a86T46QC7UiaU7CFwpMhTIqpv1KwkZIPGyDoM7JWgK"
}


def call(i):
    try:
        t1 = time.time()
        rp = requests.get(url, headers=headers).text
        print(i, time.time() - t1, rp)
        # rp = json.loads(rp)
        # print(i, time.time(), rp["chart_total"])

    except Exception as e:
        print(i, e)


if __name__ == "__main__":
    count = 10
    threads = []
    t1 = time.time()
    for r in range(count):
        th = threading.Thread(target=call, args=(r,))
        th.start()
        threads.append(th)

    for t in threads:
        t.join()

    # print(time.time() - t1)
