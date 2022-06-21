from tkinter import *
from PIL import ImageTk, Image



rootWindow = Tk() # create windows widget
rootWindow.title("python logo")
rootWindow.iconbitmap("images/favicon.ico") # create icon window

img = ImageTk.PhotoImage(Image.open("images/android-chrome-192x192.png")) # create image
imgLabel = Label(image=img)
imgLabel.pack()

closeButton = Button(rootWindow, text="close program", command=rootWindow.quit) # create close window button
closeButton.pack()


rootWindow.mainloop()



