from tkinter import *
from common.kline_elem import KLineElem
from common.point import Point
from data_source.kline_api import KLineAPI

# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    _kline_width = 5
    _kline_color = ["red", "green"]
    KLINE_COLOR_RED = 0
    KLINE_COLOR_GREEN = 1

    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)
    '''
    def CreateOneKLine(self, KLineElem):
        kline_width = self._kline_width
        kline_color = None
        p1 = Point(100, 0)
        p2 = Point(p1.x, 0)
        if (KLineElem.open < KLineElem.close):
            p2.y = p1.y + (KLineElem.high - KLineElem.close)
            kline_color = "red"
        else:
            p2.y = p1.y + (KLineElem.high - KLineElem.open)
            kline_color = "green"
        p3 = Point(p1.x, p2.y + abs(KLineElem.open - KLineElem.close))
        p4 = Point(p1.x, p1.y + (KLineElem.high - KLineElem.low))

        p1.Print()
        p2.Print()
        p3.Print()
        p4.Print()

        self.create_line(p1.x, p1.y, p4.x, p4.y, fill=kline_color)
        self.create_rectangle(p2.x-kline_width, p2.y, p3.x+kline_width, p3.y, fill=kline_color)
        # self.create_line(0, 0, 200, 100)
        # self.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
        # self.create_rectangle(50, 25, 150, 75, fill="red")
    '''

    def CreateOneKLine(self, start_point = Point(0,0), kline_elem = KLineElem(0,0,0,0)):
        """
        CreateOneKLine
        :param Point: start position
        :param KLineElem: KLine data
        """
        kline_width = self._kline_width
        kline_color = None
        p1 = Point(start_point.x, start_point.y)
        p2 = Point(p1.x, 0)
        if (kline_elem.open < kline_elem.close):
            p2.y = p1.y + (kline_elem.high - kline_elem.close)
            kline_color = "red"
        else:
            p2.y = p1.y + (kline_elem.high - kline_elem.open)
            kline_color = "green"
        p3 = Point(p1.x, p2.y + abs(kline_elem.open - kline_elem.close))
        p4 = Point(p1.x, p1.y + (kline_elem.high - kline_elem.low))

        p1.Print()
        p2.Print()
        p3.Print()
        p4.Print()

        self.create_line(p1.x, p1.y, p4.x, p4.y, fill=kline_color)
        self.create_rectangle(p2.x - kline_width, p2.y, p3.x + kline_width, p3.y, fill=kline_color)

def main():
    root = Tk()
    myframe = Frame(root)
    myframe.pack(fill=BOTH, expand=YES)
    mycanvas = ResizingCanvas(myframe,width=850, height=400, bg="white", highlightthickness=0)
    mycanvas.pack(fill=BOTH, expand=YES)

    start_point = Point(50, 0)
    kline = KLineElem(100, 300, 400, 5)
    mycanvas.CreateOneKLine(start_point, kline)

    start_point.x += 12
    kline = KLineElem(300, 100, 400, 5)
    mycanvas.CreateOneKLine(start_point, kline)

    # to do here
    kline_elem_list = KLineAPI.GetKLineData("15min", 10, "btcusdt")


    # tag all of the drawn widgets
    mycanvas.addtag_all("all")
    root.mainloop()

if __name__ == "__main__":
    main()