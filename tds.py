import json
import operator

from unit_test.unit_test_main import UnitTestMain
from data_source.huobi.kline import KLineDataParser
from data_source.huobi.ma import MAEx

from tds_test_huobi_kline_data import TestHuobiKline15MinData

# UnitTestMain.TestAll()

'''

huobi_kline_15min_json_dict = TestHuobiKline15MinData.GetTestData_15min_300()
huobi_kline_15min_json_str = json.dumps(huobi_kline_15min_json_dict)
kline_elem_list_15min = []
kline_elem_list_15min = KLineDataParser.ParseKLineDataEx(huobi_kline_15min_json_str)

kline_elem_list_result = MAEx()
kline_elem_list_result.ComputeMA(30, kline_elem_list_15min)
kline_elem_list_result.ComputeMA(60, kline_elem_list_15min)
kline_elem_list_result.PrintEqualMA(30, 60)
'''

'''
#######################################################################################################################
kline_1day_100_dict = TestHuobiKline15MinData.GetTestData_30min_1000()
kline_1day_100_str = json.dumps(kline_1day_100_dict)
kline_elem_list_1day_100 = []
kline_elem_list_1day_100 = KLineDataParser.ParseKLineDataEx(kline_1day_100_str)

kline_elem_list_result = MAEx()
kline_elem_list_result.ComputeMA(5, kline_elem_list_1day_100)
kline_elem_list_result.ComputeMA(10, kline_elem_list_1day_100)
kline_elem_list_result.ComputeMA(20, kline_elem_list_1day_100)
kline_elem_list_result.ComputeMA(30, kline_elem_list_1day_100)
kline_elem_list_result.ComputeMA(50, kline_elem_list_1day_100)
kline_elem_list_result.ComputeMA(60, kline_elem_list_1day_100)

kline_elem_list_result.PreparePrintEqualMA()

tuple_list = []
tuple1 = kline_elem_list_result.PrintEqualMA2(5, 10)   # profit_sum = 397
tuple_list.append(tuple1)
tuple10 = kline_elem_list_result.PrintEqualMA(5, 10)   # profit_sum = 397
tuple_list.append(tuple10)
tuple100 = kline_elem_list_result.PrintEqualMA(5, 10)   # profit_sum = 397
tuple_list.append(tuple100)

tuple2 = kline_elem_list_result.PrintEqualMA2(10, 20)  # profit_sum = 1295.4399999999996
tuple_list.append(tuple2)
tuple20 = kline_elem_list_result.PrintEqualMA(10, 20)  # profit_sum = 1295.4399999999996
tuple_list.append(tuple20)
tuple200 = kline_elem_list_result.PrintEqualMA(10, 20)  # profit_sum = 1295.4399999999996
tuple_list.append(tuple200)

tuple3 = kline_elem_list_result.PrintEqualMA2(20, 30)  # 108
tuple_list.append(tuple3)
tuple30 = kline_elem_list_result.PrintEqualMA(20, 30)  # 108
tuple_list.append(tuple30)
tuple300 = kline_elem_list_result.PrintEqualMA(20, 30)  # 108
tuple_list.append(tuple300)

tuple4 = kline_elem_list_result.PrintEqualMA2(20, 50)  # -3673
tuple_list.append(tuple4)
tuple40 = kline_elem_list_result.PrintEqualMA(20, 50)  # -3673
tuple_list.append(tuple40)
tuple400 = kline_elem_list_result.PrintEqualMA(20, 50)  # -3673
tuple_list.append(tuple400)

tuple5 = kline_elem_list_result.PrintEqualMA2(30, 60)  # -3673
tuple_list.append(tuple5)
tuple50 = kline_elem_list_result.PrintEqualMA(30, 60)  # -3673
tuple_list.append(tuple50)
tuple500 = kline_elem_list_result.PrintEqualMA(30, 60)  # -3673
tuple_list.append(tuple500)

for i in tuple_list:
    print("ma{0}, ma{1}: counter={2}, profit: {3}".format(i[0], i[1], i[2], i[3]))

#######################################################################################################################
'''

import time
import logging


def GetCurrentTimeStampStr():
    timeNum = int(round(time.time()))
    timeStamp = float(timeNum)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return (otherStyleTime)


logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                    filename='tds.log',
                    filemode='w',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    # a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    # 日志格式
                    )

data_source_list = [
    TestHuobiKline15MinData.GetTestData_1min_1000,
    TestHuobiKline15MinData.GetTestData_5min_1000,
    TestHuobiKline15MinData.GetTestData_15min_1000,
    TestHuobiKline15MinData.GetTestData_30min_1000,
    TestHuobiKline15MinData.GetTestData_1hour_1000,
    TestHuobiKline15MinData.GetTestData_4hour_1000,
    TestHuobiKline15MinData.GetTestData_1day_1000,
    TestHuobiKline15MinData.GetTestData_1week_1000]

data_source_index = 0
tuple_list_all = []
for data_source in data_source_list:
    kline_data_dict = None
    kline_data_str = None
    kline_data_parse_list = None
    kline_elem_list = None
    tuple_list_from_one_data_source = []

    kline_data_dict = data_source()
    kline_data_str = json.dumps(kline_data_dict)
    kline_data_parse_list = []
    kline_data_parse_list = KLineDataParser.ParseKLineDataEx(kline_data_str)

    kline_elem_list = MAEx()
    for ma in range(2, 61):
        kline_elem_list.ComputeMA(ma, kline_data_parse_list)

    kline_elem_list.PreparePrintEqualMA()

    range_start = 2
    for ma_qk in range(range_start, 61):
        logging.debug("{0}, ma_qk={1} start".format(GetCurrentTimeStampStr(), ma_qk))
        for ma_sl in range(range_start + 1, 91):
            for thresh in range(0, 201):
                tuple = None
                tuple = kline_elem_list.PrintEqualMAEx(ma_qk, ma_sl, thresh)
                if tuple and tuple[4] > 0:
                    tuple_list_from_one_data_source.append(tuple)
        range_start += 1
        logging.debug("{0}, ma_qk={1} end".format(GetCurrentTimeStampStr(), ma_qk))
    data_source_index += 1

    tuple_list_from_one_data_source.sort(key=operator.itemgetter(4))
    print(data_source.__name__)
    tuple_list_all.append((data_source.__name__, data_source.__name__))
    tuple_list_all.append(tuple_list_from_one_data_source)
    tuple_list_all.append((data_source.__name__, data_source.__name__))


for tuple_list_one in tuple_list_all:
    if len(tuple_list_one) == 2:
        logging.debug(
            "func_name: ffffffffffffffffffffffffffffffffffffffffffffffffffffff: {0}, {1}".format(tuple_list_one[0], tuple_list_one[1]))
    else:
        idx = 0
        for i in tuple_list_one:
            if i:
                logging.debug(
                    "idx={5} ma{0}, ma{1}: counter={2}, threshold={3}, profit={4}".format(i[0], i[1], i[2], i[3], i[4], idx))
            idx += 1
