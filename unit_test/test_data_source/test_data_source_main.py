from unit_test.test_data_source.test_huobi.test_ma import TestMA, TestMAEx
from unit_test.test_data_source.test_huobi.test_kline import TestKLineDataParser


class TestDataSourceMain:
    @staticmethod
    def TestAll():
        TestMA.TestAll()
        TestMAEx.TestAll()
        TestKLineDataParser.TeatAll()