from tkinter import *
from PIL import ImageTk, Image

rootWindow = Tk()
rootWindow.title("python logo")
rootWindow.iconbitmap("images/favicon.ico")
rootWindow.geometry("300x300") # window size

def resizeWindow():
    labelSlide = Label(rootWindow, text="v: " + str(verticalScale.get()) + " h: " + str(horizontalScale.get())).pack()
    rootWindow.geometry(str(horizontalScale.get())+ "x" + str(verticalScale.get()))

verticalScale = Scale(rootWindow, from_=0, to=300)
verticalScale.pack(anchor=E)

horizontalScale = Scale(rootWindow, from_=0, to=300, orient=HORIZONTAL)
horizontalScale.pack(anchor=S)

labelSlide = Label(rootWindow, text="v: " + str(verticalScale.get()) + " h: " + str(horizontalScale.get())).pack()

scalingButton = Button(rootWindow, text="resize window", command=resizeWindow).pack()

rootWindow.mainloop()