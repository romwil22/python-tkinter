from tkinter import *
from PIL import ImageTk, Image

rootWindow = Tk() # create windows widget
rootWindow.title("entry designing")
rootWindow.iconbitmap("images/favicon.ico") 


#entry widget
nameEntry = Entry(rootWindow, width=20, borderwidth=2)
nameEntry.insert(0, "enter your name")
nameEntry.pack()

# function
def clickMessage():
    messageLabel = Label(rootWindow, text="hello future developer " + nameEntry.get(), fg="blue")
    messageLabel.pack()
    
clickButton = Button(rootWindow, text="click name", padx=5, pady=5, fg="red", bg="green", command=clickMessage) # create button widget, with function
clickButton.pack()

rootWindow.mainloop()



