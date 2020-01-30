import logging
import operator

logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                    filename='tds_test.log',
                    filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    # a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    # 日志格式
                    )

range_start = 2
for ma_qk in range(range_start, 10):
    for ma_sl in range(range_start + 1, 10):
        for thresh in range(1, 5):
            logging.debug("{0}.{1}.{2}".format(ma_qk, ma_sl, thresh))
    range_start += 1


list = []
list.append((2,5,1,1,7,1.1))
list.append((2,6,1,1,7,7.7))
list.append((2,5,1,3,7,-9.9))
list.append((2,5,1,1,8,2.2))
list.append((2,5,1,9,7,3.3))

list.sort(key=operator.itemgetter(5))
print(list)

def test_func():
    pass

list = [test_func]

print((list[0].__name__))

tuple = (1,2,3)
print(len(tuple))
tuple = ("123", "1234")
print(len(tuple))
tuple = ((list[0].__name__, list[0].__name__, list[0].__name__))
print(len(tuple))
