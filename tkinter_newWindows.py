from tkinter import *
from PIL import ImageTk, Image

rootWindow = Tk() # create windows widget
rootWindow.title("new window")
rootWindow.iconbitmap("images/favicon.ico") # create icon window

def newWindow():
    global img
    topwindow = Toplevel() # create new window
    topwindow.title("new window 2")
    topwindow.iconbitmap("images/favicon.ico")

    img = ImageTk.PhotoImage(Image.open("images2/imgsample1.png")) # create image
    Label(topwindow, image=img).pack(padx=50, pady=50)
    
    buttonClose = Button(topwindow, text="close window", command=topwindow.destroy).pack()



buttonNewWindow = Button(rootWindow, text="new window", command=newWindow).pack()


rootWindow.mainloop()