from tkinter import *

root=Tk()

e=Entry(root,width=50,borderwidth=5)
e.insert(0,"Enter your Name:")
e.pack()

def onClick():
    myLabel=Label(root,text="Hello "+e.get())
    myLabel.pack()

myButton=Button(root,text="Click",command=onClick,padx=15,pady=5)
myButton.pack()
root.mainloop()