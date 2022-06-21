from tkinter import *
from PIL import ImageTk, Image



rootWindow = Tk()
rootWindow.title("python logo")
rootWindow.iconbitmap("images/favicon.ico")

def clickRadio(status):
    labelRadio = Label(rootWindow, text=status)
    labelRadio.pack()

radiobtn = StringVar()
radiobtn.set("choose your vaccine status:")

# radio button 
# Radiobutton(rootWindow, text="1st dose", variable=radiobtn, value="1st dose", command=lambda: clickRadio(radiobtn.get())).pack()
# Radiobutton(rootWindow, text="Fully vaccinated", variable=radiobtn, value="fully vaccinated", command=lambda: clickRadio(radiobtn.get())).pack()
# Radiobutton(rootWindow, text="1st booster", variable=radiobtn, value="1st booster", command=lambda: clickRadio(radiobtn.get())).pack()
# Radiobutton(rootWindow, text="2nd booster", variable=radiobtn, value="2nd booster", command=lambda: clickRadio(radiobtn.get())).pack()

# radio button with for loop
vaccineStatus = [("1st dose", "1st dose"),
                 ("fully vaccinated", "fully vaccinated"),
                 ("1st booster", "1st booster"),
                 ("2st booster", "2st booster"),]

vaccine = StringVar()
vaccine.set("choose your vaccine status:")

labelRadio = Label(rootWindow, text=vaccine.get())
labelRadio.pack()

for text, status in vaccineStatus:
    Radiobutton(rootWindow, text=text, variable=vaccine, value=status).pack(anchor=W)


buttongetStatus = Button(rootWindow, text="set", command=lambda: clickRadio(vaccine.get()), padx=40, pady=5)
buttongetStatus.pack()

rootWindow.mainloop()



