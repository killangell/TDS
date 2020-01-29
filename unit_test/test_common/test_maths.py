import sys
from common.maths import *

class TestMaths:
    @staticmethod
    def Test_FloatAverage():
        fl = [1.11, 2.22, 3.33, 4.44, 5.55]
        ret = Maths.FloatAverage(fl)
        assert (ret == 3.33)

    @staticmethod
    def TestAll():
        TestMaths.Test_FloatAverage()


if __name__ == "__main__":
    TestMaths.TestAll()