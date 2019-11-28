from tkinter import *
from math import *


class Calculator:
        #img = PhotoImage(Image('mitch.jpg'))
    def __init__(self):
        display = Tk()
        #C = Canvas(display, bg='blue', height=460, width=518)

        img = PhotoImage('mitch.jpg')
        display.geometry('470x692')

        # img_l.image = img
        display.config(bg='black')
        display.title('Calculator')
        display.iconbitmap('calculator.ico')
        display.resizable(width=False, height=False)
        self.string = StringVar()
        entry = Entry(display, font=("Helvetica", 18), textvariable=self.string, width=30, bd=30, insertwidth=4,
                      justify='right')
        entry.grid(row=0, column=0, columnspan=6)
        entry.configure(background="white")
        entry.focus()

        values = [
            "radians", ",", "log", "tan()", "%", "clear",
            "AC", "sin", "asin", "cos", "e", "(",
            ")", "**", "log10", "max", "abs", "acos",
            "7", "8", "9", "king", "min", "floor",
            "4", "5", "6", "-", "/", "pow",
            "1", "2", "3", "+", "*", "pi",
            "0", '.', 'sqrt', "ceil", "degrees", "="
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
                #photo3 = PhotoImage(file="equal.png")
                #photosize3 = photo3.subsample(10, 10)
                btn = Button(display, height=2, width=4, padx=padx, pady=pady,
                             text=txt, command=lambda txt=txt: self.equals())
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.configure(background="#46D895")

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
          
            else:
                btn = Button(display, height=2, width=4,
                	font=("Helvetica", 15,"italic bold"),foreground='white',bg='green',
                	 padx=padx, pady=pady,
                             text=txt, command=lambda txt=txt: self.addChar(txt))
                btn.grid(row=row, column=col, padx=1, pady=1)
                btn.configure(background="black")

            col += 1
            i += 1
        # img = PhotoImage('mitch.jpg')
        # img_l = Label(display, image=img)
        # img_l.image = img
        # img_l.place(x=0, y=0, relwidth=1, relheight=1)
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
# display.iconname('calculator.png')


# running the display

if __name__ == '__main__':
    Calculator()
