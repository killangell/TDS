import sys
import logging
from data_source.huobi.kline import *
from common.kline_elem import KLineElem

sys.setrecursionlimit(1000000)


class MAEx:
    def __init__(self):
        self._kline_elem_list = []
    '''
    def ComputeMA(self, period, kline_elem_list=[]):
        if len(kline_elem_list) >= int(period):
            todo_list = kline_elem_list[0:period:1]
            # print(todo_list)
            ma = Maths.FloatAverage2(todo_list)
        else:
            todo_list = kline_elem_list[0::1]
            # print(todo_list)
            ma = -1
        kline_elem_list[0]._ma_elem.SetMA(period, ma)
        self._kline_elem_list.append(kline_elem_list[0])
        if len(kline_elem_list) > 1:
            # Remove head from close_list
            self.ComputeMA(period, kline_elem_list[1::1])
    '''

    def ComputeMA(self, period, kline_elem_list=[], reset=True):
        if reset:
            self._kline_elem_list = []
        if len(kline_elem_list) >= int(period):
            todo_list = kline_elem_list[0:period:1]
            # print(todo_list)
            ma = Maths.FloatAverage2(todo_list)
        else:
            todo_list = kline_elem_list[0::1]
            # print(todo_list)
            ma = -1
        kline_elem_list[0]._ma_elem.SetMA(period, ma)
        self._kline_elem_list.append(kline_elem_list[0])
        if len(kline_elem_list) > 1:
            # Remove head from close_list
            self.ComputeMA(period, kline_elem_list[1::1], False)

    def Print(self):
        for i in self._kline_elem_list:
            i.Print()

    def GetState(self, ma_quick, ma_slow):
        if ma_quick == ma_slow:
            return 1
        elif ma_quick > ma_slow:
            return 2
        else:
            return 3

    def GetState2(self, ma_quick, ma_slow):
        if ma_quick == ma_slow:
            return 1
        elif abs(ma_quick - ma_slow) >= 20:
            if ma_quick > ma_slow:
                return 2
            else:
                return 3
        else:
            return 0

    def GetStateEx(self, ma_quick, ma_slow, threshold):
        if ma_quick == ma_slow:
            return 1
        elif abs(ma_quick - ma_slow) >= threshold:
            if ma_quick > ma_slow:
                return 2
            else:
                return 3
        else:
            return 0

    def PreparePrintEqualMA(self):
        self._kline_elem_list.reverse()

    def PrintEqualMA(self, period_quick, period_slow):
        '''
        state_machine = 1, ma_quick == ma_slow
        state_machine = 2, ma_quick > ma_slow
        state_machine = 3, ma_quick < ma_slow
        1 -> 2, long
        1 -> 3, short
        2 -> 3, short
        3 -> 2, long
        '''
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("{0}, {1}".format(period_quick, period_slow))
        profit_sum = 0
        profit_current = 0
        kline_elem_old = None
        kline_elem_current = None
        strategy_need_change = False
        strategy_long_old = None
        strategy_long_current = None
        strategy_counter = 0
        state_init = 0
        index = 0
        for i in self._kline_elem_list:
            ma_quick = i._ma_elem.GetMA(period_quick)
            ma_slow = i._ma_elem.GetMA(period_slow)
            if ma_quick != -1 and ma_slow != -1:
                break
            index += 1
        state_init = self.GetState(ma_quick, ma_slow)
        for i in self._kline_elem_list[index+1::1]:
            ma_quick= i._ma_elem.GetMA(period_quick)
            ma_slow = i._ma_elem.GetMA(period_slow)
            # if ma_quick != -1 and ma_slow != -1:
            state_current = self.GetState(ma_quick, ma_slow)
            if state_init != state_current:
                strategy_need_change = False
                if state_init == 1 and state_current == 2:
                    state_init = state_current
                    strategy_need_change = True
                    strategy_long_current = True
                    strategy_counter += 1
                    print("long +++++++++++++++++:")
                    i.Print()
                    print("long *****************")
                elif state_init == 1 and state_current == 3:
                    state_init = state_current
                    strategy_need_change = True
                    strategy_long_current = False
                    strategy_counter += 1
                    print("short -----------------")
                    i.Print()
                    print("short *****************")
                elif state_init == 2 and state_current == 3:
                    state_init = state_current
                    strategy_need_change = True
                    strategy_long_current = False
                    strategy_counter += 1
                    print("short -----------------")
                    i.Print()
                    print("short *****************")
                elif state_init == 3 and state_current == 2:
                    state_init = state_current
                    strategy_need_change = True
                    strategy_long_current = True
                    strategy_counter += 1
                    print("long +++++++++++++++++:")
                    i.Print()
                    print("long *****************")
                else:
                    strategy_need_change = False
                    print("not defined: state_init={0}, state_current={1}".format(state_init, state_current))

                if strategy_need_change:
                    kline_elem_current = i
                    if kline_elem_old:
                        if state_current == 2:
                           assert not strategy_long_old or strategy_long_old == False
                           if strategy_long_old == False:
                                # print("profit: short old")
                                # kline_elem_old.Print()
                                # print("profit: short current")
                                # kline_elem_current.Print()
                                profit_current = kline_elem_old._close - kline_elem_current._close
                                print("profit: short: {0} - {1} = {2}".format(kline_elem_old._close,
                                                                      kline_elem_current._close,
                                                                      profit_current))
                                profit_sum += profit_current
                                print("profit_sum = {0}, profit_current={1}".format(profit_sum, profit_current))
                                print("")
                                print("")
                        elif state_current == 3:
                           assert not strategy_long_old or strategy_long_old == True
                           if strategy_long_old == True:
                                # print("profit: long current")
                                # kline_elem_current.Print()
                                # print("profit: long old")
                                # kline_elem_old.Print()
                                profit_current = kline_elem_current._close - kline_elem_old._close
                                print("profit: long: {0} - {1} = {2}".format(kline_elem_current._close,
                                                                  kline_elem_old._close,
                                                                  profit_current))
                                profit_sum += profit_current
                                print("profit_sum = {0}, profit_current={1}".format(profit_sum, profit_current))
                                print("")
                                print("")
                        else:
                           print("not defined 2")
                    kline_elem_old = kline_elem_current
                    strategy_long_old = strategy_long_current
        return (period_quick, period_slow, strategy_counter, profit_sum)

    def PrintEqualMA2(self, period_quick, period_slow):
        '''
        state_machine = 1, ma_quick == ma_slow
        state_machine = 2, ma_quick > ma_slow
        state_machine = 3, ma_quick < ma_slow
        1 -> 2, long
        1 -> 3, short
        2 -> 3, short
        3 -> 2, long
        '''
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("{0}, {1}".format(period_quick, period_slow))
        profit_sum = 0
        profit_current = 0
        kline_elem_old = None
        kline_elem_current = None
        strategy_need_change = False
        strategy_long_old = None
        strategy_long_current = None
        strategy_counter = 0
        state_init = 0
        index = 0
        for i in self._kline_elem_list:
            ma_quick = i._ma_elem.GetMA(period_quick)
            ma_slow = i._ma_elem.GetMA(period_slow)
            if ma_quick != -1 and ma_slow != -1:
                state_init = self.GetState2(ma_quick, ma_slow)
                if state_init != 0:
                    break
            index += 1
        for i in self._kline_elem_list[index+1::1]:
            ma_quick= i._ma_elem.GetMA(period_quick)
            ma_slow = i._ma_elem.GetMA(period_slow)
            # if ma_quick != -1 and ma_slow != -1:
            state_current = self.GetState2(ma_quick, ma_slow)
            if state_current == 0:
                continue
            if state_init != state_current:
                strategy_need_change = False
                if state_init == 1 and state_current == 2:
                    state_init = state_current
                    strategy_need_change = True
                    strategy_long_current = True
                    strategy_counter += 1
                    print("long +++++++++++++++++:")
                    i.Print()
                    print("long *****************")
                elif state_init == 1 and state_current == 3:
                    state_init = state_current
                    strategy_need_change = True
                    strategy_long_current = False
                    strategy_counter += 1
                    print("short -----------------")
                    i.Print()
                    print("short *****************")
                elif state_init == 2 and state_current == 3:
                    state_init = state_current
                    strategy_need_change = True
                    strategy_long_current = False
                    strategy_counter += 1
                    print("short -----------------")
                    i.Print()
                    print("short *****************")
                elif state_init == 3 and state_current == 2:
                    state_init = state_current
                    strategy_need_change = True
                    strategy_long_current = True
                    strategy_counter += 1
                    print("long +++++++++++++++++:")
                    i.Print()
                    print("long *****************")
                else:
                    strategy_need_change = False
                    print("not defined: state_init={0}, state_current={1}".format(state_init, state_current))

                if strategy_need_change:
                    kline_elem_current = i
                    if kline_elem_old:
                        if state_current == 2:
                           assert not strategy_long_old or strategy_long_old == False
                           if strategy_long_old == False:
                                # print("profit: short old")
                                # kline_elem_old.Print()
                                # print("profit: short current")
                                # kline_elem_current.Print()
                                profit_current = kline_elem_old._close - kline_elem_current._close
                                print("profit: short: {0} - {1} = {2}".format(kline_elem_old._close,
                                                                      kline_elem_current._close,
                                                                      profit_current))
                                profit_sum += profit_current
                                print("profit_sum = {0}, profit_current={1}".format(profit_sum, profit_current))
                                print("")
                                print("")
                        elif state_current == 3:
                           assert not strategy_long_old or strategy_long_old == True
                           if strategy_long_old == True:
                                # print("profit: long current")
                                # kline_elem_current.Print()
                                # print("profit: long old")
                                # kline_elem_old.Print()
                                profit_current = kline_elem_current._close - kline_elem_old._close
                                print("profit: long: {0} - {1} = {2}".format(kline_elem_current._close,
                                                                  kline_elem_old._close,
                                                                  profit_current))
                                profit_sum += profit_current
                                print("profit_sum = {0}, profit_current={1}".format(profit_sum, profit_current))
                                print("")
                                print("")
                        else:
                           print("not defined 2")
                    kline_elem_old = kline_elem_current
                    strategy_long_old = strategy_long_current
        return (period_quick, period_slow, strategy_counter, profit_sum)

    def PrintEqualMAEx(self, period_quick, period_slow, threshold):
        '''
        state_machine = 1, ma_quick == ma_slow
        state_machine = 2, ma_quick > ma_slow
        state_machine = 3, ma_quick < ma_slow
        1 -> 2, long
        1 -> 3, short
        2 -> 3, short
        3 -> 2, long
        '''
        logging.debug("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        logging.debug("period_quick={0}, period_slow={1}, threshold={2}".format(period_quick, period_slow, threshold))
        profit_sum = 0
        profit_current = 0
        kline_elem_old = None
        kline_elem_current = None
        strategy_need_change = False
        strategy_long_old = None
        strategy_long_current = None
        strategy_counter = 0
        state_init = 0
        index = 0
        for i in self._kline_elem_list:
            ma_quick = i._ma_elem.GetMA(period_quick)
            ma_slow = i._ma_elem.GetMA(period_slow)
            if ma_quick != -1 and ma_slow != -1:
                state_init = self.GetStateEx(ma_quick, ma_slow, threshold)
                if state_init != 0:
                    break
            index += 1
        for i in self._kline_elem_list[index+1::1]:
            ma_quick= i._ma_elem.GetMA(period_quick)
            ma_slow = i._ma_elem.GetMA(period_slow)
            # if ma_quick != -1 and ma_slow != -1:
            state_current = self.GetStateEx(ma_quick, ma_slow, threshold)
            if state_current == 0:
                continue
            if state_init != state_current:
                strategy_need_change = False
                if state_init == 1 and state_current == 2:
                    state_init = state_current
                    strategy_need_change = True
                    strategy_long_current = True
                    strategy_counter += 1
                    # logging.debug("long +++++++++++++++++:")
                    # i.Print()
                    # logging.debug("long *****************")
                elif state_init == 1 and state_current == 3:
                    state_init = state_current
                    strategy_need_change = True
                    strategy_long_current = False
                    strategy_counter += 1
                    # logging.debug("short -----------------")
                    # i.Print()
                    # logging.debug("short *****************")
                elif state_init == 2 and state_current == 3:
                    state_init = state_current
                    strategy_need_change = True
                    strategy_long_current = False
                    strategy_counter += 1
                    # logging.debug("short -----------------")
                    # i.Print()
                    # logging.debug("short *****************")
                elif state_init == 3 and state_current == 2:
                    state_init = state_current
                    strategy_need_change = True
                    strategy_long_current = True
                    strategy_counter += 1
                    # logging.debug("long +++++++++++++++++:")
                    # i.Print()
                    # logging.debug("long *****************")
                else:
                    strategy_need_change = False
                    logging.debug("not defined: state_init={0}, state_current={1}".format(state_init, state_current))

                if strategy_need_change:
                    kline_elem_current = i
                    if kline_elem_old:
                        if state_current == 2:
                           assert not strategy_long_old or strategy_long_old == False
                           if strategy_long_old == False:
                                # print("profit: short old")
                                # kline_elem_old.Print()
                                # print("profit: short current")
                                # kline_elem_current.Print()
                                profit_current = kline_elem_old._close - kline_elem_current._close
                                logging.debug("profit: short: {0} - {1} = {2}".format(kline_elem_old._close,
                                                                      kline_elem_current._close,
                                                                      profit_current))
                                profit_sum += profit_current
                                logging.debug("profit_sum = {0}, profit_current={1}".format(profit_sum, profit_current))
                                logging.debug("")
                                logging.debug("")
                        elif state_current == 3:
                           assert not strategy_long_old or strategy_long_old == True
                           if strategy_long_old == True:
                                # print("profit: long current")
                                # kline_elem_current.Print()
                                # print("profit: long old")
                                # kline_elem_old.Print()
                                profit_current = kline_elem_current._close - kline_elem_old._close
                                logging.debug("profit: long: {0} - {1} = {2}".format(kline_elem_current._close,
                                                                  kline_elem_old._close,
                                                                  profit_current))
                                profit_sum += profit_current
                                logging.debug("profit_sum = {0}, profit_current={1}".format(profit_sum, profit_current))
                                logging.debug("")
                                logging.debug("")
                        else:
                           logging.debug("not defined 2")
                    kline_elem_old = kline_elem_current
                    strategy_long_old = strategy_long_current
        if strategy_counter >= 1:
            return (period_quick, period_slow, strategy_counter, threshold, profit_sum)
        else:
            return None

class MA:
    def __init__(self):
        self.Reset()

    def Reset(self):
        self.period = None
        # Format (close, average)
        self.ma = []

    def GetMAList(self, period, close_list):
        '''
        print(close_list)
        print(len(close_list))
        print(period)
        '''
        self.period = period
        if (len(close_list) >= period):
            todo_list = close_list[0:period:1]
            # print(todo_list)
            avr = Maths.FloatAverage(todo_list)
            _ma = (close_list[0], avr)
            self.ma.append(_ma)
        else:
            todo_list = close_list[0::1]
            # print(todo_list)
            _ma = (close_list[0], -1)
            self.ma.append(_ma)
        if (len(close_list) > 1):
            # Remove head from close_list
            self.GetMAList(period, close_list[1::1])

    def PrintAll(self):
        print("\nperiod=", self.period)
        print("ma list:")
        # for i,j in self.ma:
        #    print("close={0}, ma={1}".format(i, j))


if __name__ == "__main__":
    json_data = KLine.GetKLineHistory("15min", 100, "btcusdt")
    json_dumps = KLineDataParser.ParseKLineData(json_data)
    print(json_dumps)
    print(type(json_dumps))
    close_list = []
    for item in json_dumps["data"]:
        str = "open:{0}, close:{1}".format(item["open"], item["close"])
        close_list.append(item["close"])
        print(str)
    '''
    ma5 = MA()
    ma5.GetMAList(5, close_list)
    ma5.PrintAll()

    ma10 = MA()
    ma10.GetMAList(10, close_list)
    ma10.PrintAll()

    ma20 = MA()
    ma20.GetMAList(20, close_list)
    ma20.PrintAll()

    ma30_list = MA()
    ma30_list.GetMAList(30, close_list)
    ma30_list.PrintAll()

    ma60_list = MA()
    ma60_list.GetMAList(60, close_list)
    ma60_list.PrintAll()

    print(type(ma60_list.ma[0]))
    ma60_index = 0
    for close, ma30 in ma30_list.ma:
        if (close == ma60_list.ma[ma60_index][0]):
            # print("close={0}, ma30={1}, ma60={2}".format(close, ma30, ma60_list.ma[ma60_index][1]))

            if (int(ma30) == int(ma60_list.ma[ma60_index][1])):
                print("close={0}, ma30={1}, ma60={2}".format(close, ma30, ma60_list.ma[ma60_index][1]))
                next30_price = ma30_list.ma[ma60_index+1][1]
                next60_price = ma60_list.ma[ma60_index+1][1]
                if (next30_price > next60_price):
                    print("long: {0} > {1}".format(next30_price, next60_price))
                elif (next30_price < next60_price):
                    print("short: {0} > {1}".format(next30_price, next60_price))

        ma60_index += 1
    '''
    json_data = KLine.GetKLineHistory("15min", 100, "btcusdt")
    kline_elem_list = KLineDataParser.ParseKLineDataEx(json_data)

    ma = MAEx()
    ma.ComputeMA(15, kline_elem_list)
    ma.Print()
