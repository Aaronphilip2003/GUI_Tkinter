from tkinter import *

root=Tk()

MODES=[
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
]

pizza=StringVar()
pizza.set("Pepperoni")

for text,mode in MODES:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack(#anchor=w
    )

def clicked(value):
    myLabel=Label(root,text=value)
    myLabel.pack()

myButton=Button(root,text="Enter",command=lambda :clicked(pizza.get()))
myButton.pack()

root.mainloop()

