from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox



rootWindow = Tk() # create windows widget
rootWindow.title("python logo")
rootWindow.iconbitmap("images/favicon.ico") # create icon window

# messagebox showinfo
def messageShowInfo():
    response = messagebox.showinfo("information", "pop-up message here")
    Label(rootWindow, text=response).pack()
# messagebox showwarning
def messageShowWaning():
    response = messagebox.showwarning("warning", "pop-up message here")
    Label(rootWindow, text=response).pack()
# messagebox showwarning
def messageShowError():
    response = messagebox.showerror("error", "pop-up message here")
    Label(rootWindow, text=response).pack()

# messagebox showwarning
def messageAskQuestion():
    response = messagebox.askquestion("ask question", "pop-up message here")
    
    if (response == "yes"):
        Label(rootWindow, text=response).pack()
    else:
        Label(rootWindow, text=response).pack()

# messagebox showwarning
def messageAskOkaCancel():
    response = messagebox.askokcancel("ask yes no", "pop-up message here")
    
    if (response):
        Label(rootWindow, text="ok").pack()
    else:
        Label(rootWindow, text="cancel").pack()
    
# messagebox showwarning
def messageAskYesNo():
    response = messagebox.askyesno("ask yes no", "pop-up message here")
    
    if (response):
        Label(rootWindow, text="yes").pack()
    else:
        Label(rootWindow, text="no").pack()


Button(rootWindow, text="message showinfo", command=messageShowInfo).pack()
Button(rootWindow, text="message showwarning", command=messageShowWaning).pack()
Button(rootWindow, text="message showerror", command=messageShowError).pack()
Button(rootWindow, text="message askquestion", command=messageAskQuestion).pack()
Button(rootWindow, text="message askokcancel", command=messageAskOkaCancel).pack()
Button(rootWindow, text="message askyesno", command=messageAskYesNo).pack()

rootWindow.mainloop()