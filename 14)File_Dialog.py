from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root=Tk()

def open():
    global img
    root.filename=filedialog.askopenfile(initialdir="F:\PythonPrograms\Temp",title="Select a file",filetypes=(("png files","*.png"),("all files","*.*")))
    myLabel=Label(root,text=root.filename).pack()
    img=ImageTk.PhotoImage(Image.open(root.filename))
    img_Label=Label(image=img).pack()

button=Button(root,text="Open File",command=open).pack()

root.mainloop()