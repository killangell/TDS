
#https://api.huobi.pro/market/history/kline?period=30min&size=1&symbol=btcusdt

HUOBI_URI = "https://api.huobi.pro"

class HuobiUri:
    @staticmethod
    def GetKLineUrl(period, size, symbol):
        url = "{0}/market/history/kline?period={1}&size={2}&symbol={3}".format(HUOBI_URI, period, size, symbol)
        return url

    @staticmethod
    def GetKLineUrlData(period, size, symbol):
        url = HuobiUri.GetKLineUrl(period, size, symbol)
        return None
