from classes.DooMongodb import Mongodb
import config
import csv
import time

cfg = config.mongodb
client = Mongodb(cfg["host"], cfg["port"], cfg["user"], cfg["password"], cfg["db"])


def get_timestamp(time_str=None):
    """
    根据实际跟随获取对于的时间戳
    :param time_str:
    :return:
    """
    if time_str is None:
        return time.time().__int__()
    else:
        return time.mktime(time.strptime(time_str, "%Y-%m-%d %H:%M:%S")).__int__()


def get_time_str(timestamp):
    """
    获取实际时间
    :param timestamp:
    :return:
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))


def get_k(symbol_id, source, period, start, end):
    """
    获取某报价源下某品种在一段时间内的某种类型的K线
    :param symbol_id:
    :param source:
    :param period:
    :param start:
    :param end:
    :return:
    """
    collection_name = f"kline_{symbol_id}_2019"
    period_dict = {"1": 60, "5": 300, "15": 900, "30": "1800", "60": 3600, "240": 14400, "D": 86400, "W": 604800,
                   "M": ""}

    query = {
        "$and": [
            {"source": source},
            {"symbol_id": symbol_id},
            {"period": period},
            {"time": {"$gte": start, "$lt": end}}
        ]
    }
    data = list(client.db[collection_name].find(query).sort("time", -1))
    count = len(data)
    print(f"K线类型：{period}，在{start} ~ {end}内，存在K线总数为：{count}")

    k = [(data[l + 1]["time"], data[l]["time"], data[l]["time"] - data[l + 1]["time"]) for l in range(count - 1)]

    except_k = list(filter(lambda item: item[2] != period_dict[period], k))
    correct_k = list(filter(lambda item: item[2] == period_dict[period], k))

    # print("异常K线为：")
    # [print(e, get_time_str(e[0]), get_time_str(e[1])) for e in except_k]

    # print("正常K线为：")
    # [print(c) for c in correct_k]

    print("全部K线为：")
    [print(i) for i in k]


def get_init_price(symbol_id, source, start, end, date=None):
    if date is None:
        date = time.strftime("%Y%m%d", time.localtime(time.time()))

    collection_name = f"market_{date}"
    query = {
        "$and": [
            {"source": source},
            {"symbol_id": symbol_id},
            {"time": {"$gte": start, "$lt": end}}
        ]
    }
    print(query)
    data = list(client.db[collection_name].find(query).sort("time", 1))
    count = len(data)
    print(f"日期：{date}，在{start} ~ {end}内，存在K线总数为：{count}")
    with open(f"{symbol_id}-{source}.csv", "w", newline="") as f:
        write = csv.writer(f)
        for d in data:
            write.writerow([f'{get_time_str(d["time"])}.', d["tick"][0]["bid_price"], d["tick"][0]["ask_price"]])


if __name__ == "__main__":
    # date = 20191028
    # start = get_timestamp("2019-10-28 21:30:00")
    # end = get_timestamp("2019-10-28 22:30:00")
    date = 20191030
    start = get_timestamp("2019-10-30 13:30:00")
    end = get_timestamp("2019-10-30 14:30:00")
    # end = get_timestamp()
    # get_k(symbol_id="200", source="9", period="1", start=start, end=end)
    # get_init_price(symbol_id="142", source="3", start=start, end=end, date=date)  # EURUSD
    # get_init_price(symbol_id="222", source="5", start=start, end=end, date=date)  # CL_1912.h
    get_init_price(symbol_id="200", source="1", start=start, end=end, date=date)  # BTCUSDT.b
    # get_init_price(symbol_id="200", source="9", start=start, end=end, date=date)  # BTCUSDT.h
    # get_init_price(symbol_id="567", source="6", start=start, end=end, date=date)  # USDTUSD.k
    # get_init_price(symbol_id="1fa79c0a-d383-11e9-9b77-02bc60f5518c", source="7fdd595c-d2cf-11e9-9b77-02bc60f5518c", start=start, end=end, date=date)  # Apple.m
    # get_init_price(symbol_id="142", source="7fdd595c-d2cf-11e9-9b77-02bc60f5518c", start=start, end=end, date=date)  # EURUSD.m
