from statistics import geometric_mean
from tkinter import *

root = Tk()
root.geometry("200x200")

var = StringVar()
e1 = Entry(root, font="gorgia 15", textvariable=var).pack()

def fn():
    print(var.get())
b1 = Button(root, text="Enter", command=fn).pack()

root.mainloop()