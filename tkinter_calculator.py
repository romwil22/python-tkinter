""" 
Python GUI Basic Operation Calculator
"""

from tkinter import *

calculatorWindow = Tk() # create windows widget
calculatorWindow.title("Basic Calculator")

#function section
def clickButton(number):
    current = resultBox.get()
    resultBox.delete(0, END)
    resultBox.insert(0, str(current) + str(number))

def clearButton():
    resultBox.delete(0, END)

def addButton():
    number1 = resultBox.get()
    global getNumber1
    getNumber1 = int(number1)
    resultBox.delete(0, END)

def equalButton():
    number2 = resultBox.get()
    result = getNumber1 + int(number2)
    resultBox.delete(0, END)
    resultBox.insert(0, result)
    
def subtractButton():
    pass

def multipleButton():
    pass

def divideButton():
    pass

# entry widget section
resultBox = Entry(calculatorWindow, width=40, borderwidth=6)

#button widget section
button1 = Button(calculatorWindow, text="1", padx=40, pady=20, command=lambda: clickButton(1))
button2 = Button(calculatorWindow, text="2", padx=40, pady=20, command=lambda: clickButton(2))
button3 = Button(calculatorWindow, text="3", padx=40, pady=20, command=lambda: clickButton(3))
button4 = Button(calculatorWindow, text="4", padx=40, pady=20, command=lambda: clickButton(4))
button5 = Button(calculatorWindow, text="5", padx=40, pady=20, command=lambda: clickButton(5))
button6 = Button(calculatorWindow, text="6", padx=40, pady=20, command=lambda: clickButton(6))
button7 = Button(calculatorWindow, text="7", padx=40, pady=20, command=lambda: clickButton(7))
button8 = Button(calculatorWindow, text="8", padx=40, pady=20, command=lambda: clickButton(8))
button9 = Button(calculatorWindow, text="9", padx=40, pady=20, command=lambda: clickButton(9))
button0 = Button(calculatorWindow, text="0", padx=40, pady=20, command=lambda: clickButton(0))


buttonClear = Button(calculatorWindow, text="Clear", padx=80, pady=20, command=clearButton)
buttonEqual = Button(calculatorWindow, text="=", padx=90, pady=20, command=equalButton)

buttonAdd = Button(calculatorWindow, text="+", padx=40, pady=20, command=addButton)
buttonSubtract = Button(calculatorWindow, text="-", padx=40, pady=20, command=subtractButton)
buttonMultiple = Button(calculatorWindow, text="*", padx=40, pady=20, command=multipleButton)
buttonDivide = Button(calculatorWindow, text="/", padx=40, pady=20, command=addButton)


# grid section

# resultbox
resultBox.grid(row=0, column=0, columnspan=3, padx=5, pady=10) # row 0

# buttons
button1.grid(row=3, column=0) #row 1
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0) #row 2
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=2, column=0)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1) #row 3
button9.grid(row=1, column=2)

button0.grid(row=4, column=0) # row 4
buttonClear.grid(row=4, column=1, columnspan=2)

buttonAdd.grid(row=5, column=0) # row 5
buttonEqual.grid(row=5, column=1, columnspan=2)

buttonSubtract.grid(row=6, column=0) # row 6
buttonMultiple.grid(row=6, column=1) # row 6
buttonDivide.grid(row=6, column=2) # row 6




calculatorWindow.mainloop()



