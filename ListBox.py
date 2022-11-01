import imp
from tkinter import *

root = Tk()
root.geometry('200x300')

courselist = ['html', 'css', 'java script', 'php']
var = Variable(value=courselist)

lb = Listbox(root ,height=10, width=20, selectmode="multiple", font="Arial 20",listvariable=var, bg='mistyrose')
lb.pack()

root.mainloop()
