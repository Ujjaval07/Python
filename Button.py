from tkinter import *

root = Tk()
root.geometry('200x200')

b = Button(text="Enter",
           bg='mistyrose',
           fg='blue', 
           activebackground='red', 
           activeforeground='black', 
           bd=5)
b.pack()

root.mainloop()