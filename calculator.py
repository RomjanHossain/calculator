from tkinter import *
from math import *


class Calculator:
    def __init__(self):
        display = Tk()
        display.geometry('460x518')
        display.config(bg='#C9EBE7')
        display.title('Calculator')
        display.iconbitmap('calculator.ico')
        display.resizable(width=True, height=True)
        self.string = StringVar()
        entry = Entry(display, font=("Helvetica", 18), textvariable=self.string, width=30, bd=30, insertwidth=4,
                      justify='right')
        entry.grid(row=0, column=0, columnspan=6)
        entry.configure(background="#FF828E")
        entry.focus()

        values = [
            "radians", ",", "log", "/", "%", "clear",
            "AC", "sin", "asin", "cos", "*", "(",
            ")", "**", "log10", "max", "abs", "-",
            "7", "8", "9", ".", "min", "+",
            "4", "5", "6", "acos", "tan()", "pow",
            "1", "2", "3", "floor", "pi", "e",
            "0", 'king', 'boss', "ceil", "degrees", "="
        ]
        text = 1
        i = 0
        row = 1
        col = 0
        for txt in values:
            padx = 10
            pady = 10
            if i == 6:
                row = 2
                col = 0
            if i == 12:
                row = 3
                col = 0
            if i == 18:
                row = 4
                col = 0
            if i == 24:
                row = 5
                col = 0
            if i == 30:
                row = 6
                col = 0
            if i == 36:
                row = 7
                col = 0
            if txt == '=':
                btn = Button(display, height=2, width=4, padx=padx, pady=pady,
                             text=txt, command=lambda txt=txt: self.equals())
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.configure(background="yellow")

            elif txt == 'clear':
                btn = Button(display, height=2, width=4, padx=padx, pady=pady,
                             text=txt, command=lambda txt=txt: self.delete())
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.configure(background="grey")
            elif txt == 'AC':
                btn = Button(display, height=2, width=4, padx=padx, pady=pady,
                             text=txt, command=lambda txt=txt: self.clearall())
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.configure(background="red")
            elif txt == 'pi':
            	photo=PhotoImage(file="pi2.png")
            	photosize = photo.subsample(10,10)
            	btn = Button(display,width=50,height=50,
                             image=photosize, command=lambda txt=txt: self.addChar(txt))
            	btn.grid(row=row, column=col, padx=1, pady=1)
            else:
                btn = Button(display, height=2, width=4, padx=padx, pady=pady,
                             text=txt, command=lambda txt=txt: self.addChar(txt))
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.configure(background="lightblue")

            col += 1
            i += 1
        display.mainloop()

    def clearall(self):
        self.string.set("")

    def equals(self):
        result = ""

        try:
            result = eval(self.string.get())
            self.string.set(result)
        except:
            result = "INVALID INPUT"
        self.string.set(result)

    def addChar(self, char):
        self.string.set(self.string.get()+(str(char)))

    def delete(self):
        self.string.set(self.string.get()[0:-1])
    def clickpi():
    	self.pi
# display.iconname('calculator.png')


# running the display
if __name__ == '__main__':
    Calculator()
