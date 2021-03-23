from tkinter import *
from PIL import ImageTk,Image

root=Tk()

root.title("IMAGES")

img=ImageTk.PhotoImage(Image.open("Aaron.jpg"))
label=Label(image=img)
label.pack()





button_quit=Button(root,text="QUIT",command=root.quit,padx=20,pady=20,bg="RED")
button_quit.pack()

root.mainloop()