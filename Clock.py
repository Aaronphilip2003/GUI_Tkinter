from time import strftime
from tkinter import *
from tkinter.ttk import *


def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)


root = Tk()
root.title("ClOCK")

label = Label(root, font=('ds-digital', 40), background="black", foreground="cyan")
label.pack(anchor="center")

time()

root.mainloop()
