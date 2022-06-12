from tkinter import *

rootWindow = Tk() # create windows widget

# function
def clickMessage():
    messageLabel = Label(rootWindow, text="tkinter GUI", fg="red")
    messageLabel.pack()
    
clickButton = Button(rootWindow, text="click here", padx=10, pady=10, fg="white", bg="grey", command=clickMessage) # create button widget, with function
clickButton.pack()

rootWindow.mainloop()



