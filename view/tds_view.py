import tkinter as tk
from _tkinter import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
# Maxmize window
root.state("zoomed")

canvas = Canvas(root, width=500, height=500)
canvas.pack()
canvas.create_line(0, 0, 500, 500)
canvas.create_rectangle(10, 10, 50, 50)

app = Application(master=root)
app.mainloop()