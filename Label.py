from tkinter import *

root = Tk()
root.geometry('200x200')

l = Label(root, 
          text="This is Label", 
          font=20, fg='blue', 
          bg='mistyrose', 
          bd=5)
l.pack()

root.mainloop()

