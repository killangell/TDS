import time
import logging
from common.ma_elem import MAElem


class KLineElem:
    def __init__(self):
        self._amount = None
        self._ts = None
        self._ts_str = None
        self._open = None
        self._close = None
        self._high = None
        self._low = None
        self._vol = None
        self._ma_elem = MAElem()

    def Equal(self, kline_elem_other):
        if self._amount == kline_elem_other._amount and \
                self._ts == kline_elem_other._ts and \
                self._open == kline_elem_other._open and \
                self._close == kline_elem_other._close and \
                self._high == kline_elem_other._high and \
                self._low == kline_elem_other._low and \
                self._vol == kline_elem_other._vol and \
                self._ma_elem.Equal(kline_elem_other._ma_elem):
            return True
        else:
            return False

    def ParseTS(self, ts):
        try:
            currentTimeStamp = int(ts)  # 1580032800
            time_local = time.localtime(currentTimeStamp)  # 格式化时间戳为本地时间
            time_YmdHMS = time.strftime("%Y%m%d_%H%M%S", time_local)  # 自定义时间格式
            return time_YmdHMS
        except:
            return ts

    def Print(self):
        logging.debug(self.ParseTS(self._ts))
        logging.debug("KLineElem: amount:{0}, ts:{1}, open:{2}, close:{3}, high:{4}, low:{5}, vol:{6}".format(self._amount,
                                                                                                      self.ParseTS(self._ts),
                                                                                                      self._open,
                                                                                                      self._close,
                                                                                                      self._high,
                                                                                                      self._low,
                                                                                                      self._vol))
        self._ma_elem.Print()
        #print("")
