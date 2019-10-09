import datetime
import math
import asyncio
import random
from time import sleep


def get_ceil(total, per):
    """

    :param total:
    :param per:
    :return:
    """
    return math.ceil(total / per)


def get_between_month(start, end):
    """
    获取两个时间段的每一个月
    :param start:
    :param end:
    :return:
    """
    start = datetime.datetime.strptime(start, '%Y-%m-%d')
    end = datetime.datetime.strptime(end, '%Y-%m-%d')
    start_year, start_month = start.year, start.month
    end_year, end_month = end.year, end.month
    diff_months = (end_year - start_year) * 12 + end_month - start_month
    month_range = []
    year, month = start_year, start_month
    for i in range(diff_months + 1):
        if (start_month + i) % 12 == 1:
            year += 1
            month = 1
        month_range.append("{}-{}".format(year, "0{}".format(month) if month < 10 else month))
        month += 1

    return month_range


class Potatoes(object):
    @classmethod
    def make(cls, num, *args, **kwargs):
        """

        :param num:
        :param args:
        :param kwargs:
        :return:
        """
        potatoes = [cls.__new__(cls, *args, **kwargs) for n in range(num)]
        return potatoes


total_potatoes = Potatoes.make(5)


async def buy_potatoes():
    """
    购买
    :return:
    """
    bucket = []
    i = 1
    async for p in take_potatoes(50):
        bucket.append(p)
        print(i, f"Got potato {id(p)}...")
        i += 1


async def take_potatoes(num):
    """
    获取
    :param num:
    :return:
    """
    count = 0
    while True:
        if len(total_potatoes) == 0:
            await ask_for_potato()
        else:
            potatoes = total_potatoes.pop()
            yield potatoes
            count += 1
            if count == num:
                break


async def ask_for_potato():
    """
    请求
    :return:
    """
    await asyncio.sleep(random.random())
    total_potatoes.extend(Potatoes.make(random.randint(1, 10)))


def run():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(buy_potatoes())
    loop.close()


# if __name__ == '__main__':
#     run()
