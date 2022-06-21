from tkinter import *
from PIL import ImageTk, Image

rootWindow = Tk()
rootWindow.title("python logo")
rootWindow.iconbitmap("images/favicon.ico")

def powerTurn():
    powerLabel = Label(rootWindow, text=switch.get()).pack()

switch = StringVar()
turnCheckbox = Checkbutton(rootWindow, text="power switch", variable=switch, onvalue="on", offvalue="off")
turnCheckbox.deselect()
turnCheckbox.pack()

SwitchButton = Button(rootWindow, text="turn", command=powerTurn).pack()

rootWindow.mainloop()