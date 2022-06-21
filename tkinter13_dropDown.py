from tkinter import *
from PIL import ImageTk, Image

rootWindow = Tk()
rootWindow.title("python logo")
rootWindow.iconbitmap("images/favicon.ico")
rootWindow.geometry("200x200")

def daySelected():
    dayLabel = Label(rootWindow, text=day.get()).pack()

day = StringVar()
day.set("days")

listDays = ["mon", "tue", "wed", "thurs", "fri", "sat", "sun"]

daysList = OptionMenu(rootWindow, day, *listDays)
daysList.pack()

selectButton = Button(rootWindow, text="select day", command=daySelected).pack()



rootWindow.mainloop()