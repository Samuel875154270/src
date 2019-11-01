# import unittest
# from run.run_test_trade import RunOpenCloud
# from BeautifulReport import BeautifulReport
#
# if __name__ == '__main__':
#     cases = unittest.TestSuite()
#     cases.addTest(unittest.makeSuite(RunOpenCloud))
#     result = BeautifulReport(cases)
#     result.report(filename="TestReport", description="Test Report", report_dir="report", theme="theme_default")


def calculate(string, lot, dept=1, mode=1, digit=3, contract=100000, points=10, is_ask=True):
    lot = lot * contract
    string_list = list(map(lambda item: eval(item), string.replace("/", ",").split("|")))

    calculate_lot = 0
    calculate_price = 0
    last_lot = None
    for sl in string_list:
        calculate_lot += sl[1]
        calculate_price += sl[0] * sl[1] * dept
        if calculate_lot > lot:
            last_lot = sl
            calculate_lot -= sl[1]
            calculate_price -= sl[0] * sl[1] * dept
            break

    if last_lot is None:
        if mode == 1:
            calculate_price += (lot - calculate_lot) * string_list[-1][0] * dept
            price = calculate_price / lot
        else:
            price = calculate_price / calculate_lot

    else:
        calculate_price += (lot - calculate_lot) * last_lot[0] * dept
        price = calculate_price / lot

    price = price + points / (10 ** digit) if is_ask is True else price - points / (10 ** digit)
    print(round(price, digit))


if __name__ == '__main__':
    # calculate(
    #     string="(108.60100/100000)|(108.60100/100000)|(108.60100/500000)|(108.60000/1000000)|(108.60000/1000000)",
    #     lot=40,
    #     dept=1,
    #     mode=0,
    #     digit=3,
    #     contract=100000,
    #     points=-19,
    #     is_ask=False
    # )

    import json

    x = 1
    json.loads(x)