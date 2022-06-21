from tkinter import *

rootWindow = Tk() # create windows widget

#entry widget
nameEntry = Entry(rootWindow, width=20, borderwidth=2)
nameEntry.insert(0, "enter your name")
nameEntry.pack()

# function
def clickMessage():
    messageLabel = Label(rootWindow, text="hello future developer " + nameEntry.get(), fg="green")
    messageLabel.pack()
    
clickButton = Button(rootWindow, text="click name", padx=10, pady=10, fg="white", bg="grey", command=clickMessage) # create button widget, with function
clickButton.pack()

rootWindow.mainloop()



