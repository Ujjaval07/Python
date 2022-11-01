from tkinter import *

root = Tk()
root.geometry("300x300")

var = StringVar()
rb1 = Radiobutton(root, text="Male", value=0, variable=var ).pack()
rb2 = Radiobutton(root, text="Female", value=1, variable=var).pack()

def val():
    print(var.get())

b1 = Button(root, text="enter", command=val).pack()

root.mainloop()