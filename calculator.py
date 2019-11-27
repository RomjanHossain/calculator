from tkinter import *
from math import pi, e, sin, cos, tan, log, log10, ceil, degrees, radians, exp, asin, acos, floor

# some shit for title bar


# doing some fucking things with display
# display = Tk()
# display.geometry('500x600')
# display.config(bg='#C9EBE7')
# display.title('king')
# display.iconbitmap('calculator.ico')
# display.resizable(width=True, height=True)
# # display.iconname('calculator.png')

# # calculator display
# # cal_dis = Entry(display, font=("Helvetica", 14), textvariable=StringVar(
# # ), bg='#F9E9D9', width=40, borderwidth='12px')
# # cal_dis = Entry(display, font=("Helvetica", 14), textvariable=StringVar(
# # ), bg='#F9E9D9')
# # cal_dis.grid(column=0, row=0)
# monitor = Entry(display)
# monitor.grid(column=1,row=0)

# # buttons value
# values = ["7", "8", "9", "/", "%", "clear", "AC",
#           "4", "5", "6", "*", "(", ")", "**",
#           "1", "2", "3", "-", "=", ",", "0", ".", "min", "+", "sin", "asin", "cos", "acos", "tan()",
#           "pow", "log10", "max", "abs", "floor", "pi", "e", "log", "ceil", "degrees", "radians"]

# # making thoes button displayed
# i = 0
# row=1
# col = 1
# for key in values:
# 	padx=10
# 	pady = 10
# 	if i==7:
# 		row=2
# 		col=0

class Calculator:
	def __init__(self):
		display = Tk()
		display.geometry('500x600')
		display.config(bg='#C9EBE7')
		display.title('king')
		display.iconbitmap('calculator.ico')
		display.resizable(width=True, height=True)

		values = ["7", "8", "9", "/", "%", "clear", "AC",
          "4", "5", "6", "*", "(", ")", "**",
          "1", "2", "3", "-", "=", ",", "0", ".", "min", "+", "sin", "asin", "cos", "acos", "tan()",
          "pow", "log10", "max", "abs", "floor", "pi", "e", "log", "ceil", "degrees", "radians"]
		
		i = 0
		row = 1
		col = 0

		display.mainloop()		
# display.iconname('calculator.png')



#running the display
if __name__=='__main__':
	Calculator()