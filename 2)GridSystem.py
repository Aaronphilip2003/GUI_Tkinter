from tkinter import *

root=Tk()

myLabel=Label(root,text="Hello Word!")
myLabel2=Label(root,text="My name is Aaron Philip")

myLabel.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)

root.mainloop()