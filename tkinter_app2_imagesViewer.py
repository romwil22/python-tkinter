from tkinter import *
from PIL import ImageTk, Image

# function
def next(imageNumber):
    global backButton
    global nextButton
    global labelImage
    
    labelImage.grid_forget()
    labelImage = Label(image=imageList[imageNumber - 1])
    
    backButton = Button(imageViwerWindow, text="<~", command=lambda: back(imageNumber - 1))
    nextButton = Button(imageViwerWindow, text="~>", command=lambda: next(imageNumber + 1))
    
    if (imageNumber == 4):
        nextButton = Button(imageViwerWindow, text="~>", state=DISABLED)
    
    labelImage.grid(row=0, column=0, columnspan=3)
    backButton.grid(row=1, column=0)
    nextButton.grid(row=1, column=2)

def back(imageNumber):
    global backButton
    global nextButton
    global labelImage
    
    labelImage.grid_forget()
    labelImage = Label(image=imageList[imageNumber - 1])
    
    backButton = Button(imageViwerWindow, text="<~", command=lambda: back(imageNumber - 1))
    nextButton = Button(imageViwerWindow, text="~>", command=lambda: next(imageNumber + 1))
    
    if (imageNumber == 1):
        backButton = Button(imageViwerWindow, text="<~", state=DISABLED)
    
    labelImage.grid(row=0, column=0, columnspan=3)
    backButton.grid(row=1, column=0)
    nextButton.grid(row=1, column=2)

imageViwerWindow = Tk()
imageViwerWindow.title("Image Viewer")
imageViwerWindow.iconbitmap("images/favicon.ico")

#image section
pngImage1 = ImageTk.PhotoImage(Image.open("images2/imgsample1.png"))
pngImage2 = ImageTk.PhotoImage(Image.open("images2/imgsample2.png"))
pngImage3 = ImageTk.PhotoImage(Image.open("images2/imgsample3.png"))
pngImage4 = ImageTk.PhotoImage(Image.open("images2/imgsample4.png"))

# list of images
imageList = [pngImage1, pngImage2, pngImage3, pngImage4]

# label section
labelImage = Label(image=pngImage1)

# button section
exitButton = Button(imageViwerWindow, text="Close Program", command=imageViwerWindow.quit)
backButton = Button(imageViwerWindow, text="<~", command=back, state=DISABLED)
nextButton = Button(imageViwerWindow, text="~>", command=lambda: next(2))

# grid section

# label
labelImage.grid(row=0, column=0, columnspan=3)

# buttons
backButton.grid(row=1, column=0)
exitButton.grid(row=1, column=1)
nextButton.grid(row=1, column=2)

imageViwerWindow.mainloop()



