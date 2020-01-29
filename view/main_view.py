#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tkinter
#import tkmessagebox

# -*- coding: cp936 -*-
# 创建一个矩形，指定画布的颜色为白色
from tkinter import *

root = Tk()
root.state("zoomed")
# 创建一个Canvas，设置其背景色为白色
cv = Canvas(root, bg='white')
# 创建一个矩形，坐标为(10,10,110,110)
cv.create_rectangle(10, 10, 110, 110)
cv.pack()
root.mainloop()
