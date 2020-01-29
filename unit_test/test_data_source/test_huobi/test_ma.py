from common.maths import Maths
from common.kline_elem import KLineElem
from common.ma_elem import MAElem

from data_source.huobi.ma import MA, MAEx


class TestMA:
    @staticmethod
    def TestAll():
        close_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        ma1_expect_list = [(0, 0.0), (1, 1.0), (2, 2.0), (3, 3.0), (4, 4.0), (5, 5.0), (6, 6.0), (7, 7.0), (8, 8.0),
                           (9, 9.0)]
        ma2_expect_list = [(0, 0.5), (1, 1.5), (2, 2.5), (3, 3.5), (4, 4.5), (5, 5.5), (6, 6.5), (7, 7.5), (8, 8.5),
                           (9, -1)]
        ma3_expect_list = [(0, 1.0), (1, 2.0), (2, 3.0), (3, 4.0), (4, 5.0), (5, 6.0), (6, 7.0), (7, 8.0), (8, -1),
                           (9, -1)]
        ma10_expect_list = [(0, Maths.FloatAverage(close_list)), (1, -1), (2, -1), (3, -1), (4, -1), (5, -1), (6, -1),
                            (7, -1), (8, -1), (9, -1)]

        ma = MA()

        ma.Reset()
        ma.GetMAList(1, close_list)
        ma.PrintAll()
        index = 0
        for i, j in ma1_expect_list:
            assert ((i, j) == ma.ma[index])
            index += 1

        ma.Reset()
        ma.GetMAList(2, close_list)
        ma.PrintAll()
        index = 0
        for i, j in ma2_expect_list:
            assert ((i, j) == ma.ma[index])
            index += 1

        ma.Reset()
        ma.GetMAList(3, close_list)
        ma.PrintAll()
        index = 0
        for i, j in ma3_expect_list:
            assert ((i, j) == ma.ma[index])
            index += 1

        ma.Reset()
        ma.GetMAList(10, close_list)
        ma.PrintAll()
        index = 0
        for i, j in ma10_expect_list:
            if (index == 0):
                assert ((i, j) == (0, Maths.FloatAverage(close_list)))
            else:
                assert ((i, j) == ma.ma[index])
            index += 1


class TestMAEx:
    @staticmethod
    def TestMA5():
        # Test input
        kline_elem_list = []
        for i in range(0, 10):
            kline_elem = KLineElem()
            kline_elem._close = i
            kline_elem_list.append(kline_elem)
        # Test expect output
        kline_elem_list_expect = []
        # 0
        kline_elem0 = KLineElem()
        kline_elem0._close = 0
        float_list0 = range(0, 5)
        kline_elem0._ma_elem._ma5 = Maths.FloatAverage(float_list0)
        kline_elem_list_expect.append(kline_elem0)
        # 1
        kline_elem1 = KLineElem()
        kline_elem1._close = 1
        float_list1 = range(1, 6)
        kline_elem1._ma_elem._ma5 = Maths.FloatAverage(float_list1)
        kline_elem_list_expect.append(kline_elem1)
        # 2
        kline_elem2 = KLineElem()
        kline_elem2._close = 2
        float_list2 = range(2, 7)
        kline_elem2._ma_elem._ma5 = Maths.FloatAverage(float_list2)
        kline_elem_list_expect.append(kline_elem2)
        # 3
        kline_elem3 = KLineElem()
        kline_elem3._close = 3
        float_list3 = range(3, 8)
        kline_elem3._ma_elem._ma5 = Maths.FloatAverage(float_list3)
        kline_elem_list_expect.append(kline_elem3)
        # 4
        kline_elem4 = KLineElem()
        kline_elem4._close = 4
        float_list4 = range(4, 9)
        kline_elem4._ma_elem._ma5 = Maths.FloatAverage(float_list4)
        kline_elem_list_expect.append(kline_elem4)
        # 5
        kline_elem5 = KLineElem()
        kline_elem5._close = 5
        float_list5 = range(5, 10)
        kline_elem5._ma_elem._ma5 = Maths.FloatAverage(float_list5)
        kline_elem_list_expect.append(kline_elem5)
        # 6
        kline_elem6 = KLineElem()
        kline_elem6._close = 6
        kline_elem6._ma_elem._ma5 = -1
        kline_elem_list_expect.append(kline_elem6)
        # 7
        kline_elem7 = KLineElem()
        kline_elem7._close = 7
        kline_elem7._ma_elem._ma5 = -1
        kline_elem_list_expect.append(kline_elem7)
        # 8
        kline_elem8 = KLineElem()
        kline_elem8._close = 8
        kline_elem8._ma_elem._ma5 = -1
        kline_elem_list_expect.append(kline_elem8)
        # 9
        kline_elem9 = KLineElem()
        kline_elem9._close = 9
        kline_elem9._ma_elem._ma5 = -1
        kline_elem_list_expect.append(kline_elem9)

        # Test real output
        kline_elem_list_result = MAEx()
        kline_elem_list_result.ComputeMA(5, kline_elem_list)
        assert (len(kline_elem_list_expect) == len(kline_elem_list_result._kline_elem_list))
        index = 0
        for k in kline_elem_list_expect:
            assert (k.Equal(kline_elem_list_result._kline_elem_list[index]))
            print("TestMA5: index={0} pass".format(index))
            index += 1

    @staticmethod
    def TestMA10():
        # Test input
        kline_elem_list = []
        for i in range(0, 10):
            kline_elem = KLineElem()
            kline_elem._close = i
            kline_elem_list.append(kline_elem)
        # Test expect output
        kline_elem_list_expect = []
        # 0
        kline_elem0 = KLineElem()
        kline_elem0._close = 0
        float_list0 = range(0, 10)
        kline_elem0._ma_elem.SetMA(10, Maths.FloatAverage(float_list0))
        kline_elem_list_expect.append(kline_elem0)
        # 1 ~ 9
        for j in range(1, 10):
            kline_elem1 = KLineElem()
            kline_elem1._close = j
            kline_elem1._ma_elem.SetMA(10, -1)
            kline_elem_list_expect.append(kline_elem1)

        # Test real output
        kline_elem_list_result = MAEx()
        kline_elem_list_result.ComputeMA(10, kline_elem_list)
        assert (len(kline_elem_list_expect) == len(kline_elem_list_result._kline_elem_list))
        index = 0
        for k in kline_elem_list_expect:
            assert (k.Equal(kline_elem_list_result._kline_elem_list[index]))
            print("TestMA10: index={0} pass".format(index))
            index += 1

        kline_elem_list_result.ComputeMA(5, kline_elem_list)
        assert (len(kline_elem_list_expect) == len(kline_elem_list_result._kline_elem_list))

    @staticmethod
    def TestStrategy():
        kline_elem_list = []
        kline_elem0 = KLineElem()
        kline_elem0._close = 1
        kline_elem0._ma_elem._ma30 = 0
        kline_elem0._ma_elem._ma60 = 0
        kline_elem_list.append(kline_elem0)
        kline_elem1 = KLineElem()
        kline_elem1._close = 2
        kline_elem1._ma_elem._ma30 = 3
        kline_elem1._ma_elem._ma60 = 2
        kline_elem_list.append(kline_elem1)
        kline_elem2 = KLineElem()
        kline_elem2._close = 3
        kline_elem2._ma_elem._ma30 = 4
        kline_elem2._ma_elem._ma60 = 3
        kline_elem_list.append(kline_elem2)
        kline_elem3 = KLineElem()
        kline_elem3._close = 4
        kline_elem3._ma_elem._ma30 = 4
        kline_elem3._ma_elem._ma60 = 5
        kline_elem_list.append(kline_elem3)
        maex = MAEx()
        maex._kline_elem_list = kline_elem_list
        maex.PrintEqualMA(30, 60)

    @staticmethod
    def TestAll():
        TestMAEx.TestMA5()
        TestMAEx.TestMA10()
        TestMAEx.TestStrategy()

if __name__ == "__main__":
    TestMA.TestAll()
    TestMAEx.TestAll()
