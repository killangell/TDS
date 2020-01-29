import json
from data_source.huobi.kline import KLineDataParser

class TestKLineDataParser:
    @staticmethod
    def TestParseKLineDataEx1():
        huobi_kline_json_response = {"status":"a",
                                     "ch":"b",
                                     "ts":1,
                                     "data":[
                                         {"amount":1.1, "open":2.2, "close":3.3, "high":4.4, "id":5.5, "count":6.6, "low":7.7, "vol":8.8}]}
        str = json.dumps(huobi_kline_json_response)
        kline_elem_list_parse_result = KLineDataParser.ParseKLineDataEx(str)
        assert 1 == len(kline_elem_list_parse_result)
        i0 = kline_elem_list_parse_result[0]
        assert i0._amount == 1.1
        assert i0._ts == 5.5
        assert i0._open == 2.2
        assert i0._close == 3.3
        assert i0._high == 4.4
        assert i0._low == 7.7
        assert i0._vol == 8.8
        print("TestParseKLineDataEx1: pass")

    @staticmethod
    def TestParseKLineDataEx2():
        huobi_kline_json_response = {"status":"a",
                                     "ch":"b",
                                     "ts":1,
                                     "data":[
                                         {"amount":1.1, "open":2.2, "close":3.3, "high":4.4, "id":5.5, "count":6.6, "low":7.7, "vol":8.8},
                                         {"amount":1.11, "open":2.21, "close":3.31, "high":4.41, "id":5.51, "count":6.61, "low":7.71, "vol":8.81}]}
        str = json.dumps(huobi_kline_json_response)
        kline_elem_list_parse_result = KLineDataParser.ParseKLineDataEx(str)
        assert 2 == len(kline_elem_list_parse_result)
        i0 = kline_elem_list_parse_result[0]
        assert i0._amount == 1.1
        assert i0._ts == 5.5
        assert i0._open == 2.2
        assert i0._close == 3.3
        assert i0._high == 4.4
        assert i0._low == 7.7
        assert i0._vol == 8.8
        i1 = kline_elem_list_parse_result[1]
        assert i1._amount == 1.11
        assert i1._ts == 5.51
        assert i1._open == 2.21
        assert i1._close == 3.31
        assert i1._high == 4.41
        assert i1._low == 7.71
        assert i1._vol == 8.81
        print("TestParseKLineDataEx2: pass")

    @staticmethod
    def TestParseKLineDataEx3():
        huobi_kline_json_response = {"status": "a",
                                     "ch": "b",
                                     "ts": 1,
                                     "data": [
                                         {"amount": 1.1, "open": 2.2, "close": 3.3, "high": 4.4, "id": 5.5,
                                          "count": 6.6, "low": 7.7, "vol": 8.8},
                                         {"amount": 1.11, "open": 2.21, "close": 3.31, "high": 4.41, "id": 5.51,
                                          "count": 6.61, "low": 7.71, "vol": 8.81},
                                         {"amount": 1.12, "open": 2.22, "close": 3.32, "high": 4.42, "id": 5.52,
                                          "count": 6.62, "low": 7.72, "vol": 8.82},
                                         {"amount": 1.13, "open": 2.23, "close": 3.33, "high": 4.43, "id": 5.53,
                                          "count": 6.63, "low": 7.73, "vol": 8.83},
                                         {"amount": 1.14, "open": 2.24, "close": 3.34, "high": 4.44, "id": 5.54,
                                          "count": 6.64, "low": 7.74, "vol": 8.84},
                                         {"amount": 1.15, "open": 2.25, "close": 3.35, "high": 4.45, "id": 5.55,
                                          "count": 6.65, "low": 7.75, "vol": 8.85},
                                         {"amount": 1.16, "open": 2.26, "close": 3.36, "high": 4.46, "id": 5.56,
                                          "count": 6.66, "low": 7.76, "vol": 8.86},
                                         {"amount": 1.17, "open": 2.27, "close": 3.37, "high": 4.47, "id": 5.57,
                                          "count": 6.67, "low": 7.77, "vol": 8.87},
                                         {"amount": 1.18, "open": 2.28, "close": 3.38, "high": 4.48, "id": 5.58,
                                          "count": 6.68, "low": 7.78, "vol": 8.88},
                                         {"amount": 1.19, "open": 2.29, "close": 3.39, "high": 4.49, "id": 5.59,
                                          "count": 6.69, "low": 7.79, "vol": 8.89}]}
        str = json.dumps(huobi_kline_json_response)
        kline_elem_list_parse_result = KLineDataParser.ParseKLineDataEx(str)
        assert 10 == len(kline_elem_list_parse_result)
        i0 = kline_elem_list_parse_result[0]
        assert i0._amount == 1.1
        assert i0._ts == 5.5
        assert i0._open == 2.2
        assert i0._close == 3.3
        assert i0._high == 4.4
        assert i0._low == 7.7
        assert i0._vol == 8.8
        i1 = kline_elem_list_parse_result[1]
        assert i1._amount == 1.11
        assert i1._ts == 5.51
        assert i1._open == 2.21
        assert i1._close == 3.31
        assert i1._high == 4.41
        assert i1._low == 7.71
        assert i1._vol == 8.81
        i3 = kline_elem_list_parse_result[3]
        assert i3._amount == 1.13
        assert i3._ts == 5.53
        assert i3._open == 2.23
        assert i3._close == 3.33
        assert i3._high == 4.43
        assert i3._low == 7.73
        assert i3._vol == 8.83
        i5 = kline_elem_list_parse_result[5]
        assert i5._amount == 1.15
        assert i5._ts == 5.55
        assert i5._open == 2.25
        assert i5._close == 3.35
        assert i5._high == 4.45
        assert i5._low == 7.75
        assert i5._vol == 8.85
        i7 = kline_elem_list_parse_result[7]
        assert i7._amount == 1.17
        assert i7._ts == 5.57
        assert i7._open == 2.27
        assert i7._close == 3.37
        assert i7._high == 4.47
        assert i7._low == 7.77
        assert i7._vol == 8.87
        i9 = kline_elem_list_parse_result[9]
        assert i9._amount == 1.19
        assert i9._ts == 5.59
        assert i9._open == 2.29
        assert i9._close == 3.39
        assert i9._high == 4.49
        assert i9._low == 7.79
        assert i9._vol == 8.89
        print("TestParseKLineDataEx3: pass")

    @staticmethod
    def TeatAll():
        TestKLineDataParser.TestParseKLineDataEx1()
        TestKLineDataParser.TestParseKLineDataEx2()
        TestKLineDataParser.TestParseKLineDataEx3()


if __name__ == "__main__":
    TestKLineDataParser.TeatAll()