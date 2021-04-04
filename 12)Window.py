from tkinter import *
from PIL import ImageTk,Image

root=Tk()
img=ImageTk.PhotoImage(Image.open("INOY8878.JPG"))

def win():
    win=Toplevel()
    lbl=Label(win,image=img).pack()

button1=Button(root,text="PICTURE",command=win)
button1.pack()

root.mainloop()