from common.kline_elem import KLineElem
from common.ma_elem import MAElem
from unit_test.test_common.test_ma_elem import TestMAElem


class TestKLineElem:
    @staticmethod
    def Init(kline_elem=KLineElem()):
        kline_elem._amount = 1
        kline_elem._ts = 1
        kline_elem._open = 1
        kline_elem._close = 1
        kline_elem._high = 1
        kline_elem._low = 1
        kline_elem._vol = 1
        ma_elem = MAElem()
        TestMAElem.Init(ma_elem)
        kline_elem._ma_elem = ma_elem

    @staticmethod
    def TestAll():
        input_a = KLineElem()
        TestKLineElem.Init(input_a)

        input_b = KLineElem()
        TestKLineElem.Init(input_b)
        assert (input_a.Equal(input_b))

        TestKLineElem.Init(input_b)
        input_b._amount = 2
        assert (not input_a.Equal(input_b))

        TestKLineElem.Init(input_b)
        input_b._ts = 2
        assert (not input_a.Equal(input_b))

        TestKLineElem.Init(input_b)
        input_b._open = 2
        assert (not input_a.Equal(input_b))

        TestKLineElem.Init(input_b)
        input_b._close = 2
        assert (not input_a.Equal(input_b))

        TestKLineElem.Init(input_b)
        input_b._high = 2
        assert (not input_a.Equal(input_b))

        TestKLineElem.Init(input_b)
        input_b._low = 2
        assert (not input_a.Equal(input_b))

        TestKLineElem.Init(input_b)
        input_b._vol = 2
        assert (not input_a.Equal(input_b))

        TestKLineElem.Init(input_b)
        input_b._ma_elem._ma5 = 2
        assert (not input_a.Equal(input_b))

        TestKLineElem.Init(input_b)
        input_b._ma_elem._ma10 = 2
        assert (not input_a.Equal(input_b))

        TestKLineElem.Init(input_b)
        input_b._ma_elem._ma15 = 2
        assert (not input_a.Equal(input_b))

        TestKLineElem.Init(input_b)
        input_b._ma_elem._ma20 = 2
        assert (not input_a.Equal(input_b))

        TestKLineElem.Init(input_b)
        input_b._ma_elem._ma25 = 2
        assert (not input_a.Equal(input_b))

        TestKLineElem.Init(input_b)
        input_b._ma_elem._ma30 = 2
        assert (not input_a.Equal(input_b))

        TestKLineElem.Init(input_b)
        input_b._ma_elem._ma50 = 2
        assert (not input_a.Equal(input_b))

        TestKLineElem.Init(input_b)
        input_b._ma_elem._ma60 = 2
        assert (not input_a.Equal(input_b))

        TestKLineElem.Init(input_b)
        input_b._ma_elem._ma90 = 2
        assert (not input_a.Equal(input_b))

        TestKLineElem.Init(input_b)
        input_b._ma_elem._ma120 = 2
        assert (not input_a.Equal(input_b))

        TestKLineElem.Init(input_b)
        input_b._ma_elem._ma150 = 2
        assert (not input_a.Equal(input_b))

        TestKLineElem.Init(input_b)
        input_b._ma_elem._ma180 = 2
        assert (not input_a.Equal(input_b))

        print("TestKLineElem pass")

if __name__ == "__main__":
    TestKLineElem.TestAll()
