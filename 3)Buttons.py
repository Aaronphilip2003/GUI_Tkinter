from tkinter import *

root=Tk()

def myClick():
    myLabel=Label(root,text="You Clicked a Button!!")
    myLabel.pack()


button1=Button(root,text="Click me!",command=myClick,fg="black",bg="Yellow")#padx=50,pady=50,

button1.pack()

root.mainloop()