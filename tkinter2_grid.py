from tkinter import *

rootWindow = Tk() # create windows widget

# label
messageLabel = Label(rootWindow, text="python desktop GUI tkinter") # create label widget
nameLabel = Label(rootWindow, text="rom")
learnLabel = Label(rootWindow, text="python tkinter")

# grid
messageLabel.grid(row=0, column=0) # rows and columns grid positioning in window
nameLabel.grid(row=1, column=1)
learnLabel.grid(row=2, column=2)

rootWindow.mainloop()



