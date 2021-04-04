from tkinter import *

root=Tk()
root.geometry("400x400")

clicked=StringVar()
clicked.set("Monday")

def show():
    label=Label(root,text=clicked.get()).pack()

menu=OptionMenu(root,clicked,"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
menu.pack()

button=Button(root,text="Show",command=show).pack()

root.mainloop()