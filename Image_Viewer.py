
#TO BE CONTINUED LATER IT IS JUST TOO BORING

from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("GALLERY")
root.geometry("1000x800")

img1=ImageTk.PhotoImage(Image.open("IMG_7196.PNG"))
img2=ImageTk.PhotoImage(Image.open("IMG_7527.JPG"))
img3=ImageTk.PhotoImage(Image.open("IMG_7682.JPG"))
img4=ImageTk.PhotoImage(Image.open("INOY8878.JPG"))

image_list=[img1,img2,img3,img4]

label_1=Label(image=img4 )
label_1.grid(row=0,column=0)
label_1.pack()

root.mainloop()
