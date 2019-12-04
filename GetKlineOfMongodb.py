from classes.DooMongodb import Mongodb
import config
import csv
import time

cfg = config.mongodb
client = Mongodb(cfg["host"], cfg["port"], cfg["user"], cfg["password"], cfg["db"], is_live=False)


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
    collection = client.db[collection_name]
    print(collection)
    data = list(collection.find(query).sort("time", -1))
    count = len(data)
    print(f"K线类型：{period}，在{start} ~ {end}内，存在K线总数为：{count}")

    k = [(data[l + 1]["time"], data[l]["time"], data[l]["time"] - data[l + 1]["time"]) for l in range(count - 1)]

    except_k = list(filter(lambda item: item[2] != period_dict[period], k))
    correct_k = list(filter(lambda item: item[2] == period_dict[period], k))

    print("异常K线为：")
    [print(e, get_time_str(e[0]), get_time_str(e[1])) for e in except_k]

    # print("正常K线为：")
    # [print(c) for c in correct_k]

    # print("全部K线为：")
    # [print(i) for i in k]


def get_init_price(symbol_id, source, start, end, date=None):
    """

    :param symbol_id:
    :param source:
    :param start:
    :param end:
    :param date:
    :return:
    """
    if date is None:
        date = time.strftime("%Y%m%d", time.localtime(time.time()))

    collection_name = f"market_{date}"
    query = {
        "$and": [
            {"symbol_id": symbol_id},
            {"source": source},
            {"time": {"$gte": start, "$lte": end}}
        ]
    }
    print(date, query)
    data = list(client.db[collection_name].find(query).sort("time", 1))
    count = len(data)
    print(f"日期：{date}，在{start} ~ {end}内，存在K线总数为：{count}")
    with open(f"{symbol_id}-{source}.csv", "a", newline="") as f:
        write = csv.writer(f)
        for d in data:
            write.writerow([f'{get_time_str(d["time"])}.', d["tick"][0]["bid_price"], d["tick"][0]["ask_price"]])


def fmt(date_int):
    """

    :param date_int:
    :return:
    """
    date_str = str(date_int)
    result = f"{date_str[:4]}-{date_str[4:6]}-{date_str[-2:]}"
    return result


if __name__ == "__main__":
    # date = 20191028
    # start = get_timestamp("2019-10-28 21:30:00")
    # end = get_timestamp("2019-10-28 22:30:00")
    # date = 20191127
    # start = get_timestamp("2019-11-27 00:00:00")
    # end = get_timestamp("2019-11-27 23:59:59")

    start = get_timestamp("2019-11-29 08:00:00")
    end = get_timestamp("2019-11-29 15:59:59")

    get_k("d930ed50-d475-11e9-b6ae-02bc60277759", "c281e474-d475-11e9-b6ae-02bc60277759", "1", start, end)

    """测试环境"""
    # get_k(symbol_id="200", source="9", period="1", start=start, end=end)
    # get_init_price(symbol_id="142", source="3", start=start, end=end, date=date)  # EURUSD
    # get_init_price(symbol_id="222", source="5", start=start, end=end, date=date)  # CL_1912.h
    # get_init_price(symbol_id="200", source="1", start=start, end=end, date=date)  # BTCUSDT.b
    # get_init_price(symbol_id="200", source="9", start=start, end=end, date=date)  # BTCUSDT.h
    # get_init_price(symbol_id="567", source="6", start=start, end=end, date=date)  # USDTUSD.k
    # get_init_price(symbol_id="1fa79c0a-d383-11e9-9b77-02bc60f5518c", source="7fdd595c-d2cf-11e9-9b77-02bc60f5518c",
    #                start=start, end=end, date=date)  # Apple.m
    # get_init_price(symbol_id="142", source="7fdd595c-d2cf-11e9-9b77-02bc60f5518c", start=start, end=end,
    #                date=date)  # EURUSD.m

    """生产环境"""
    # get_init_price(symbol_id="142", source="3", start=start, end=end, date=date)  # EURUSD.p
    # get_init_price(symbol_id="222", source="5", start=start, end=end, date=date)  # CL_1912.h
    # get_init_price(symbol_id="200", source="1", start=start, end=end, date=date)  # BTCUSDT.b
    # get_init_price(symbol_id="200", source="9", start=start, end=end, date=date)  # BTCUSDT.h
    # get_init_price(symbol_id="567", source="6", start=start, end=end, date=date)  # USDTUSD.k
    # get_init_price(symbol_id="200", source="3", start=start, end=end, date=date)  # BTCUSDT.oz
    # get_init_price(symbol_id="603bc22c-0084-11ea-81bc-022f905e2cf0", source="ed45bb94-dc28-11e9-ae79-022f90c2c9a4",
    #                start=start, end=end, date=date)  # Amazon.m
    # get_init_price(symbol_id="026021cc-0082-11ea-81bc-022f905e2cf0", source="ed45bb94-dc28-11e9-ae79-022f90c2c9a4",
    #                start=start, end=end, date=date)  # Apple.m
    # get_init_price(symbol_id="34ec2950-09ed-11ea-9667-022f90c50569", source="3", start=start, end=end,
    #                date=date)  # USDAED.oz

    # date = 20191128
    # for i in range(0, 14):
    #     hour = f"0{i}" if i < 10 else i
    #     start = get_timestamp(f"{fmt(date)} {hour}:00:00")
    #     end = get_timestamp(f"{fmt(date)} {hour}:59:59")
    #     new_date = date - 1 if i < 8 else date
    #     get_init_price(symbol_id="142", source="3", start=start, end=end, date=new_date)  # EURUSD.p
    #     new_date = date
