from tkinter import *

root=Tk()

r=IntVar()
r.set("2")


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


Radiobutton(root,text="Option 1",variable=r,value=1,command= lambda :clicked(r.get())).pack()
Radiobutton(root,text="Option 2",variable=r,value=2,command= lambda :clicked(r.get())).pack()


root.mainloop()