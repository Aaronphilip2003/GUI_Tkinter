from tkinter import *

root=Tk()
root.geometry("400x400")
r=IntVar()

def show():
    label=Label(root,text=r.get()).pack()

box=Checkbutton(root,text="Click",var=r)
box.pack()

button=Button(root,text="Show Selection",command=show).pack()

root.mainloop()