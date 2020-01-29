class MAElem:
    def __init__(self):
        self._ma5 = None
        self._ma10 = None
        self._ma15 = None
        self._ma20 = None
        self._ma25 = None
        self._ma30 = None
        self._ma50 = None
        self._ma60 = None
        self._ma90 = None
        self._ma120 = None
        self._ma150 = None
        self._ma180 = None

    def SetMA(self, period, ma):
        if period == 5:
            self._ma5 = ma
        elif period == 10:
            self._ma10 = ma
        elif period == 15:
            self._ma15 = ma
        elif period == 20:
            self._ma20 = ma
        elif period == 25:
            self._ma25 = ma
        elif period == 30:
            self._ma30 = ma
        elif period == 50:
            self._ma50 = ma
        elif period == 60:
            self._ma60 = ma
        elif period == 90:
            self._ma90 = ma
        elif period == 120:
            self._ma120 = ma
        elif period == 150:
            self._ma150 = ma
        elif period == 180:
            self._ma180 = ma
        else:
            print("SetMA： Invalid input: period={0}, ma={1}".format(period, ma))
            assert False

    def GetMA(self, period):
        if period == 5:
            ma = self._ma5
        elif period == 10:
            ma = self._ma10
        elif period == 15:
            ma = self._ma15
        elif period == 20:
            ma = self._ma20
        elif period == 25:
            ma = self._ma25
        elif period == 30:
            ma = self._ma30
        elif period == 50:
            ma = self._ma50
        elif period == 60:
            ma = self._ma60
        elif period == 90:
            ma = self._ma90
        elif period == 120:
            ma = self._ma120
        elif period == 150:
            ma = self._ma150
        elif period == 180:
            ma = self._ma180
        else:
            print("GetMA： Invalid input: period={0}".format(period))
            assert False
        return ma

    def Equal(self, ma_elem_other):
        if self._ma5 == ma_elem_other._ma5 and \
                self._ma10 == ma_elem_other._ma10 and \
                self._ma15 == ma_elem_other._ma15 and \
                self._ma20 == ma_elem_other._ma20 and \
                self._ma25 == ma_elem_other._ma25 and \
                self._ma30 == ma_elem_other._ma30 and \
                self._ma50 == ma_elem_other._ma50 and \
                self._ma60 == ma_elem_other._ma60 and \
                self._ma90 == ma_elem_other._ma90 and \
                self._ma120 == ma_elem_other._ma120 and \
                self._ma150 == ma_elem_other._ma150 and \
                self._ma180 == ma_elem_other._ma180:
            return True
        else:
            return False

    @staticmethod
    def ValidPeiod(period):
        if period == 5 or period == 10 or period == 15 or period == 20 or \
                period == 25 or period == 30 or period == 50 or period == 60 or \
                period == 90 or period == 120 or period == 150 or period == 180:
            return True
        else:
            return False

    def Print(self):
        print("MAElem: 5:{0}, 10:{1}, 15:{2}, 20:{3}, 25:{4}, 30:{5}, 50:{6}, 60:{7}, 90:{8}, 120:{9}, 150:{10}, 180:{11}".
              format(self._ma5, self._ma10, self._ma15, self._ma20, self._ma25, self._ma30, self._ma50,
                     self._ma60, self._ma90, self._ma120, self._ma150, self._ma180))
