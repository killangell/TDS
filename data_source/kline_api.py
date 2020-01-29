from common.kline_elem import KLineElem
from data_source.huobi.kline import *

class KLineAPI:
    @staticmethod
    def GetKLineData(period, size, symbol):
        json_data = KLine.GetKLineHistory(period, size, symbol)
        json_dumps = KLineDataParser.ParseKLineData(json_data)
        print(json_dumps)
        print(type(json_dumps))
        kline_list = []
        for item in json_dumps["data"]:
            str = "open:{0}, close:{1}".format(item["open"], item["close"])
            kline_list.append(KLineElem(item["open"], item["close"], item["high"], item["low"]))
            print(str)
        return kline_list