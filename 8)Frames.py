from tkinter import *
from PIL import ImageTk,Image

root=Tk()
def click():
    myLabel=Label(root,text="BUTTON CLICKED!")
    myLabel.pack()




frame=LabelFrame(root,text="FRAME",padx=10,pady=0)
frame.pack(padx=20,pady=20)


button_1=Button(frame,text="CLICK",command=click).pack()





root.mainloop()