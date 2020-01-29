from unit_test.test_common.test_common_main import *
from unit_test.test_data_source.test_data_source_main import *

class UnitTestMain:
    @staticmethod
    def TestAll():
        TestCommonMain.TestAll()
        TestDataSourceMain.TestAll()


if __name__ == "__main__":
    UnitTestMain.TestAll()