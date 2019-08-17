import gevent
import geventlet
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
    "Cookie": "SID=h3L02lOPHbbJ566a3_q6qh0v_LqoT90BegeAYkqkwMZoNA86nCrq2ApSMJTo0hCC"
}


def call(i):
    try:
        rp = requests.get(url, headers=headers, timeout=30).text
        rp = json.loads(rp)
        print(i, time.time(), rp["chart_total"])

    except Exception as e:
        print(i, e)


if __name__ == "__main__":
    count = 50
    g = []
    t1 = time.time()
    for r in range(count):
        g.append(gevent.spawn(call, r))

    gevent.joinall(g)
    print("总用时", time.time() - t1)
