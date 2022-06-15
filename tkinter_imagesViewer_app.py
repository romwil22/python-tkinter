from tkinter import *
from PIL import ImageTk, Image

# function
def next():
    pass

def back():
    pass

imageViwerWindow = Tk()
imageViwerWindow.title("Image Viewer")
imageViwerWindow.iconbitmap("images/favicon.ico")

#image section
pngImage1 = ImageTk.PhotoImage(Image.open("images/imgsample5.png"))
pngImage2 = ImageTk.PhotoImage(Image.open("images/imgsample2.png"))
pngImage3 = ImageTk.PhotoImage(Image.open("images/imgsample3.png"))
pngImage4 = ImageTk.PhotoImage(Image.open("images/imgsample4.png"))

# label section
labelImage = Label(image=pngImage1)

# button section
exitButton = Button(imageViwerWindow, text="Close Program", command=imageViwerWindow.quit)
backButton = Button(imageViwerWindow, text="<~")
nextButton = Button(imageViwerWindow, text="~>")

# grid section

# label
labelImage.grid(row=0, column=0, columnspan=3)

# buttons
backButton.grid(row=1, column=0)
exitButton.grid(row=1, column=1)
nextButton.grid(row=1, column=2)
imageViwerWindow.mainloop()



