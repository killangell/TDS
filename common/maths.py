from common.kline_elem import KLineElem

class Maths:
    @staticmethod
    def FloatAverage(float_list):
        sum = 0
        for i in float_list:
            sum += float(i)
        return round(sum/len(float_list), 2)

    @staticmethod
    def FloatAverage2(kline_elem_list):
        sum = 0
        for i in kline_elem_list:
            sum += float(i._close)
        return round(sum/len(kline_elem_list), 2)