import json
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


################################
kline_1day_100_dict = TestHuobiKline15MinData.GetTestData_1min_1000()
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

##################################
