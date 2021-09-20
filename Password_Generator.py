import random
from tkinter import *


def generatePassword():
    length = e1.get()
    length = int(length)
    lowerCase = "abcdefghijklmnopqrstuvwxyz"
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    spec_char = "!@#$%^&*"
    all = lowerCase + upperCase + num + spec_char
    password = "".join(random.sample(all, length))
    passwordLabel=Label(root, text=password, bg="cyan")
    passwordLabel.config(font="Terminal")
    passwordLabel.place(x=230, y=180)


root = Tk()
root.geometry("600x300")
root.configure(bg="cyan")
root.title("Password Generator")
welcomeLabel = Label(root, text="Welcome to your Password Generator!", bg="cyan")
button_gen = Button(root, text="GENERATE", command=generatePassword)
button_gen.config(font='Terminal')
welcomeLabel.config(font=('Terminal', 20))
welcomeLabel.grid(row=0, column=0)
lengthLabel = Label(root, text="Length of Required Password:", bg="cyan")
lengthLabel.config(font="Terminal")
e1 = Entry(root, width=30, borderwidth=7, bg="cyan")
button_gen.place(x=230, y=120)
lengthLabel.place(x=0, y=60)
e1.place(x=350, y=55)
root.mainloop()
