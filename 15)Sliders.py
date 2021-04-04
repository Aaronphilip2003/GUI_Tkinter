from tkinter import *

root=Tk()
slider=Scale(root,from_=0,to=100)
slider.pack(anchor="ne")

slide2=Scale(root,from_=0,to=100,orient=HORIZONTAL)
slide2.pack()

def slide():
    label=Label(root,text=slide2.get()).pack()



button=Button(root,text="Click Me!",command=slide).pack()

root.mainloop()