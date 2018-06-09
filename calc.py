import tkinter  # importing the tkinter GUI tools

calcWindow = tkinter.Tk()  # creating the main window for the calculator
calcWindow.title('Calculator')
calcWindow.geometry('340x380+500+200')
calcWindow['padx'] = 36  # x and y padding are given here
calcWindow['pady'] = 30

for i in range(6):
    calcWindow.rowconfigure(i, weight=1)
for i in range(4):
    calcWindow.columnconfigure(i, weight=1)

display = tkinter.Entry(calcWindow, relief='sunken', borderwidth='3')
display.grid(row=0, column=0, columnspan=4, sticky='news')

C = tkinter.Button(calcWindow, relief='raised', borderwidth=3, text='C')
CE = tkinter.Button(calcWindow, relief='raised', borderwidth=3, text='CE')
C.grid(row=1, column=0, sticky='news')
CE.grid(row=1, column=1, sticky='swen')

zeroDigit = tkinter.Button(calcWindow, relief='raised', borderwidth=3, text='0')
zeroDigit.grid(row=5, column=0, sticky='swen')
digit = 1
for rows in range(4, 1, -1):
    for columns in range(3):
        numberButton = tkinter.Button(calcWindow, relief='raised', borderwidth=3, text=str(digit)).grid(row=rows,
                                                                                                        column=columns,
                                                                                                        sticky='swen')
        digit += 1

operation = ['+', '-', '*', '/']
i = 2
for sign in operation:
    do = tkinter.Button(calcWindow, relief='raised', borderwidth=3, text=sign).grid(row=i, column=3, stick='swen')
    i += 1

result = tkinter.Button(calcWindow, relief='raised', borderwidth=3, text='=')
result.grid(row=5, column=1, columnspan=2, sticky='swen')
calcWindow.mainloop()
