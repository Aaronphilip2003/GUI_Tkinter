from tkinter import *
from tkinter import messagebox

root=Tk()

# Types of buttons:
# showinfo,showwarning,showerror,askquestion,askokcancel,askyesno

def popup():
    messagebox.showinfo("INFO","HELLO WORLD!")

def warn():
    messagebox.showerror(title="ERROR",message="Unfortunately idiots do not have access")

Button(root,text="CLICK",command=popup).pack()
Button(root,text="WARN",command=warn).pack()
root.mainloop()