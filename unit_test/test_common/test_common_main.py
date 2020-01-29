from unit_test.test_common.test_maths import TestMaths
from unit_test.test_common.test_ma_elem import TestMAElem
from unit_test.test_common.test_kline_elem import TestKLineElem


class TestCommonMain:
    @staticmethod
    def TestAll():
        # return None
        TestMaths.TestAll()
        TestKLineElem.TestAll()
        TestMAElem.TestAll()


if __name__ == "__main__":
    TestCommonMain().TestAll()
