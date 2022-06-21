from tkinter import *
from PIL import ImageTk, Image



rootWindow = Tk() # create windows widget
rootWindow.title("frame")
rootWindow.iconbitmap("images/favicon.ico") # create icon window

frame = LabelFrame(rootWindow, padx=80, pady=80)
frame.pack(padx=100, pady=100)

btn = Button(frame, text="exit here", padx=20, pady=20, command=rootWindow.quit)
btn.grid(row=0, column=0)
btn2 = Button(frame, text="exit here 2", padx=20, pady=20, command=rootWindow.quit)
btn2.grid(row=1, column=1)

rootWindow.mainloop()



