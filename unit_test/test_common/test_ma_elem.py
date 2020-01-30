import sys
from common.ma_elem import MAElem


class TestMAElem:
    @staticmethod
    def Init(ma_elem=MAElem()):
        ma_elem.SetMA(5, 1)
        ma_elem.SetMA(10, 1)
        ma_elem.SetMA(15, 1)
        ma_elem.SetMA(20, 1)
        ma_elem.SetMA(25, 1)
        ma_elem.SetMA(30, 1)
        ma_elem.SetMA(50, 1)
        ma_elem.SetMA(60, 1)
        ma_elem.SetMA(90, 1)
        ma_elem.SetMA(120, 1)
        ma_elem.SetMA(150, 1)
        ma_elem.SetMA(180, 1)

    @staticmethod
    def TestEqual():
        input_a = MAElem()
        TestMAElem.Init(input_a)

        input_b = MAElem()
        TestMAElem.Init(input_b)
        assert (input_a.Equal(input_b))

        TestMAElem.Init(input_b)
        input_b.SetMA(5, 2)
        assert (not input_a.Equal(input_b))

        TestMAElem.Init(input_b)
        input_b.SetMA(10, 2)
        assert (not input_a.Equal(input_b))

        TestMAElem.Init(input_b)
        input_b.SetMA(15, 2)
        assert (not input_a.Equal(input_b))

        TestMAElem.Init(input_b)
        input_b.SetMA(20, 2)
        assert (not input_a.Equal(input_b))

        TestMAElem.Init(input_b)
        input_b.SetMA(25, 2)
        assert (not input_a.Equal(input_b))

        TestMAElem.Init(input_b)
        input_b.SetMA(30, 2)
        assert (not input_a.Equal(input_b))

        TestMAElem.Init(input_b)
        input_b.SetMA(50, 2)
        assert (not input_a.Equal(input_b))

        TestMAElem.Init(input_b)
        input_b.SetMA(60, 2)
        assert (not input_a.Equal(input_b))

        TestMAElem.Init(input_b)
        input_b.SetMA(90, 2)
        assert (not input_a.Equal(input_b))

        TestMAElem.Init(input_b)
        input_b.SetMA(120, 2)
        assert (not input_a.Equal(input_b))

        TestMAElem.Init(input_b)
        input_b.SetMA(150, 2)
        assert (not input_a.Equal(input_b))

        TestMAElem.Init(input_b)
        input_b.SetMA(180, 2)
        assert (not input_a.Equal(input_b))

        print("TestEqual pass")

    @staticmethod
    def TestSetGet():
        input_a = MAElem()

        input_a.SetMA(5, 1)
        assert 1 == input_a.GetMA(5)
        input_a.SetMA(5, 1.01)
        assert 1.01 == input_a.GetMA(5)
        input_a.SetMA(5, "123")
        assert "123" == input_a.GetMA(5)

        input_a.SetMA(10, 1)
        assert 1 == input_a.GetMA(10)

        input_a.SetMA(15, 1)
        assert 1 == input_a.GetMA(15)

        input_a.SetMA(20, 1)
        assert 1 == input_a.GetMA(20)

        input_a.SetMA(25, 1)
        assert 1 == input_a.GetMA(25)

        input_a.SetMA(30, 1)
        assert 1 == input_a.GetMA(30)

        input_a.SetMA(50, 1)
        assert 1 == input_a.GetMA(50)

        input_a.SetMA(60, 1)
        assert 1 == input_a.GetMA(60)

        input_a.SetMA(90, 1)
        assert 1 == input_a.GetMA(90)

        input_a.SetMA(120, 1)
        assert 1 == input_a.GetMA(120)

        input_a.SetMA(150, 1)
        assert 1 == input_a.GetMA(150)

        input_a.SetMA(180, 1)
        assert 1 == input_a.GetMA(180)

        print("TestSetGet pass")

    @staticmethod
    def TestValidPeriod():
        assert MAElem.ValidPeiod(1)
        assert MAElem.ValidPeiod(2)
        assert MAElem.ValidPeiod(3)
        assert MAElem.ValidPeiod(4)
        assert MAElem.ValidPeiod(5)
        assert MAElem.ValidPeiod(10)
        assert MAElem.ValidPeiod(15)
        assert MAElem.ValidPeiod(20)
        assert MAElem.ValidPeiod(25)
        assert MAElem.ValidPeiod(30)
        assert MAElem.ValidPeiod(50)
        assert MAElem.ValidPeiod(60)
        assert MAElem.ValidPeiod(90)
        assert MAElem.ValidPeiod(120)
        assert MAElem.ValidPeiod(150)
        assert MAElem.ValidPeiod(180)
        print("TestValidPeiod pass")

    @staticmethod
    def TestAll():
        TestMAElem.TestEqual()
        TestMAElem.TestSetGet()
        TestMAElem.TestValidPeriod()


if __name__ == "__main__":
    TestMAElem.TestAll()
