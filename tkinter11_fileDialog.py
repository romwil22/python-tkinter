from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog



rootWindow = Tk() # create windows widget
rootWindow.title("open file dialog")
rootWindow.iconbitmap("images/favicon.ico") # create icon window

def openImage():
    global img
    
    # get filename directory
    rootWindow.filename = filedialog.askopenfilename(initialdir=r"C:\Users\Rom\Desktop\PROGRAMMING\python-tkinter\files", title="open file", filetypes=(("png files", "*.png"), ("all files", "*.*")))

    # file directory text label
    labelFilename = Label(rootWindow, text=rootWindow.filename).pack()

    # opening image to window
    img = ImageTk.PhotoImage(Image.open(rootWindow.filename))
    imgLabel = Label(image=img).pack()

imageButton = Button(rootWindow, text="open image", command=openImage, padx=30, pady=5).pack()

rootWindow.mainloop()